"""
analyze_games.py
Reads a Lichess PGN export, applies inclusion rules, runs Stockfish on every
move I (Peacefulmonkey) played, and writes a CSV with engine fields plus
empty columns for my hand annotations.

Usage: python3 analyze_games.py games.pgn path/to/stockfish out.csv
"""
import csv
import sys

import chess
import chess.engine
import chess.pgn

ME = "peacefulmonkey"
MATE_CP = 1000          # cap mate scores so averages stay readable
BLUNDER = 200           # centipawn drop that counts as a blunder
MISTAKE = 100           # centipawn drop that counts as a mistake
TIME_PER_POS = 0.05     # seconds of engine time per position


def era(date):
    year = date[:4]
    return {"2026": "fresh_2026", "2023": "old_2023"}.get(year, "old_2018")


def exclude_reason(game):
    h = game.headers
    moves = len(list(game.mainline_moves()))
    if h.get("Variant") not in ("Standard", "From Position"):
        return "non-standard variant"
    if "AI level" in h.get("White", "") + h.get("Black", ""):
        return "opponent is a computer"
    if h.get("Event", "").startswith("casual"):
        return "casual (unrated) game"
    if h.get("Termination") in ("Abandoned", "Rules infraction"):
        return "not a played-out game (%s)" % h.get("Termination")
    if moves < 20:  # fewer than 10 full moves
        return "too short (<10 moves)"
    return ""


def speed(tc):
    if tc == "-":
        return "correspondence"
    base, inc = (int(x) for x in tc.split("+"))
    est = base + 40 * inc
    if est < 180:
        return "bullet"
    if est < 480:
        return "blitz"
    return "rapid"


def cp(score, me_white):
    s = score.white() if me_white else score.black()
    return s.score(mate_score=MATE_CP)


def analyze(game, engine):
    me_white = game.headers["White"].lower() == ME
    board = game.board()
    losses = []
    worst = None
    for node in game.mainline():
        move = node.move
        my_turn = board.turn == (chess.WHITE if me_white else chess.BLACK)
        if my_turn:
            before = engine.analyse(board, chess.engine.Limit(time=TIME_PER_POS))
            best = before.get("pv", [None])[0]
            best_san = board.san(best) if best else ""
            ev_before = max(-MATE_CP, min(MATE_CP, cp(before["score"], me_white)))
            san = board.san(move)
            move_no = board.fullmove_number
            board.push(move)
            after = engine.analyse(board, chess.engine.Limit(time=TIME_PER_POS))
            ev_after = max(-MATE_CP, min(MATE_CP, cp(after["score"], me_white)))
            loss = max(0, ev_before - ev_after)
            losses.append(loss)
            if worst is None or loss > worst[0]:
                worst = (loss, move_no, san, best_san, ev_before, ev_after)
        else:
            board.push(move)
    if not losses:
        return None
    return {
        "my_moves": len(losses),
        "acpl": round(sum(losses) / len(losses)),
        "blunders": sum(l >= BLUNDER for l in losses),
        "mistakes": sum(MISTAKE <= l < BLUNDER for l in losses),
        "worst_move_no": worst[1],
        "worst_move": worst[2],
        "engine_best_there": worst[3],
        "eval_before_cp": worst[4],
        "eval_after_cp": worst[5],
        "worst_loss_cp": worst[0],
    }


def main(pgn_path, sf_path, out_path):
    engine = chess.engine.SimpleEngine.popen_uci(sf_path)
    rows = []
    with open(pgn_path) as f:
        while True:
            game = chess.pgn.read_game(f)
            if game is None:
                break
            h = game.headers
            me_white = h["White"].lower() == ME
            result = h["Result"]
            if result == "1/2-1/2":
                my_result = "draw"
            elif (result == "1-0") == me_white:
                my_result = "win"
            else:
                my_result = "loss"
            reason = exclude_reason(game)
            row = {
                "game_id": h["GameId"],
                "url": h["Site"],
                "date": h["UTCDate"].replace(".", "-"),
                "era": era(h["UTCDate"]),
                "event": h["Event"],
                "time_control": h["TimeControl"],
                "speed": speed(h["TimeControl"]),
                "my_color": "white" if me_white else "black",
                "my_elo": h["WhiteElo"] if me_white else h["BlackElo"],
                "opp_elo": h["BlackElo"] if me_white else h["WhiteElo"],
                "my_result": my_result,
                "termination": h["Termination"],
                "custom_start_position": "yes" if h.get("SetUp") == "1" else "no",
                "included": "no" if reason else "yes",
                "exclude_reason": reason,
            }
            if not reason:
                stats = analyze(game, engine)
                if stats:
                    row.update(stats)
                else:
                    row["included"], row["exclude_reason"] = "no", "no moves by me"
            rows.append(row)
            print(row["game_id"], row["included"], file=sys.stderr)
    engine.quit()

    hand_cols = [
        "annotation_mode",        # recalled (fresh) / reconstructed (old)
        "critical_moment_i_see",  # move number I think decided the game
        "agree_with_engine",      # yes / partly / no
        "cause_i_assign",         # time / miscalculation / didnt_see / rushed / tilt / opponent_good / other
        "how_it_felt",            # fresh games only: one or two words
        "understood_position",    # yes / partly / no
        "confidence",             # high / medium / low
        "notes",
    ]
    engine_cols = ["my_moves", "acpl", "blunders", "mistakes", "worst_move_no",
                   "worst_move", "engine_best_there", "eval_before_cp",
                   "eval_after_cp", "worst_loss_cp"]
    cols = list(rows[0].keys())[:15] + engine_cols + hand_cols
    with open(out_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            if r["included"] == "yes":
                r["annotation_mode"] = "recalled" if r["era"] == "fresh_2026" else "reconstructed"
            w.writerow({c: r.get(c, "") for c in cols})


if __name__ == "__main__":
    main(*sys.argv[1:4])

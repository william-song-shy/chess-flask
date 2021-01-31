import chess.pgn
from flask import Flask, render_template, jsonify

pgn = open("lichess_pgn_2021.01.28_songhongyi_vs_lichess_AI_level_1.nPf67Pc3.pgn", encoding="utf-8")
game = chess.pgn.read_game(pgn)
l = []
for node in game.mainline():
	board=node.board()
	l.append({'fen':board.fen(),'is_check': board.is_check(),'is_checkmate':board.is_checkmate(),'comment':node.comment,'turn':node.turn(),'pov':((node.eval().relative.score(mate_score=1000000000))if node.eval() else None)})
#l.append({'fen':board.fen(),'is_check': board.is_check(),'is_checkmate':board.is_checkmate()})
app = Flask(__name__)


@app.route('/api')
def api():
	return jsonify(l)


@app.route('/')
def main():
	return render_template('test.html')

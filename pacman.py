import random

moves = ['a','w','d','s']

def initialize():
	board = [['.' for y in range(0,35)] for x in range(0,15)]

	board[7][19] = 'P'
	board[12][7] = 'G'
	board[3][5] = 'G'
	board[7][32] = 'G'
	board[13][12] = 'G'

	for x in range(20):
		while 1:
			r = random.randint(0,14)
			c = random.randint(0,34)
			if board[r][c] == '.':
				board[r][c] = 'C'
				break

	for y in range(30):
		while 1:
			r = random.randint(0,14)
			c = random.randint(0,34)
			if board[r][c] == '.':
				board[r][c] = 'X'
				break
	return board

def showBoard(board):
	for x in range(15):
			for y in range(35):
				print board[x][y],
			print

if __name__ == '__main__':

	board = initialize()

	while 1:
		showBoard(board)
		move = raw_input("Enter your move : ")
		if move == 'q' :
			break
		elif move not in moves:
			print "Move not recognized"
import random

moves = ['a','w','d','s']
coinsCount = 20

def initializeBoard():
	board = [['.' for y in range(0,35)] for x in range(0,15)]

	board[7][19] = 'P'
	board[12][7] = 'G'
	# board[3][5] = 'G'
	# board[7][32] = 'G'
	# board[13][12] = 'G'

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

def gameOver(score):
	print "Game Over !!!"
	print "Final Score is : %d" % score

class Person(object):
	"""docstring for Person"""

	def __init__(self, x, y):
		super(Person, self).__init__()
		self.new_x = self.x = x
		self.new_y = self.y = y

	def makeMove(self, move):
		if move == 'a':
			self.new_y = self.y - 1
		elif move == 's':
			self.new_x = self.x + 1
		elif move == 'w':
			self.new_x = self.x - 1
		elif move == 'd':
			self.new_y = self.y + 1

	def checkWall(self, board):
		if board[self.new_x][self.new_y] == 'X':
			return 1
		return 0

	def checkCoin(self, board):
		if board[self.new_x][self.new_y] == 'C':
			return 1
		return 0

class Pacman(Person):

	def __init__(self,x,y):
		Person.__init__(self,x,y)
		self.score = 0

	def checkGhost(self,board):
		if board[self.new_x][self.new_y] == 'G':
			return 1
		return 0

	def collectCoin(self,board):
		board[self.new_x][self.new_y] = '.'
		self.score += 1

	def updatePosition(self,board):
		board[self.x][self.y] = '.'
		self.x = self.new_x
		self.y = self.new_y
		board[self.x][self.y] = 'P'

class Ghost(Person):
	
	def __init__(self,x,y):
		Person.__init__(self,x,y)
		self.flag = 0

if __name__ == '__main__':

	board = initializeBoard()
	player = Pacman(7,19)
	ghost = Ghost(12,7)

	while 1:
		showBoard(board)
		move = raw_input("Enter your move : ")
		if move == 'q' :
			break
		elif move not in moves :
			print "Move not recognized"
		else :
			player.makeMove(move)
			if player.checkGhost(board) :
				gameOver(player.score)
				break
			elif player.checkCoin(board) :
				player.collectCoin(board)
			elif player.checkWall(board) :
				continue
			player.updatePosition(board)
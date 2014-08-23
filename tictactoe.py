## Tic Tac Toe implementation without numpy. Derived, but not copied, from Gaurav Chandarana's solution.

board = ['','','','','','','','','']
turn = 1
end = 1
null = ''

print 
"""
This is a simple game of tic tac toe. Player 1, input a number between 0-8 to make your move.
								0 | 1 | 2
								---------
								3 | 4 | 5
								---------
								6 | 7 | 8
"""

def draw_board():
    print "\n\t", board[0], "|", board[1], "|", board[2]
    print "\t", "--------"
    print "\n\t", board[3], "|", board[4], "|", board[5]
    print "\t", "--------"
    print "\n\t", board[6], "|", board[7], "|", board[8], "\n"

def player_move():
	global a
	a = raw_input("Your move...")
	if a not in ('0', '1', '2', '3', '4', '5', '6', '7', '8'):
		print "Choose a number between 0-8."
		a = raw_input("Your move...")
	elif board[int(a)] != null:
		print "That space is already taken."
		a = raw_input("Your move...")
	else:
		a = int(a)

	global turn
	if turn == 1:
		turn = 0
	else:
		turn = 1

def win():
	ways = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
	for i in ways:
		if board[i[0]] == board[i[1]] == board[i[2]] != null:
			winner = board[i[0]]
			print winner, " is the winner!"
			end = 0
	if null not in board:
		return 'TIE'
	return None	
		
def main():
	while end == 1:
		if turn == 1:
			draw_board()
			player_move()
			board[a] = 'X'
			win()
		else:
			draw_board()
			player_move()
			board[a] = 'O'
			win()
			
main()
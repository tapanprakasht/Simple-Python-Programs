#!/usr/bin/python3
class TicTacToe:
  def __init__(self):
    self.board=[0,0,0,0,0,0,0,0,0]
    
    
  def displayBoard(self):
    print("\u001b[2J\u001b[H")
    try:
      for i in range(0,9):
	if self.board[i] != 0:
	  print("\t{}\t".format(self.board[i]))
    except:
      print("Error")
      
    print("-------------------")
    print("|     |     |     |")
    print("|     |     |     |")
    print("|     |     |     |")
    print("-------------------") 
    print("|     |     |     |")
    print("|     |     |     |")
    print("|     |     |     |")
    print("-------------------") 
    print("|     |     |     |")
    print("|     |     |     |")
    print("|     |     |     |")
    print("-------------------") 
    
def main():
  ch='y'
  tic=TicTacToe()
  while ch!='n':
    print("\u001b[2J\u001b[H")			
    print("\t\t----------  TIC TAC TOE   --------------")
    print("\n\n\t\t\tAuthor:Tapan Prakash T")
    print("\t\t\tE-mail:tapanprakasht@gmail.com")
    ch=input("\n\n\n\nStart the game(y/n):")
    t.displayBoard()
if __name__=="__main__":main()


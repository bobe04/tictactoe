
#Här är brädans tomma positioner och tillgänliga positioner

board=['0','1','2','3','4','5','6','7','8']
empty = [0,1,2,3,4,5,6,7,8]

#Det här är en funktion som då tar input av spelare och placerar vart man ska lägga sitt move någonstans, samt vilka markörer man väljer X, och O
def player_input(player):
  player_symbol = ['X','O']
  correct_input = True

  position = int(input('Spelare {playerNo} tur.  Välj vart du ska placera {symbol} '.format(playerNo = player +1, symbol = player_symbol[player])))

  if board[position] == 'X' or board[position] == 'O':
    correct_input = False
  
  if not correct_input:
    print("Plats redan upptagen. :(")
    player_input(player)
  else:
    empty.remove(position)
    board[position] = player_symbol[player] 
    return 1

#Detta är spelbrädan över hur den är designad. 
def display_board():
        print('  |   |   ')
        print(board[0]+' | '+board[1]+' | '+board[2])
        print('  |   |   ')
        print('---------')
        print('  |   |   ')
        print(board[3]+' | '+board[4]+' | '+board[5])
        print('  |   |   ')
        print('---------') 
        print('  |   |   ')
        print(board[6]+' | '+board[7]+' | '+board[8])
        print('  |   |   ')


#Funktion som visar om spelare vunnit, och då alltså fått 3 i rad
def check_win():
  #Här är spelarens markörer och dom olika platserna som är möjliga för att få 3 i rad, alltså får du någon av dessa positioner och dom inte är upptagna så får man vinst.  vv
  player_symbol = ['X','O']
  winning_positions =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

  #Här är då koden som kollar så att någon av spelarna fått dessa positioner ^
  for check in winning_positions:
    first_symbol = board[check[0]]
    if first_symbol != ' ':
      won = True
      for point in check:
        if board[point] !=  first_symbol:
          won = False
          break
      #Om en spelare lyckats få någon av möjliga vinst platser så får dom ett meddelande att man vunnit. vv
      if won:
        if first_symbol == player_symbol[0]:
          print('Spelare 1 vann! :D')
        else:
          print('Spelare 2 vann! :P')
        break
    else:
      won = False

  if won:
    return 0
  else:
    return 1

#Detta är en funktion med hur ingen vann, alltså att det blir ovagjort

def play():
  player = 0
  while empty and check_win():    
    display_board()
    player_input(player)
    player = int(not player)
    
#Om ingen vunnit, alltså ovagjort är detta if satsen.
  if not empty:
    print("Ovagjort, ingen vinnare!")

#Nu är det game time
if __name__ == '__main__':
  play()  
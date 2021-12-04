#main file!

# import whatever modules we need
# 
# loading screen
#     print an ASCII graphics picture
#     "Welcome, chess players."
#     "Do you wish to [p]lay, or [q]uit?"
#     if neither p or q is entered:
#         "Please type in p or q."
#     else if p:
#         "Good to see.  :)"
#         load player entry screen
#     else if q:
#         "Oh...bye then."
#         
# player entry screen
#     "Who is playing white?"
#     input the name
#     "And who's playing black?"
#     input that name
#     "All right.  Ready to play!"
#     load chessboard
#     
# chessboard
#     load 8x8 B&W checkered grid
#     place pieces on appropriate squares
#     begin gameplay loop
# 
# gameplay loop
#     start on white
#     
    def makeMove(self, move):
        self.board[move.startRow][
class Move():
    # maps keys to values
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
        
    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
        
#     if king is in check:
#         restrict valid moves to whatever gets king out of check
#     else:
#         valid moves are what pieces can do, and what isn't obstructed
#         
#     have piece moved when clicked and dragged
#     
#     if move is invalid:
#         it doesn't happen
#     
#     if move is onto opponent's piece:
#         opponent's piece disappears
#         player's piece overtakes it
#
#     if opponent is checkmated:
#         "[color] wins! :D"
#         go to loading screen
#     elif checkmate is impossible:
#         "Stalemate...  :/"
#         go to loading screen
#     else:
#         end turn
#         switch players
    

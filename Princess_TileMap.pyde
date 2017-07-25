# Non-player character finite state machine and maze navigation demo
# NPC simulates NES 8-bit Zelda monsters that switch between states
# of random wander and chase.
# The NPC monster and its state behavior is implemented as a class.
# The 2-D tile map is written as plain Python - no class.
# You may restructure the map to be a class if you prefer.

# Enables call to random.randint(a, b)
import random

  
# Non-player character finite state machine and maze navigation demo
# NPC simulates NES 8-bit Zelda monsters that switch between states
# of random wander and chase.
# The NPC monster and its state behavior is implemented as a class.
# The 2-D tile map is written as plain Python - no class.
# You may restructure the map to be a class if you prefer.

# Enables call to random.randint(a, b)
import random

# Assume our tile map image tiles are 50x50 pixels
TILE_SIZE_PIXELS = 50
# Assume our tile map is 10x10 rowsxcolunms
MAP_SIZE_TILES = 11
# Compute size of map in pixels.
MAP_SIZE_PIXELS = MAP_SIZE_TILES * TILE_SIZE_PIXELS

# Assume tile map value 0 signals a passable tile.
PASSABLE_TILE = 0

# Global constants to define current direction of travel.
MOVE_NONE = 0
MOVE_LEFT = 1
MOVE_RIGHT = 2
MOVE_UP = 3
MOVE_DOWN = 4
global lives

def getMoveRowCol(startRow, startCol, moveDir):
    if moveDir == MOVE_RIGHT:
        startCol += 1
    elif moveDir == MOVE_LEFT:
        startCol -= 1
    elif moveDir == MOVE_UP:
        startRow -= 1
    elif moveDir == MOVE_DOWN:
        startRow += 1
    
    moveTile = [startRow, startCol]
    

    return moveTile


state_stay = 0
state_move = 1
lives = 3

class Monster: 
    # Initializing constructor.
    # Set monster's row, column location to a known passable tile.
    # Set monster's state to STATE_WANDER
    # Set monster's movement direction to a randomly selected
    # passable movement direction.
    # Receive theMap, which is the 2D tile map.
    # Assume theMap is fully initialized.
    def __init__(self, theMap,r,c, the_troll):
        # Advanced work: Write a function that finds a randomly
        # located passable tile for the spawn location.
        
        # Choose a starting or spawn position that is known to 
        # be in an open map tile in your map.
        self.row = r
        self.col = c
        self.counter = 0
        self.troll = the_troll
        #self.row2 = 1
        #self.col2 = 5
        #self.row3 = 1
        #self.col3 = 7

        # Monster begins in wander state.
        #self.state = STATE_WANDER
        #self.state = state_stay
        # From starting map row,col position initialize list of 
        # possible passable move directions.
        # List is a list of named constants MOVE_RIGHT, etc.
       # possibleMoves = getPassableMoveDirections(theMap,self.row, self.col)
        # Set direction to a random choice of one of the passable directions.
   #     self.direction = self.chooseWanderDirection(possibleMoves)
        
    # return tile map row index of monster's location.
    def getRow(self):
        return self.row
 
    # return tile map column index of monster's location.
    def getColumn(self):
        return self.col
        
    # Randomly choose from given list of possible (passable)
    # movement directions.  Example, dirList is [MOVE_LEFT, MOVE_UP]
    # Return integer value corresponding one of the move values 
    # in given dirList.
    # Return MOVE_NONE if dirList is empty.
    #return MOVE_NONE
    #def chooseWanderDirection(self, dirList):
        #numChoices = len(dirList)
       # index = random.randint(0, numChoices-1)
      #  return dirList[index]
    
    # choose monster move direction.
    # Depending on monster's state call either chooseChaseDirection or
    # chooseWanderDirection.
    # Given theMap, tile map 2-D list 
    # Given playerRow, playerColumn tile map indices of player.
    # Return move direction as an integer constant value of
    # MOVE_LEFT, MOVE_RIGHT, MOVE_UP, MOVE_DOWN, or MOVE_NONE.
  #  def chooseDirection(self, theMap, playerRow, playerCol):
     #   self.direction = self.direction # DO NOTHING TO KEEP PYTHON HAPPY
                    
    
    def move(self, theMap, playerRow, playerCol):
        # Probe ahead to next tile ahead along the current move direction.
        # moveTile is a list of two integers giving the row, column indices.
        self.counter += 3
        #make self.counter and set = 0
        if self.counter > 40 and playerCol == self.col:
            
            if theMap[self.row + 1][self.col] == PASSABLE_TILE:
                self.row = self.row + 2
                #counter = counter + 1
                #self.row = counter
                    
                #current_position = self.row
                #state_stay = 0
                #self.state = state_stay
                #state_stay = true
            #keep it from moving forever, move one spot
            self.counter = 0
        else:
            return 0
    def fall(self, theMap):
        global playerRow
        global playerCol
        global lives
        if self.row == playerRow and self.col == playerCol:
            print("Ouch!")
            lives = lives - 1
        self.row = self.row + 1
        if(self.row > 11):
            self.row = self.troll.getRow() + 1
            
     #   moveToCoords = getMoveRowCol(self.row, self.col, self.direction)
      #  row = moveToCoords[0]
       # col = moveToCoords[1]
        # Check if moveTile is passable.
       # if theMap[row][col] == PASSABLE_TILE:
            # Update monster's location to confirmed passable location.
            # Simplify movement by just updating its row, column location rather than by pixels.
         #   self.row = row
        #    self.col = col
       # else:
            #get list of passable tiles
       #     possibleMoves = getPassableMoveDirections(theMap, self.row, self.col)
            # Monster hit a wall, so must choose a new direction.
            # self.chooseState(theMap, playerRow, playerCol)
            # self.chooseDirection(theMap, playerRow, playerCol)
      #      self.direction = self.chooseWanderDirection(possibleMoves)
     #   return 0

#---------- MAIN PY-PROCESSING PROGRAM ---------------

# Setup runs one time at start of program.
# Load tile map and initialize monster and player.
# Must name this function setup for PyProcessing.
def setup():
    # Declare global variables accessible outside of setup function body.
    global spriteList
    global tileMap
    global playerRow
    global playerCol
    global npc
    global npc2
    global npc3
    global npc4
    global npc5
    global npc6
    global gameOver
    global lives
    global theFont
    
    # Since we simplify to move one tile at a time, set a low frame rate
    # so objects move slow enough to see.
    frameRate(8)
    
    theFont = createFont("Arial",16,True)
    # List of sprite tile images.
    spriteList = []
  
    # Open PyProcessing graphics window with given width x height in pixels.
    # Assume map is 10 x 10 tiles at 50x50 pixels per tile image.
    size(MAP_SIZE_PIXELS, MAP_SIZE_PIXELS)
  
    # Tile values -       0              1           2           3                             4
    spriteNames = ["grass.jpg", "tree3.jpg", "ogre50px.png", "Zuvan_facing_forward1.png", "ogre50px2.png", "ogre50px3.png", "spear.png"]
# Note that all sprites are loaded into this list.
    # Create pixel image loaded from given PNG file.
    for name in spriteNames:
        img = loadImage( name )
        spriteList.append(img)
    
    # Create empty list for entire map.
    tileMap = []
  
    # Read input file formatted as rows of integers 0-3, each separated by a space.
    with open("map.txt") as inputFile:
        for line in inputFile:
            # split single string into list of strings, one per integer
            # default split expects space separators.  can provide argument to split on commas, etc.
            line = line.split() 
            # create empty list for current row
            mapRow = []
            for token in line:
                # append each integer after it's converted from string to int
                mapRow.append( int(token) )  
            # append completed row into map      
            tileMap.append(mapRow)
        
    # Set location of player tile to a known empty tile.
    # Advanced work: Modify map input file to designate
    # starting tile of player.
    playerRow = 9
    playerCol = 1
  
    # Create enemy NPC
    npc = Monster(tileMap, 1, 3, None)
    npc2 = Monster(tileMap, 1, 5, None)
    npc3 = Monster(tileMap, 1, 7, None)
    npc4 = Monster(tileMap,npc.getRow() + 1,npc.getColumn(), npc)
    npc5 = Monster(tileMap, npc2.getRow() + 1, npc2.getColumn(), npc2)
    npc6 = Monster(tileMap, npc3.getRow() + 1, npc3.getColumn(), npc3)
  
# Processing repeatedly calls draw to animate and re-paint the screen.
# This function must be named draw.
def draw():
    # Designate global variables to be used in this function.
    global spriteList
    global tileMap
    global playerRow
    global playerCol
    global livesText
    global lives
    
    # Clear window to background color black.
    
        

    numRows = len(tileMap)
    numCols = len(tileMap[0])
  
    # Draw first tile at top left corner
    x = 0
    y = 0
    for r in range(numRows):
        for c in range(numCols):
            # Get map value at row r, column c.
            # Value is an index into spriteList.
            tileNumber = tileMap[r][c]
            image( spriteList[tileNumber], x, y )
            x = x + 50  
        # end of row, move down one tile size in pixels
        y = y + 50
        x = 0
  
    #background(0);
    textFont(theFont,25)
    fill(12,18,10)
    livesText = "Lives: " + str(lives)
    text(livesText, 40, 20)
    if(lives <=0 or npc.getRow() == 9 or npc2.getRow() == 9 or npc3.getRow() == 9):
        background(0)
        fill(255,0,0)
        textFont(theFont,40)
        gameOverText = "GAME OVER"
        text(gameOverText, 200,200)
    if playerRow == 0 and playerCol == 9:
        background(0)
        fill(100,0,100)
        textFont(theFont,30)
        gameOverText = "You have rescued Princess Maleda"
        text(gameOverText, 0,200)
  
    # Draw player as happy prince.
    image( spriteList[3], playerCol*TILE_SIZE_PIXELS, playerRow*TILE_SIZE_PIXELS)
  
    # Draw monsters as mean trolls.
    image( spriteList[2], npc.getColumn()*TILE_SIZE_PIXELS, npc.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[4], npc2.getColumn()*TILE_SIZE_PIXELS, npc2.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[5], npc3.getColumn()*TILE_SIZE_PIXELS, npc3.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[6], npc4.getColumn()*TILE_SIZE_PIXELS, npc4.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[6], npc5.getColumn()*TILE_SIZE_PIXELS, npc5.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[6], npc6.getColumn()*TILE_SIZE_PIXELS, npc6.getRow()*TILE_SIZE_PIXELS)
    # Update NPC state.
    # npc.chooseState(tileMap, playerRow, playerCol)
    # Move NPC one step
    npc.move(tileMap, playerRow, playerCol)
    npc2.move(tileMap, playerRow, playerCol)
    npc3.move(tileMap, playerRow, playerCol)
    npc4.fall(tileMap)
    npc5.fall(tileMap)
    npc6.fall(tileMap)

            
# Define function that is automatically called each time a keyboard even happens.
def keyPressed():
    global tileMap
    global playerRow
    global playerCol
    
    newRow = playerRow
    newCol = playerCol
    
    # Update your position variable by key press.
    if (key == CODED):
        if (keyCode == LEFT):
            newCol = newCol - 1
        elif (keyCode == RIGHT):
            newCol = newCol + 1
        elif (keyCode == UP):
            newRow = newRow - 1
        elif (keyCode == DOWN):
            newRow = newRow + 1
            
        # Check if new tile location is passable.
        if tileMap[newRow][newCol] == PASSABLE_TILE:
            # Commit change of player location.
            playerRow = newRow
            playerCol = newCol
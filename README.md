#go_game
####A flexible Pygame framework that initializes a tiled background from a descriptior file upon startup.

Currently, go_game.py is a program that will load in and display a sequence of tile images as described in a file. The real work of getting the background that you want is in creating a descriptor file. This file gives the program everything that it needs to create a properly sized window and display the tiles correctly. 

From here, go_game contains the framework a simple game loop framework that allows for the addition of any number of game elements.

**Pointing to a new descriptor file:**
Go into go_game.py and edit the global "MAPNAME" parameter to contain the path to the desired file.

**Map descriptor file:**

* First line:
  * [SIZE] [F1] [F2] ... [FX]
    * [SIZE] = "tile-size:20x20"
      * substituting actual sizes of the tiles
    * [FX] = "r:path/to/red.png"
      * the first element is an arbitrary symbol that you'll use in your map design
      * the next element is the path to that tile image
* All remaining lines represent the map matrix, and utilize the symbols you declared in the leading line.



**A very simple example:**
```
tile-size:20x20 r:./img/red.png g:./img/green.png
r g r g r g r g r g r g
g r g r g r g r g r g r
r g r g r g r g r g r g
g r g r g r g r g r g r
r g r g r g r g r g r g
g r g r g r g r g r g r
r g r g r g r g r g r g
g r g r g r g r g r g r
r g r g r g r g r g r g
g r g r g r g r g r g r
r g r g r g r g r g r g
g r g r g r g r g r g r
```
Which outputs:

![go_game Image](http://i.imgur.com/Clwu270.png?1)

#####go_game is powered by the Pygame and Twisted libraries:

![Pygame Image](http://www.pygame.org/docs/pygame_powered.gif)

![Twisted Image](http://twistedmatrix.com/images/header-logo.png)

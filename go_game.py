import pygame

MAPFILE = 'example.map'

class Tile(pygame.sprite.Sprite):

	def __init__(self, gs=None, tilefile=None, xpos=0, ypos=0):

		pygame.sprite.Sprite.__init__(self)

		self.gs = gs

		self.tilefile = tilefile
		self.xpos = xpos
		self.ypos = ypos

		# load the image
		self.image = pygame.image.load(tilefile)
		self.rect = self.image.get_rect()

		# set position
		self.rect.x = self.xpos
		self.rect.y = self.ypos

		# keep original image
		self.orig_image = self.image

	def print_info(self):
		print "tilefile:" + self.tilefile + " x:" + str(self.xpos) + " y:" + str(self.ypos)

class GameSpace:

	# basic setup
	def run(self):

		# basic initialization
		pygame.init()

		# to store board information
		self.mapArray = [] 
		self.mapSymbols = {}
		self.tileSizeX = 0
		self.tileSizeY = 0

		# populate, from file, mapArray list and mapSymbols dictionary
		if self.parse_map_file(MAPFILE) is False:
			print "go_game: failed to load map. exiting."		
			return

		# set up screen based on sizes
		self.screenWidth = len(self.mapArray[0]) * int(self.tileSizeX)
		self.screenHeight = len(self.mapArray) * int(self.tileSizeY)
		self.size = int(self.screenWidth), int(self.screenHeight) 
		self.black = 0, 0, 0
		self.white = 255, 255, 255
		self.screen= pygame.display.set_mode(self.size)
		
		# set up button click values

		# set up game objects
		self.clock = pygame.time.Clock()
		self.Tiles = []
		xpos = 0
		ypos = 0
		# Create all of the tiles
		for row in self.mapArray:
			for tile in row:
				tilefile = self.mapSymbols[self.mapArray[xpos][ypos]]				
				tilex = xpos * self.tileSizeX
				tiley = ypos * self.tileSizeY
				temptile = Tile(self,tilefile,tilex,tiley)
				self.Tiles.append(temptile)				
				xpos += 1
			xpos = 0  # reset xpos
			ypos += 1 # increment ypos

		# start game loop
		runGame = True
		while runGame == True:
			
			# clock tick regulation (framerate)
			self.clock.tick(60)

			# handle user input
			
			# send tick to every game object

			# display game objects
			for tile in self.Tiles:
				self.screen.blit(tile.image, tile.rect)			

			pygame.display.flip()

	# populates mapArray list and mapSymbols dictionary, error checking along the way
	def parse_map_file(self,filename):
		
		f = open(filename)
		firstline = True

		# Parse the file
		for line in f:
			line = line.strip()

			# Read the first line
			if firstline is True:
				specs = line.split() # splits on whitespace

				for spec in specs:

					elements = spec.split(':')

					if len(elements) is not 2:
						print "go_game error: problem in map description file. first line should consist of <type>:<spec> (2 part) elements"
						print "go_game: an example first line could be: \"tile-size:20x20 r:red.png:2 g:green.png\""
						return False
					elif elements[0] == "tile-size":
						sizes = elements[1].split('x')
						if len(sizes) is not 2:
							print "go_game error: map file example usage: \"tile-size:20x20\""
							return False
						self.tileSizeX = int(sizes[0])
						self.tileSizeY = int(sizes[1])
					else:
						self.mapSymbols[elements[0]] = elements[1]
				firstline = False # We're done parsing the first line

			# read the rest of the lines
			else:

				elements = line.split()
				mapLine = []

				for element in elements:

					if element not in self.mapSymbols:
						print "go_game error: invalid symbol in map description."
						return False

					mapLine.append(element)

				self.mapArray.append(mapLine)

		# Now check to make sure that the map dimensions are correct
		if len(self.mapArray) == 0:

			print "go_game error: no map described in file."
			return False

		else:

			length = len(self.mapArray[0])

			for mapLine in self.mapArray:

				if len(mapLine) != length:

					print "go_game error: invalid map description (not a rectangle)."

					return False
		# Now that we've made it through successfully, return true
		print "go_game: map file read successfully"
		return True

	def loop(self):
		placeholder = True

if __name__ == '__main__':
	gs = GameSpace()
	gs.run()

# Constants used in the game

# Camera
CAMERA_WIDTH = 400
CAMERA_HEIGHT = 600

# Objects
PLATFORM_HEIGHT = 10
PLATFORM_WIDTH = 60
VERTICAL_DIST_BTW_PLATFORMS = 100
PLATFORM_COUNT = 6
Y_BASELINE = CAMERA_HEIGHT - 50

SPRITESHEET_PATH = "SpriteSheet.png"
SPRITESHEET_ROW_COUNT = 1
SPRITESHEET_COLUMN_COUNT = 11

JETPACK_EFFECTIVE_FRAMES = 120
JETPACK_SPAWN_CHANCE = 0.1

# Physics
PLAYER_X_SPEED_INCREMENT = 3
FRICTION = 0.8
GRAVITY = 0.5
REBOUNCE_SPEED = -15
JETPACK_SPEED = REBOUNCE_SPEED

# Graphics
FONT_SIZE_1 = 40
FONT_SIZE_2 = 30
PADDING = 10

# Highscore
X_START = 80
Y_START = 80
VERTICAL_SEP_HIGHSCORE = PADDING+30
ROW_COUNT = (CAMERA_HEIGHT - Y_START)//VERTICAL_SEP_HIGHSCORE

# Misc
FRAME_PER_MOVEMENT = 30
HIGHSCORE_PATH = ".highscore.txt"

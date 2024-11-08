import os 

from dotenv import load_dotenv

load_dotenv()

COLLISION_THRESHOLD = float(os.getenv('COLLISION_THRESHOLD'))

G = float(os.getenv('G'))

FPS = int(os.getenv('FPS'))

TIMESTEP = 1/FPS
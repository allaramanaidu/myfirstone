import animal
import bird
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
msg = config['message']['runmsg']
print("message from config.ini:", msg)
a = animal.animalclass()
b = bird.birdclass()

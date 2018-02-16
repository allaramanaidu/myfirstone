import configparser

class birdclass:
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read('config.ini')
		self.msg = self.config['message']['birdmsg']
		print("message from config.ini:", self.msg)

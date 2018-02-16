import configparser

class animalclass:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.msg = self.config['message']['animalmsg']
        print("message from config.ini:", self.msg)

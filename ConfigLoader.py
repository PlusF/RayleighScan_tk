import json


class ConfigLoader:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            config = json.load(f)
        self.mode = config['mode']
        self.dt = int(1000 / config['FPS'])
        self.port = f'COM{config["PORT"]}'
        self.baudrate = int(config['BAUDRATE'])
        self.temperature = int(config['TEMPERATURE'])
        self.folder = config['FOLDER']


def main():
    cl = ConfigLoader('./config.json')
    print(cl.mode)


if __name__ == '__main__':
    main()

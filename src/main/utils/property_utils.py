import configparser

def get_property(key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT'].get(key, 'false')

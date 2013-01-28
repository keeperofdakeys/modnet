import configparser

class ConfigurationFile:
  def __init__(self, conf_file):
    self.config_file = config_file

  def load_config(self):
    config = configparser.ConfigParser()
    config.read(self.config_file)
    return config

  def write_config(self, config_dict):
    config = configparser.ConfigParser()
    config.read_dict(config_dict)
    config.write(file(self.config_file))

import configparser

def main():
  configuration = {}

  for config_name in {'general', 'interfaces', 'connections', 'wireless_connections'}:
    config_file = config_dir + config_name + '.conf'
    if os.path.exists(config_file):
      config = configparser.ConfigParser()
      config.read(config_file)
      configuration[config_name] = config
    else:
      configuration[config_name] = {}



  # make interfaces

  for x in connection_config.load_config():
    connections.append


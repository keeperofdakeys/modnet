import Configuration

def main():
  connection_config = ConfigurationFile("~/.config/modnet/connections.py")
  connections = connection_config.load_config()

  # make interfaces

  for x in connection_config.load_config():
    connections.append


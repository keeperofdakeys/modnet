import configparser
import interfaces

def main():
  configuration = {}
  config_dir = "/home/blueteeth/.config/modnet/"

  for config_name in {'general', 'interfaces', 'connections', 'wireless_connections'}:
    config_file = config_dir + config_name + '.conf'
    if os.path.exists(config_file):
      config = configparser.ConfigParser()
      config.read(config_file)
      configuration[config_name] = config
    else:
      configuration[config_name] = {}

  dhcp_service = DHCP()
  ip_service = IP()
  wpa_supplicant = WpaSupplicant()

  interfaces = {}

  for x in configuration['interfaces']:
    if x['wireless'] == "False":
      interface = Interface(x['name'], dhcp_service, ip_service)
    else:
      interface = WirelessInterface(x['name'], wpa_supplicant)

    interfaces[x['name']] = interface
    

  connections = {}
  wireless_connections = {}

  for x in configuration['connections']:
    connection = Connection(x['name'], x['priority'], x['local'])
    connections[x['name']]

  for x in configuration['wireless_connections']:
    connection = Connection(x['name'], x['priority'],
        x['enc_mode'], x['ssid'], x['psk'], x['local'])
    wireless_connections[x['name']] = connection

  for x in interfaces:
    if isinstance(x, WirelessInterface):
      for y in wireless_connections:
        x.add_connection(y)
    else:
      for y in connections:
        x.add_connection(y)

  dbus_receiver = Dbus_handler()

  # dbus_receiver.network_selected_add_receiver(

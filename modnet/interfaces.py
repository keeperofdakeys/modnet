class Interface:
  def __init__(self, interface):
    self.interface = interface
    self.active = False
    self.local = False
    self.static = False
    self.ip = 0
    self.subnet = 0
    self.connections = []

  def add_connection(self, connection):
    self.connections.add(connection)
    self.connections.sort()

  def remove_connection(self, connection):
    self.connections.remove(connection)

  def select_connection(self, connection):
    if self.connections.dhcp = True
      # do DHCP stuff
    else:
      # do static stuff, based on connection

class WirelessInterface:
  def __init__(self, interface, wpa_supplicant):
    Interface.__init__(self, interface)
    self.wpa_supplicant = wpa_supplicant
    self.wpa_supplicant.add_interface(self.interface)

  def add_connection(self, connection):
    self.wpa_supplicant.add_connection(self.interface, connection)
    Interface.add_connection(self, connection)

  def remove_connection(self, connection):
    self.wpa_supplicant.remove_connection(self.interface, connection)
    Interface.remove_connection(self, connection)

  def select_connection(self, connection):
    self.wpa_supplicant.select_connection(self.interface, connection)
    Interface.select_connection(self, connection)

  def disconnect(self):
    self.wpa_supplicant.disconnect(self.interface)

  def scan(self):
    self.wpa_supplicant.scan(self.interface)

  def get_status(self):
    self.wpa_supplicant.get_status(self.interface)

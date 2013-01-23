class Interface:
  def __init__(self, interface):
    self.interface = interface
    self.active = False
    self.local = False
    self.static = False
    self.ip = 0
    self.subnet = 0

  def add_connection(self, connection):
    pass

  def remove_connection(self, connection):
    pass

  def select_connection(self, connection):
    pass

class WirelessInterface:
  def __init__(self, interface, mode, wpa_supplicant):
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

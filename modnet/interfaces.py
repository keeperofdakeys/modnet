class Interface:
  def __init__(self, interface):
    self.interface = interface
    self.active = False
    self.local = False
    self.static = False
    self.mode = 0
    self.ip = 0
    self.subnet = 0

  def apply_connection(self, connection):
    if self.mode == 1:
      connection.apply_wireless_connection(connection)

class WirelessInterface:
  def __init__(self, interface, mode, wpa_supplicant):
    Interface.__init__(self, interface)
    self.mode = 1
    self.wpa_supplicant = wpa_supplicant

  def apply_wireless_connection(self, wirless_connection):
    # configure wpa_supplicant to connect to this, via some means

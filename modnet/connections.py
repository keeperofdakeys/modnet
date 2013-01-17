class Connection:
  def __init__(self, interface):
    self.interface = interface

  def enable_dhcp(self):
    pass

  def disable_dhsp(self):
    pass

  def set_static_ip(self, ip):
    pass

  def get_ip(self):
    pass

  def set_gateway(self, gateway):
    pass

  def remove_gateway(self):
    pass

class WiredConnection(Connection):
  def __init__(self, interface):
    Connection.__init__(self, interface)
    self.mode = 0

class WirelessConnection(Connection):
  def __init__(self, interface, enc_mode, ssid, psk=None):
    Connection.__init__(self, interface)
    self.enc_mode = enc_mode
    self.ssid = ssid
    self.mode = 1

  def connect(self):
    pass

  def disconnect(self):
    pass

  def status(self):
    pass

class Connection:
  def __init__(self, interface, local):
    self.interface = interface
    self.local = local
    self.mode = 0

  def enable_dhcp(self):
    pass

  def disable_dhsp(self):
    pass

  def set_static_ip(self, ip, subnet):
    pass

  def get_ip(self):
    pass

  def set_gateway(self, gateway):
    pass

  def remove_gateway(self):
    pass

class WirelessConnection(Connection):
  def __init__(self, interface, local, enc_mode, ssid, psk=None):
    Connection.__init__(self, interface, local)
    self.enc_mode = enc_mode
    self.ssid = ssid
    self.mode = 1

  def connect(self):
    pass

  def disconnect(self):
    pass

  def status(self):
    pass

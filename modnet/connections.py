class Connection:
  def __init__(self):

class WirelessConnection(Connection):
  def __init__(self, enc_mode, ssid, psk=None):
    Connection.__init__(self)
    self.enc_mode = enc_mode
    self.ssid = ssid


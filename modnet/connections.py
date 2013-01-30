class Connection:
  def __init__(self, name, priority, local=False):
    self.name = name
    self.priority = priority
    self.active = False
    self.dhcp = True
    self.local = local
    self.static_ip = None
    self.static_subnet = None
    self.active_interface = None

  def setup_static_ip(self, ip, subnet):
    self.dhcp = False
    self.static_ip = ip
    self.static_subnet = subnet
    if self.active:
      self.active_interface.reinitialise()
  
  def setup_dhcp(self):
    self.dhcp = True
    self.static_ip = None
    self.static_subnet = None
    if self.active:
      self.active_interface.reinitialise()

  def activate(self, interface):
    self.active = True
    self.active_interface = interface
    # STUB: do other required stuff

  def deactivate(self, interface):
    self.active = False
    self.active_interface = None
    # STUB: do other required stuff

  def _key(self):
    return (self.name, self.priority)

  def __hash__(self):
    return hash(self._key)

  def __lt__(self, other):
    return _cmp(self, other) < 0

  def __le__(self, other):
    return _cmp(self, other) <= 0

  def __gt__(self, other):
    return _cmp(self, other) > 0

  def __ge__(self, other):
    return _cmp(self, other) >= 0

  def __eq__(self, other):
    return self._key() == other._key()

  def __ne__(self, other):
    return self._key() != other._key()

  def _cmp(self, other):
    if not isinstance(other, Connection):
      return NotImplemented
    comp_pri = self.priority - other.priority
    if comp_pri != 0:
      return comp_pri
    return self.name.__cmp__(other)

class WirelessConnection(Connection):
  def __init__(self, name, priority, enc_mode, ssid, psk=None, local=None):
    Connection.__init__(self, name, priority, local)
    self.enc_mode = enc_mode
    self.ssid = ssid

  def _key(self):
    return (self.name, self.priority, self.enc_mode, self.ssid)

  def __hash__(self):
    return hash(self._key)

  def __eq__(self, other):
    return self._key() == other._key()

  def __ne__(self, other):
    return self._key() != other._key()

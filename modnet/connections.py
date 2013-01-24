class Connection:
  def __init__(self, name, priority):
    self.name = name
    self.priority = priority

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
  def __init__(self, name, priority, enc_mode, ssid, psk=None):
    Connection.__init__(self, name, priority)
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

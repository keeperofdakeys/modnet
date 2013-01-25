class Interface:
  def __init__(self, interface):
    self.interface = interface
    self.active = False
    self.local = False
    self.dhcp = False
    self.ip = 0
    self.subnet = 0
    self.connections = []
    self.active_connection = None

  def add_connection(self, connection):
    self.connections.add(connection)
    self.connections.sort()

  def remove_connection(self, connection):
    if connection is self.active_connection:
      deinitialise(self)
    self.connections.remove(connection)

  def select_connection(self, connection):
    self.active_connection = connection
    self.active_connection.activate()
    self.active = True
    initialise(self)

  def deactivate_connection(self):
    self.active_connection = None
    self.active_connection.deactivate()
    self.active = False
    deinitialise()

  def initialise(self):
    if self.active_connection == None:
      return
    if self.dhcp:
      # STUB: do DHCP stuff
    else:
      # STUB: do static stuff, based on connection

  def deinitialise(self):
    if self.active_connection == None:
      return
    if self.dhcp:
      # STUB: stop DHCP
    else:
      # STUB: undo static stuff

  def reinitialise(self):
    # STUB: do I need stuff here?

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

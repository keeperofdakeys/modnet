import dbus

class ModnetDaemon:
  def __init__(self):
    self.bus = dbus.SystemBus()
    self.proxy = bus.get_object(

  def start_wpa_supplicant(self):
    pass

  def start_dhcpcd(self, interface_name): # STUB: need to add options
    pass

  def start_dhclient(self, interface_name): # STUB: need to add options
    pass

  def stop_dhcpcd(self, interface_name):
    pass

  def stop_dhclient(self, interface_name):
    pass

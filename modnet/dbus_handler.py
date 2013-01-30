class Dbus_handler:
  def __init__(self):
    self.receivers = {}
    self.receivers['scan_done'] = set()
    self.receivers['bss_added'] = set()
    self.receivers['bss_removed'] = set()
    self.receivers['network_added'] = set()
    self.receivers['network_removed'] = set()
    self.receivers['network_selectedd'] = set()
    self.receivers['properties_changed'] = set()

  def scan_done_add_receiver(self, receiver):
    self.receivers['scan_done'].add(receiver)

  def scan_done(self, success):
    for x in self.receivers:
      receiver(success)

  def bss_added_add_receiver(self, receiver):
    self.receivers['bss_added'].add(receiver)

  def bss_added(self, bss, properties):
    for x in self.receivers:
      receiver(bss, properties)

  def bss_removed_add_receiver(self, receiver):
    self.receivers['bss_removed'].add(receiver)

  def bss_removed(self, bss):
    for x in self.receivers:
      receiver(bss)

  def network_added_add_receiver(self, receiver):
    self.receivers['network_added'].add(receiver)

  def network_added(self, network, properties):
    for x in self.receivers:
      receiver(network, properties)

  def network_removed_add_receiver(self, receiver):
    self.receivers['network_removed'].add(receiver)

  def network_removed(self, network):
    for x in self.receivers:
      receiver(network)

  def network_selectedd_add_receiver(self, receiver):
    self.receivers['network_selectedd'].add(receiver)

  def network_selectedd(self, network):
    for x in self.receivers:
      receiver(network)

  def properties_changed_add_receiver(self, receiver):
    self.receivers['properties_changed'].add(receiver)

  def properties_changed(self, properties):
    for x in self.receivers:
      receiver(properties)

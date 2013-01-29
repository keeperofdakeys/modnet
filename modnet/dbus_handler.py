class Dbus_handler:
  def __init__(self):
    self.receivers = {}
    self.receivers['scan_done'] = set()
    self.receivers['bss_added'] = set()
    self.receivers['bss_removed'] = set()
    self.receivers['network_added'] = set()
    self.receivers['network_removed'] = set()
    self.receivers['properties_changed'] = set()

  def scan_done_add_receiver(self, receiver):
    self.receivers['scan_done'].add(receiver)

  def scan_done(self, success):
    for x in self.receivers:
      receiver(success)

  def bss_added_add_receiver(self, receiver):
    self.receivers['bss_added'].add(receiver)

  def bss_added(self, success):
    for x in self.receivers:
      receiver(success)

  def bss_removed_add_receiver(self, receiver):
    self.receivers['bss_removed'].add(receiver)

  def bss_removed(self, success):
    for x in self.receivers:
      receiver(success)

  def network_added_add_receiver(self, receiver):
    self.receivers['network_added'].add(receiver)

  def network_added(self, success):
    for x in self.receivers:
      receiver(success)

  def network_removed_add_receiver(self, receiver):
    self.receivers['network_removed'].add(receiver)

  def network_removed(self, success):
    for x in self.receivers:
      receiver(success)

  def properties_changed_add_receiver(self, receiver):
    self.receivers['properties_changed'].add(receiver)

  def properties_changed(self, success):
    for x in self.receivers:
      receiver(success)

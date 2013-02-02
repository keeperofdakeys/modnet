class Dbus_Thread(threading.Thread):
  def __init__(self, dbus_outgoing_queue, dbus_signal_queue):
    self.outgoing_queue = dbus_outgoing_queue
    self.signal_queue = dbus_signal_queue

  def run(self):
    while True:
      item = self.outgoing_queue.get()
      handle_msg(item)

  def handle_msg(item):
    pass

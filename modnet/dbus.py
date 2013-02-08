import threading

class Dbus_Thread(threading.Thread):
  def __init__(self, msg_queue):
    self.msg_queue = msg_queue

  def run(self):
    while True:
      item = self.msg_queue.get()
      handle_msg(item)

  def handle_msg(item):
    pass

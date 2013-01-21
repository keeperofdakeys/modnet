import os, signal

class WpaSupplicant():
  def __init__(self, pid_file, config_file, prog_path, proc_name, interface):
    self.program = prog_path
    self.process_name = proc_name
    self.prog_args = [self.program,
        "-c %s" % config_file, "-B",
        "-P %s" % pid_file, 
        "-Dnl80211",
        "-i %s" % interface]
    self.started = false

  def start(self):
    if self.running == True:
      return
    os.spawnv(os.P_WAIT, self.program, self.prog_args)
    self.pid = 0
    self.running = True

  def stop(self):
    if self.running == False:
      return
    # test if PID points to the correct process
    os.kill(self.pid, signal.SIGTERM)

  def restart(self):
    stop(self)
    start(self)
    pass

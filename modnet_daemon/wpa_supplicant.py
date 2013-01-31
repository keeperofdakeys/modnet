import os, signal

class WpaSupplicant():
  def __init__(self, pid_file, config_file, prog_path, process_name):
    self.program = prog_path
    self.process_name = proc_name
    self.prog_args = [self.program,
        "-c %s" % config_file,
        "-P %s" % pid_file, 
        "-u", "-B",
        "-Dnl80211"
        # "-i %s" % interface
        ]
    self.running = False

  def start(self):
    if self.running == True:
      return
    os.spawnv(os.P_WAIT, self.program, self.prog_args)
    self.pid = int(file(pid_file).read().strip())
    self.running = True

  def stop(self):
    if self.running == False:
      return
    # test if PID points to the correct process
    os.kill(self.pid, signal.SIGTERM)
    self.running = False

  def restart(self):
    stop(self)
    start(self)

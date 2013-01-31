class Dhclient():
  def __init__(self, pid_file, prog_path, process_name, interface, kjjkjj):
    self.program = prog_path
    self.process_name = proc_name
    self.prog_args = [self.program,
        "-pf %s" % pid_file, 
        interface
        # "-i %s" % interface
        ]
    self.running = false
    pass

  def start(self):
    pass

  def stop(self):
    pass

  def restart(self):
    pass

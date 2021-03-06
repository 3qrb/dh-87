import subprocess
import os



class generator:

    def __init__(self):


        self.module = "PyInstaller"
        self.python = self.getpy()



    def to_exe(self, path):
        cmd = self.python + " -m " + self.module + f" --onefile --noconsole " + str(path)
        command = subprocess.run(cmd,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE
                                 )
        return command.returncode

    def getpy(self):
        if os.name == "nt":
            return "python"
        else:
            return "python3"
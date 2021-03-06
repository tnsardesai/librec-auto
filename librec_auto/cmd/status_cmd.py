from librec_auto.cmd import Cmd
from librec_auto.util import Files
from librec_auto import ConfigCmd
from librec_auto.util import LogFile, Status
import sys
import subprocess


class StatusCmd(Cmd):

    def __str__(self):
        return f"StatusCmd()"

    def setup(self, args):
        pass

    def dry_run(self, config):
        print (f'librec-auto (DR): Running status command {self}')

    def execute(self, config: ConfigCmd):
        self.status = Cmd.STATUS_INPROC
        files = config.get_files()
        target = files.get_exp_path()
#        result_path = files.get_result_path()

        if files.get_sub_count()==0:
            print("librec-auto: No experiments found.")
        else:
            for sub_paths in files.get_sub_paths_iterator():
                status = Status(sub_paths)
                print(status)

        self.status = Cmd.STATUS_COMPLETE



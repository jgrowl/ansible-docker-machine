import time

from ansible import utils
from ansible.utils import template
from ansible.runner.return_data import ReturnData



class ActionModule(object):

    def __init__(self, runner):
        self.runner = runner
        self.basedir = runner.basedir

    def _merge_args(self, module_args, complex_args):
        args = {}
        if complex_args:
            args.update(complex_args)

        kv = utils.parse_kv(module_args)
        args.update(kv)

        return args

    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
        args = self._merge_args(module_args, complex_args)

        module_args_tmp = "name=%s access_token=%s state=%s" % (args.get('name'), args.get('access_token'), args.get('state'))
        module_return = self.runner._execute_module(conn, tmp, 'docker_machine_digitalocean', module_args_tmp, inject=inject,
                                                    complex_args=complex_args, persist_files=True)
        return module_return

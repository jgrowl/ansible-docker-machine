import time

from ansible import utils
from ansible.utils import template
from ansible.runner.return_data import ReturnData



class ActionModule(object):

    def __init__(self, runner):
        self.runner = runner
        self.basedir = runner.basedir

    # def _arg_or_fact(self, arg_name, fact_name, args, inject):
    #     res = args.get(arg_name)
    #     if res is not None:
    #         return res
    #
    #     template_string = '{{ %s }}' % fact_name
    #     res = template.template(self.basedir, template_string, inject)
    #     return None if res == template_string else res

    def _merge_args(self, module_args, complex_args):
        args = {}
        if complex_args:
            args.update(complex_args)

        kv = utils.parse_kv(module_args)
        args.update(kv)

        return args

    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
        args = self._merge_args(module_args, complex_args)

        # path = args.get('path')
        # backup_dir = self._arg_or_fact('backup_dir', 'deployment_backup_dir', args, inject)
        # if not backup_dir:
        #     return ReturnData(conn=conn, result=dict(
        #         failed=True,
        #         msg="Please define either backup_dir parameter or deployment_backup_dir variable"
        #     ))
        #
        # timestamp_generated, timestamp = False, self._arg_or_fact('timestamp', 'deployment_backup_timestamp', args, inject)
        # if not timestamp:
        #     timestamp_generated, timestamp = True, _generate_timestamp()

        driver_config = args.get('driver_config')


        # module_args_tmp = "path=%s backup_dir=%s timestamp=%s" % (args.get('path'), backup_dir, timestamp)
        module_args_tmp = "state=%s name=%s driver=%s" % (args.get('state'), args.get('name'), args.get('driver'))
        module_return = self.runner._execute_module(conn, tmp, 'docker_machine', module_args_tmp, inject=inject,
                                                    complex_args=complex_args, persist_files=True)
        #
        # # uncomment out to make debug output module always verbose
        # # module_return.result['verbose_always'] = True
        #

        return module_return

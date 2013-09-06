# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class DescribeRoutersAction(BaseAction):

    action = 'DescribeRouters'
    command = 'describe-routers'
    usage = '%(prog)s [-r router_id, ...] [-o <owner>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--routers', dest='routers',
                action='store', type=str, default='',
                help='The comma separated IDs of routers you want to list.')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='The status of routers.')

        parser.add_argument('-C', '--console', dest='console',
                action='store', type=str, default='',
                help='ID of the console.')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='The number to specify the verbose level, larger the number, the more detailed information will be returned.')


    @classmethod
    def build_directive(cls, options):
        return {
                'routers': explode_array(options.routers),
                'status': explode_array(options.status),
                'verbose': options.verbose,
                'console': options.console,
                'offset':options.offset,
                'limit': options.limit,
                }

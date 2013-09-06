# coding: utf-8

from qingcloud_cli.iaas_client.actions.base import BaseAction

class CreateRoutersAction(BaseAction):

    action = 'CreateRouters'
    command = 'create-routers'
    usage = '%(prog)s [-c <count>] [-n <router_name>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-c', '--count', dest='count',
                action='store', type=int, default=1,
                help='The number of routers to create.')
        
        parser.add_argument('-n', '--router_name', dest='router_name',
                action='store', type=str, default='',
                help='The short name of routers')
        
        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default='',
                help='ID of the security group you want to apply to router.')
        
    @classmethod
    def build_directive(cls, options):
        required_params = {
                'router_name': options.router_name,
                } 
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'param [%s] should be specified' % param
                return None

        return {
                'count' : options.count, 
                'router_name' : options.router_name,
                'security_group': options.security_group,
                }

# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction
from qingcloud.cli.misc.utils import explode_array

class GetLoadBalancerMonitorAction(BaseAction):

    action = 'GetLoadBalancerMonitor'
    command = 'get-loadbalancer-monitoring-data'
    usage = '%(prog)s -r <resource> -m <meters> -s <step> -b <start_time> -e <end_time> [-f <conf_file>]'
    description = 'Get load balancer related resource monitoring data.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-r', '--resource', dest='resource',
                action='store', type=str, default=None,
                help='the ID of resource, can be loadbalancer_id, listener_id or backend_id.')

        parser.add_argument('-m', '--meters', dest='meters',
                action='store', type=str, default=None,
                help='''list of metering types you want to get.
                If resouce is loadbalancer, meter should be "traffic",
                otherwise meter should be "request".
                ''')

        parser.add_argument('-s', '--step', dest='step',
                action='store', type=str, default=None,
                help='the metering time step, valid steps: "5m", "15m", "30m", "1h", "2h", "1d".')

        parser.add_argument('-b', '--start_time', dest='start_time',
                action='store', type=str, default=None,
                help='the start time(UTF) stamp in the format YYYY-MM-DDThh:mm:ssZ.')

        parser.add_argument('-e', '--end_time', dest='end_time',
                action='store', type=str, default=None,
                help='the end time(UTF) stamp in the format YYYY-MM-DDThh:mm:ssZ.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'resource': options.resource,
                'meters': options.meters,
                'step': options.step,
                'start_time': options.start_time,
                'end_time': options.end_time,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None

        return {
                'resource': options.resource,
                'meters': explode_array(options.meters),
                'step': options.step,
                'start_time': options.start_time,
                'end_time': options.end_time,
                }

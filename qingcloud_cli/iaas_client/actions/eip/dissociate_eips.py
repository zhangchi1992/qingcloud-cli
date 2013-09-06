# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class DissociateEipsAction(BaseAction):

    action = 'DissociateEips'
    command = 'dissociate-eips'
    usage = '%(prog)s -e eip_id, ... [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
     
        parser.add_argument('-e', '--eips', dest='eips',
                action='store', type=str, default='',
                help='The comma separated IDs of eips you want to dissociate with instances.')
            
    @classmethod
    def build_directive(cls, options):
        eips = explode_array(options.eips)
        if not eips:
            return None

        return {'eips': eips}

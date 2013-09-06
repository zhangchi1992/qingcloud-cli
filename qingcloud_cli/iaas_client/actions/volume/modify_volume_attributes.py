# coding: utf-8

from qingcloud_cli.iaas_client.actions.base import BaseAction

class ModifyVolumeAttributesAction(BaseAction):

    action = 'ModifyVolumeAttributes'
    command = 'modify-volume-attributes'
    usage = '%(prog)s -v volume_id [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
     
        parser.add_argument('-v', '--volume_id', dest='volume_id',
                action='store', type=str, default='',
                help='The id of the volume whose attributes you want to modify.')
                
        parser.add_argument('-n', '--volume_name', dest='volume_name',
                action='store', type=str, default='',
                help='Specify the new volume name.')

        parser.add_argument('-d', '--description', dest='description',
                action='store', type=str, default='',
                help='The detailed description of the resource.')

    @classmethod
    def build_directive(cls, options):
        if not options.volume_id:
            return None
            
        return {
                'volume': options.volume_id,
                'volume_name': options.volume_name,
                'description': options.description,
                }

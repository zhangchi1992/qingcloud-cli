# coding: utf-8

from qingcloud_cli.iaas_client.actions.base import BaseAction

class ModifyImageAttributesAction(BaseAction):

    action = 'ModifyImageAttributes'
    command = 'modify-image-attributes'
    usage = '%(prog)s -i <image_id> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
     
        parser.add_argument('-i', '--image_id', dest='image_id',
                action='store', type=str, default='',
                help='the id of the image whose attributes you want to modify.')
                
        parser.add_argument('-n', '--image_name', dest='image_name',
                action='store', type=str, default='',
                help='Specify the new image name.')
        
        parser.add_argument('-d', '--description', dest='description',
                action='store', type=str, default='',
                help='The detailed description of the resource')

    @classmethod
    def build_directive(cls, options):
        if not options.image_id:
            return None
            
        return {
                'image': options.image_id,
                'image_name': options.image_name,
                'description': options.description,
                }

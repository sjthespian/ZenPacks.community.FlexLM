from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class FlexLMLicense(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "FlexLMLicense"

    vendor = None
    version = None
    feature = None
    port = 0
    total = 0
    inuse = 0

    _properties = ManagedEntity._properties + (
        {'id': 'vendor', 'type': 'string'},
        {'id': 'version', 'type': 'string'},
        {'id': 'feature', 'type': 'string'},
        {'id': 'port', 'type': 'int'},
        {'id': 'total', 'type': 'int'},
        {'id': 'inuse', 'type': 'int'},
    )

    _relations = ManagedEntity._relations + (
        ('flexLMDevice', ToOne(ToManyCont,
            'ZenPacks.community.FlexLM.FlexLMDevice',
            'licenseFlexLM',
            ),
        ),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
        },),
    },)

    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    def device(self):
        return self.flexLMDevice()

    def getRRDTemplateName(self):
        return 'LicenseFlexLM'

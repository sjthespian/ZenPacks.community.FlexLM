from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class FlexLMDevice(Device):
    """
    FlexLM device subclass. In this case the reason for creating a subclass of
    device is to add a new type of relation. We want many "FlexLMLicense"
    components to be associated with each of these devices.

    If you set the zPythonClass of a device class to
    ZenPacks.community.FlexLM.FlexLMDevice, any devices created or moved
    into that device class will become this class and be able to contain
    FlexLMLicenses.
    """

    meta_type = portal_type = 'FlexLMDevice'

    vendor_count = None
    feature_count = None
    _properties = Device._properties + (
	{'id': 'vendor_count', 'type': 'int'},
	{'id': 'feature_count', 'type': 'int'},
    )

    # This is where we extend the standard relationships of a device to add
    # our "flexLMLicenses" relationship that must be filled with components
    # of our custom "FlexLMLicense" class.
    _relations = Device._relations + (
        ('licenseFlexLM', ToManyCont(ToOne,
            'ZenPacks.community.FlexLM.FlexLMLicense',
            'flexLMDevice',
            ),
        ),
    )

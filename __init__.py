from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='External Ip',
    icon='exchange',
    description = 'Displays External IP from http://ipecho.net/', 
    dependencies=[
        PluginDependency('main'),
    ],
)


def init():
    import extip

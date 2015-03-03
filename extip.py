import requests

from ajenti.api import plugin
from ajenti.plugins.dashboard.api import DashboardWidget

@plugin
class ExternalIPWidget (DashboardWidget):
    name = _('External Ip')
    icon = 'exchange'

    def init(self):
	self.append(self.ui.inflate('ext-ip:widget'))
	self.find('name').text = _('External Ip')
	self.find('icon').icon = 'exchange'

	req = requests.get('http://ipecho.net/plain')
	if req.status_code == 200:
                self.find('value').text = req.text
        else:
                self.find('value').text = 'Unknown'

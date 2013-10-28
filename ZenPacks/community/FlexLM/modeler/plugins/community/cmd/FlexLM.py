# Module-level documentation will automatically be shown as additional
# information for the modeler plugin in the web interface.
"""
FlexLM
An flexLM plugin that collects licenses under FlexLM control
"""

# When configuring modeler plugins for a device or device class, this plugin's
# name would be community.cmd.FlexLM because its filesystem path within
# the ZenPack is modeler/plugins/community/snmp/FlexLM.py. The name of the
# class within this file must match the filename.

import re

# CommandPlugin is the base class that provides lots of help in modeling data
# that's available by connecting to a remote machine, running command line
# tools, and parsing their results.
from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin

# Classes we'll need for returning proper results from our modeler plugin's
# process method.
from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap


class FlexLM(CommandPlugin):
    # relname is a relationship name, which is the same as the relationship
    # name in the model class:
    relname = 'licenseFlexLM'

    compname = ''

    # this is the class we will instantiate. and it needs to match the container
    modname = 'ZenPacks.community.FlexLM.FlexLMLicense'

    # The command to run.
    command = "/bin/ps -efww| /bin/grep lmgrd | /bin/egrep -v grep | /bin/sed 's/^.*-c //;s/ .*$//' | /bin/sort | /usr/bin/uniq | /usr/bin/xargs -i /usr/bin/lmstat -a -c {}"


    # Query the system to find all of the lmgrd daemons running. From that
    # get the config files, and from those use lmstat to get the vendor
    # daemons and create a component for each feature.

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)

        # call self.relMap() helper method that initializes relname, compname
        rm = self.relMap()

        # For CommandPlugin, the results parameter to the process method will
        # be a string containing all output from the command defined above.

        #matcher = re.compile(r'^\d+\s+\d+\s+(?P<blocks>\d+)\s+(?P<name>\S+)')
	usageMatcher = re.compile(r'^Users of (?P<license>[^:]+):\s+\(Total of (?P<total>\d+) licenses issued.*Total of (?P<inuse>\d+) licenses in use')
	portMatcher = re.compile(r'^License server status: (?P<port>\d+)@')
	vendorMatcher = re.compile(r'^\s*(?P<vendor>[^:]+):\s+(?P<status>(UP|DOWN))\s+v(?P<version>[0-9\.]+)')

	vendor = ''	# FlexLM Vendor for the current features
	vendor_status = ''
	vendor_version = ''
	vendor_count = 0
	feature_count = 0
	lmport = 0
        for line in results.split('\n'):
            line = line.strip()
	    # Parse lmstat output, for port, vendor, feature,
	    # total and inuse licenses
            match = portMatcher.search(line)	# Get server port
            if match:
		lmport = int(match.group('port'))
		vendor = ''		# Clear vendor info
		vendor_status = ''
		vendor_version = ''
            match = vendorMatcher.search(line)	# Get license vendor
            if match:
		vendor = match.group('vendor')
		vendor_status = match.group('status')
		vendor_version = match.group('version')
            match = usageMatcher.search(line)	# Get feature usage
            if match:
		om = self.objectMap()
        	log.info("Found license %s/%s(%s) %d (%d of %d)",
		    vendor, match.group('license'), vendor_version, lmport, int(match.group('inuse')), int(match.group('total')))
                om.id = self.prepId(match.group('license'))
                om.feature = match.group('license')
                om.vendor = vendor
                om.version = vendor_version
		om.port = lmport
                om.total = match.group('total')
                om.inuse = match.group('inuse')
		feature_count = feature_count + 1
		rm.append(om)

        # Return a RelationshipMap that describes the component, relationship
        # on that component, and the module name for the created objects. Pass
        # in the previously built list of ObjectMaps that will be used to
        # populate the relationship.
	return rm
#        return RelationshipMap(
#            compname="lic", relname=relname,
#            modname=modname
#            objmaps=objectmaps)

from hs_restclient import HydroShare, HydroShareAuthBasic
auth = HydroShareAuthBasic(username="christian49", password="19941812Ch")
hs = HydroShare(auth=auth)

abstract = 'My short abstract.'
title = 'My resource'
keywords = ('my keyword 1','my keyword 2')
rtype = 'GenericResource'
fpath = '/home/christian/Desktop/hsJson'
metadata = '[{"coverage":{"type":"period", "value":{"start":"01/01/2000", "end":"12/12/2018"}}}, {"creator":{"name":" Christian E. Camacho"}}]'
extra_metadata = '{"key-1": "value-1", "key-2": "value-2"}'
resource_id = hs.createResource(rtype, title, resource_file=fpath, keywords=keywords, abstract=abstract, metadata=metadata, extra_metadata=extra_metadata)

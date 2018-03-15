from hs_restclient import HydroShare, HydroShareAuthBasic

auth = HydroShareAuthBasic(username="christian49", password = "19941812Ch")
hs = HydroShare(auth = auth)

resource_md = hs.getSystemMetadata('ba3bb556d384478cb11eb7557fce2b8a')

print(" ")
print("Creator        : " + resource_md['creator'])
print("Resource ID    : " + resource_md['resource_id'])
print("Date created   : " + resource_md['date_created'])
print("Resource Type  : " + resource_md['resource_type'])
print("Resource Title : " + resource_md['resource_title'])
print(" ")

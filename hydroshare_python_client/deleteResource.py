from hs_restclient import HydroShare, HydroShareAuthBasic

auth = HydroShareAuthBasic(username="christian49", password = "19941812Ch")
hs = HydroShare(auth = auth)

hs.deleteResource('63e538c32b97482192781e0aeda0f218')

from hs_restclient import HydroShare, HydroShareAuthBasic

auth = HydroShareAuthBasic(username="christian49", password = "19941812Ch")
hs = HydroShare(auth = auth)

# Not working
metadata = {"title:" : "A new title" }
science_metadata_json = hs.updateScienceMetadata('9cd1b4c170634534b86537321c37dd57', metadata=metadata)

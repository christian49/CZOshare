from hs_restclient import HydroShare, HydroShareAuthBasic
auth = HydroShareAuthBasic(username="christian49", password = "19941812Ch")
hs = HydroShare(auth = auth)

# Adding a local file to a HS resource
result = hs.addResourceFile('9cd1b4c170634534b86537321c37dd57',"/home/christian/src/test_file.txt")

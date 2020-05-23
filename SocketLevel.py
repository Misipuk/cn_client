import datetime

from UserRequestsFile import UserRequest

# User
# get users vverhu
# get cafes
# post review
# create cafe

# CafeOwner
# UserFunctions
# Edit functions
# MultiThreading


login = "TestUser"

userRequest = UserRequest()
userRequest.register(login, "test")
at = userRequest.login(login, "test")


userRequest.get_users(at)

"""userRequest.add_cafe(at, {
    "owner": login,
    "name": "2",
    "des": "3",
    "city": "4",
})"""
#userRequest.getCafes(at)
userRequest.getCafeReviews(at, 1)
#userRequest.add_cafe_media(at, 1, "D:\sem6_protocols\cn_client\photos\Tree.jpg")
"""userRequest.add_cafe_review(at, {
    "owner": login,
    "cafe_id": "2",
    "stars": "3",
    "description": "5",
})"""

# userRequest.do_smth()

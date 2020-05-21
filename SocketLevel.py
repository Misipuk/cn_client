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


login = "l"

userRequest = UserRequest()
userRequest.register(login, "p")
at = userRequest.login(login, "p")
userRequest.add_cafe(at, {
    "owner": login,
    "name": "2",
    "des": "3",
    "city": "4",
})

userRequest.get_users(at)

userRequest.add_cafe_media(at, 1, "/home/dbaynak/2020-04-28-144316_364x393_scrot.png")
userRequest.add_cafe_review(at, {
    "owner": login,
    "cafe_id": "2",
    "stars": "3",
    "description": "5",
})

# userRequest.do_smth()

import instaloader
import pandas as pd
 
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
 
# Loading a profile from an Instagram handle
def find_profile(handle):
    profile = instaloader.Profile.from_username(bot.context, handle)
    return profile

# for chk in profile:
#     print(chk)

# profile = find_profile('mmppwr_')
# list_of_content = {'username' : profile.username, 
#                    'userid' : profile.userid, 
#                    'mediacount' : profile.mediacount, 
#                    'followers' : profile.followers, 
#                    'followees' : profile.followees, 
#                    'biography' : profile.biography  }
# json_data = json.dumps(list_of_content, indent=2)
# print(json_data)
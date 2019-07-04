import vk_api
from config import *

vkUser = vk_api.VkApi(token = USER_TOKEN)

USER_ID = 1
result = vkUser.method('users.get',{'user_ids': '1, 445'})

def user_1():
    print(str(result[0]['first_name'])+ ' ' + str(result[0]['last_name']))

user_1()

def user_2():
    print(str(result[1]['first_name'])+ ' '+ str(result[1]['last_name']))

user_2()

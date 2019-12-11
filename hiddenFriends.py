import requests
import time



def id_friends(id,token):
	link = "https://api.vk.com/method/friends.get?user_id={}&access_token={}&v=5.52".format(id,token)
	request = requests.get(link).json()
	
	try:
		friends_list = request ['response']['items']
		print(friends_list)
		print(type(friends_list))
		time.sleep(1)
		return friends_list

	except KeyError:
		print("skip unreadble json")
		return []


def main():
	big_family = []
	print("print id to get friends")
	id = input()
	print("print token to get request")
	token = input()

	friend_list = id_friends(id,token)

	for f_id in friend_list:
		big_family.extend(id_friends(f_id,token))

	print("********************")
	new_big_family = list(dict.fromkeys(big_family))
	
	print(new_big_family)
	print(len(big_family))
	print(len(new_big_family))
	print(100*len(new_big_family)/len(big_family))


if __name__ == "__main__":
	main()

import requests
import time



def id_friends(id,token):
	link = "https://api.vk.com/method/friends.get?user_id={}&access_token={}&v=5.52".format(id,token)
	request = requests.get(link).json()

	try:
		friends_list = request ['response']['items']
		print(friends_list)
		print(type(friends_list))
		time.sleep(0.34)
		return friends_list

	except KeyError:
		print(request)
		time.sleep(0.34)
		return []


def percent_of_unique_friends(len_big_family, len_new_big_family):
	print("all quantity: ", len_big_family)
	print("unique quantity: ", len_new_big_family)
	print("percent: ", 100*len_new_big_family/len_big_family)



def get_dict_friend_id_and_his_friend_list(friend_list, token):

	dict_of_all_friends = {}

	for _ in friend_list:
		id_list = id_friends(_,token)
		dict_of_all_friends[_] = id_list
	return dict_of_all_friends


def get_list_possible_hidden_friends(id,friends_dict):
	
	id = int(id)
	list_of_possible_hidden_friends = []

	print("all clique 3 friends")

	for key,value in friends_dict.items():
		if(id in value):
			print("person_id:", key)
			list_of_possible_hidden_friends.append(key)

	return list_of_possible_hidden_friends


def get_hidden_friends(id_friend_list, possible_hidden_friend_list):
	
	friend_list = []
	
	for _ in possible_hidden_friend_list:
		if not( _ in id_friend_list):
			friend_list.append(_)

	print("numbers of hidden friends: ", len(friend_list))

	for _ in friend_list:
		print("person_id: ", _ )


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
	percent_of_unique_friends(len(big_family),len(new_big_family))
	
	friends_dict = get_dict_friend_id_and_his_friend_list(new_big_family,token)
	print("********************")
	
	possible_hidden_friend_list = get_list_possible_hidden_friends(id,friends_dict)
	get_hidden_friends(friend_list, possible_hidden_friend_list)



if __name__ == "__main__":
	main()

import vk
from getpass import getpass


APP_ID = 5818816


def get_user_login():
    return input('Enter the username:')


def get_user_password():
    return getpass('Please enter your password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline(user_id="")
    return api.users.get(user_ids=friends_online_ids)


def output_friends_to_console(friends_online):
    print("Your friends online:")
    for friend in friends_online:
        print("id: {uid}\nfirst name: {first_name}\nlast name: {last_name}\n".format(**friend))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        print("The username and/or password are not correct.")
        exit(1)
    output_friends_to_console(friends_online)

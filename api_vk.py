# Задача №1
# Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.
#
# Задача №2
# Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.
#
# Задача №3
# Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK

import requests

APP_ID = 7049807
URL = 'https://api.vk.com/method/'
VER = '5.101'
ACC_TOKEN = 'a4541a46101a30b5b599dac3e32458db2f6732e0b8dd9e01870e7b532a8a289ccee36259cc5e32341a4cb'

# Igor = 'https://vk.com/chaikinigorek'
# Sungur = 'https://vk.com/id9380940'
# Sergey = 'https://vk.com/id2020911'
user_1 = 9380940 # Sungur
user_2 = 2020911 # Sergey

params = {
    'v': VER,
    'access_token': ACC_TOKEN,
}

class Uzver:
    """
    This class is user on site vk.com
    """
    def __init__(self, id):
        parametrs = {
            'user_ids': id,
            'v': VER,
            'access_token': ACC_TOKEN,
        }
        response = requests.get(url=f'{URL}users.get', params=parametrs)
        resp = response.json()['response'][0]
        self.user_id = resp['id']
        self.family = resp['last_name']
        self.name = resp['first_name']

    def getfriends(self):
        parametrs = {
            'user_id': self.user_id,
            'fields': 'nickname',
            'v': VER,
            'access_token': ACC_TOKEN,
        }
        response = requests.get(url=f'{URL}friends.get', params=parametrs)
        resp = response.json()['response']['items']
        for i, rsp in enumerate(resp):
            print(f'{" " * 3}{i+1}) {rsp["last_name"]} {rsp["first_name"]} - https://vk.com/id{rsp["id"]}')
        pass

    def __and__(self, other):
        parametrs = {
            'source_uid': self.user_id,
            'target_uid': other.user_id,
            'v': VER,
            'access_token': ACC_TOKEN,
        }
        response = requests.get(url=f'{URL}friends.getMutual', params=parametrs)
        resp = response.json()['response']
        # print(resp)
        for rsp in resp:
            globals()[f'usr_{rsp}'] = Uzver(rsp)
        # prmtrs = 'friends.getMutual'
        # pass

    def __str__(self):
        return f'https://vk.com/id{self.user_id} {self.family} {self.name}'


if __name__ == '__main__':
    pass


sungur = Uzver(user_1)
sergey = Uzver(user_2)
# iam = Uzver()
sungur & sergey
# print(type(sergey.user_id))

# print(sergey)
# print(sungur)
#
#
# sungur.getfriends()
# print(f'\n\n{"=" * 90}\n\n')
# sergey.getfriends()
# print(f'\n\n{"=" * 90}\n\n')
# # iam.getfriends()
#
# kash = Uzver(7649363).getfriends()
# print(kash)
# kash.getfriends()
#
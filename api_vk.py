# Задача №1
# Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.
#
# Задача №2
# Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.
#
# Задача №3
# Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK

import requests
from time import sleep

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
        sleep(0.33)
        response = requests.get(url=f'{URL}users.get', params=parametrs)
        resp = response.json()['response'][0]
        self.user_id = resp['id']
        self.family = resp['last_name']
        self.name = resp['first_name']
        self.fio = self.family + ' ' + self.name
        self.url = f'https://vk.com/id{self.user_id}'

    def getfriends(self):
        parametrs = {
            'user_id': self.user_id,
            'fields': 'nickname',
            'v': VER,
            'access_token': ACC_TOKEN,
        }
        sleep(0.33)
        response = requests.get(url=f'{URL}friends.get', params=parametrs)
        # print(response.json())
        resp = response.json()['response']['items']
        print(f'\nДрузья пользователя {self.fio} ({self.url}):')
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
        sleep(0.33)
        response = requests.get(url=f'{URL}friends.getMutual', params=parametrs)
        resp = response.json()['response']
        # print(resp)
        # lst = [globals()[f'usr_{rsp}'] = Uzver(rsp) for rsp in resp]
        lst_friends = []
        print(f'\nОбщие друзья у пользователей {self.fio} и {other.fio}:')
        for ind, rsp in enumerate(resp):
            globals()[f'usr_{rsp}'] = Uzver(rsp)
            # lst_friends.append(str(globals()[f'usr_{rsp}']))
            lst_friends.append(globals()[f'usr_{rsp}'].__name__())
            print(f'{" " * 3}{ind+1}) {globals()[f"usr_{rsp}"]}')
            # print(globals()[f'usr_{rsp}'])
            # print(rsp)
        # print(lst_friends)

        # print(f'\nОбщие друзья у пользователей {self.fio} и {other.fio}:\n')

        return lst_friends

        # prmtrs = 'friends.getMutual'
        # pass

    def __str__(self):
        return f'{self.family} {self.name} - https://vk.com/id{self.user_id}'


if __name__ == '__main__':
    pass


sungur = Uzver(user_1)
sergey = Uzver(user_2)
# iam = Uzver()
lst = sungur & sergey
# print(type(sergey.user_id))
print(usr_13569560)
# print(sergey)
# print(sungur)
#
#
# sungur.getfriends()
# print(f'\n\n{"=" * 90}\n\n')
# # sergey.getfriends()
# print(f'\n\n{"=" * 90}\n\n')
# # iam.getfriends()
#
print(lst)
# sungur & sungur
# kash = Uzver(7649363).getfriends()
# print(lst)
# kash.getfriends()
#
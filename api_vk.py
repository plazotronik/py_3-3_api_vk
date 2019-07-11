# Задача №1
# Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.
#
# Задача №2
# Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать
# список общих друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.
#
# Задача №3
# Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK

import requests
from time import sleep
from pprint import pprint


URL = 'https://api.vk.com/method/'
VER = '5.101'
ACC_TOKEN = 'a4541a46101a30b5b599dac3e32458db2f6732e0b8dd9e01870e7b532a8a289ccee36259cc5e32341a4cb'


class Uzver:
    """
    This class is a user on site vk.com
    """
    def __init__(self, id=10554929):
        """
        Создание экземпляра класса. По-дефолту Я))

        Таймаут на выполнение запроса 0.2 секунды достаточно для вхождения в ограничение 3 запроса в секунду,
        т.к. дополнительно учитывается время выполнения кода и самого запроса...
        :param id:
        """
        method = 'users.get'
        parametrs = {
            'user_ids': id,
            'v': VER,
            'access_token': ACC_TOKEN,
        }
        sleep(0.2)
        response = requests.get(url=f'{URL}{method}', params=parametrs)
        resp = response.json()['response'][0]
        self.user_id = resp['id']
        self.family = resp['last_name']
        self.name = resp['first_name']
        self.fio = self.family + ' ' + self.name
        self.url = f'https://vk.com/id{self.user_id}'

    def getfriends(self):
        """
        |||Отсебяшка.||| Делал для проверки requests, хотел удалить, но в итоге оставил.
        Вывод всех друзей пользователя без создания из них экземпляров класса (ибо время выполнения кода - дорого).
        Возвращает список словарей.

        Таймаут на выполнение запроса 0.2 секунды достаточно для вхождения в ограничение 3 запроса в секунду,
        т.к. дополнительно учитывается время выполнения кода и самого запроса...
        :param id:
        """
        method = 'friends.get'
        parametrs = {
            'user_id': self.user_id,
            'fields': 'nickname',
            'v': VER,
            'access_token': ACC_TOKEN,
        }
        sleep(0.2)
        response = requests.get(url=f'{URL}{method}', params=parametrs)
        resp = response.json()['response']['items']
        print(f'\nДрузья пользователя {self.fio} ({self.url}):')
        for i, rsp in enumerate(resp):
            print(f'{" " * 3}{i+1}) {rsp["last_name"]} {rsp["first_name"]} - https://vk.com/id{rsp["id"]}')
        return resp

    def __and__(self, other):
        """
        Вывод общих друзей двух пользователей и создание из них экземпляров класса.
        Возвращает словарь.

        Таймаут на выполнение запроса 0.2 секунды достаточно для вхождения в ограничение 3 запроса в секунду,
        т.к. дополнительно учитывается время выполнения кода и самого запроса...
        :param id:
        """
        method = 'friends.getMutual'
        try:
            parametrs = {
                'source_uid': self.user_id,
                'target_uid': other.user_id,
                'v': VER,
                'access_token': ACC_TOKEN,
            }
        except AttributeError:
            print('\nВы ошиблись в написании одного из пользователей. Проверьте ввод и повторите позднее.')
        else:
            if self == other:
                print('\nСравнивать себя со своим псевдонимом не очень то логично...)) '
                      '\nДа и займет уйму времени на создание экземпляров класса. '
                      'Лучше воспользоваться методом .getfriends()\n'
                      'Например, iam.getfriends() или usr_0000000.getfriends()')
            else:
                sleep(0.2)
                response = requests.get(url=f'{URL}{method}', params=parametrs)
                resp = response.json()['response']
                # lst_friends = []
                dict_friends = {}
                print(f'\nОбщие друзья у пользователей {self.fio} и {other.fio}:')
                for ind, rsp in enumerate(resp):
                    globals()[f'usr_{rsp}'] = Uzver(rsp)
                    dict_friends.update({f'usr_{rsp}': globals()[f'usr_{rsp}'].__str__()})
                    # lst_friends.append(globals()[f'usr_{rsp}'].__str__())
                    print(f'{" " * 3}{ind+1}) usr_{rsp}: {globals()[f"usr_{rsp}"]}')
                return dict_friends
                # return lst_friends

    def __str__(self):
        return f'{self.fio} - {self.url}'


if __name__ == '__main__':
    pass

# визуальный разделитель
sep = f'\n\n{"=" * 20}\n'

# == ЭКЗЕМПЛЯРЫ КЛАССА ==
sungur = Uzver(9380940)
sergey = Uzver(2020911)
iam = Uzver()


# == НАХОЖДЕНИЕ ОБЩИХ ДРУЗЕЙ ==
frnds = sungur & sergey
print(sep)
print("Возврат результата операции пересечения.\nСловарь вида {'экземпляр класса': 'описание'}\n")
pprint(frnds)
print(sep)
iam & sungur


# == ВЫЗОВ ИСКЛЮЧЕНИЯ И ПЕРЕСЕЧЕНИЕ С ПСЕВДОНИМОМ ==
print(sep)
iam & 000000
tramp = iam
iam & tramp


# == ВЫВОДИМ ИНФО ОБ ЭКЗЕМПЛЯРЕ КЛАССА ==
print(sep)
print(usr_13569560, '\n') # экземпляр полученный в результате операции пересечения
print(sergey, '\n')
print(sungur, '\n')
print(iam, '\n')


# == ВЫВОД ВСЕХ ДРУЗЕЙ ЭКЗЕМПЛЯРА КЛАССА ==
# sungur.getfriends()
# print(sep)

# usr_13569560.getfriends() # экземпляр полученный в результате операции пересечения
# print(sep)

# sergey.getfriends()
# print(sep))

# friends = iam.getfriends()
# print(sep)
# pprint(friends)

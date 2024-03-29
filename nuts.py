#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Данный скрипт предназначен для синхронизации плейлиста пользователя
    на локальный компьютер"""

import connect, manipulation, sys, os, platform
import logging

reload(sys)
sys.setdefaultencoding('utf-8')

def replace_all(text, dic):
    for i, j in dic.iteritems():
      text = text.replace(i, j, 999)
    return text

def check_symbols(name):
    """Удаляем некорректные символы из названия файла"""
    return replace_all(name, {"|":"", "\\":"", "/":"", ":":"", "*":"", "?":"", "\"":"", "<":"", ">":"", "'":"", "ツ":""})

def check_platform(name):
    if platform.system() == 'Windows':
        name = name.encode('cp1251')
    else:
        name = name.encode('utf8')
    return name

if __name__ == '__main__':
    if os.name == 'nt':
        tmp = os.environ["TMP"]
    elif os.name == 'posix':
        tmp = '/var/tmp'
    logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = r'{0}/nuts.log'.format(tmp))
    if len(sys.argv) > 4:
        path = 'vkmusic'
        for i in list(range(1,len(sys.argv),2)):
            if sys.argv[i] == '-login':
                login = sys.argv[i+1]
            elif sys.argv[i] == '-pass':
                password = sys.argv[i+1]
            elif sys.argv[i] == '-dir':
                path = sys.argv[i+1]
        profile = connect.connect_vk(login, password)

 ''' Оставил как пример на будущее. 
        user    = profile.my_id()
        counter = profile.audio_count(user)
        manip   = manipulation.manip()
        dirr    = manip.check_dir(path)
        for i in xrange(counter):
            print u'-'*80
            artist, title, url = profile.track_info(i)
            name = artist + ' - ' + title
            name = check_symbols(name)
            name = check_platform(name)
            check = manip.check_track(name)
            if check == False:
                manip.download(url, name, dirr)
'''
        del profile
    else:
        print u'''Введены некорректные данные.
Необходимо указакать ./audio_sync.py -login Ваш_логин -pass Ваш_пароль -dir Директория_сохранения
'''
        exit()

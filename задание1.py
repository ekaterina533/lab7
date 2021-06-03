
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#11. Написать программу, которая считывает текст из файла и выводит на экран только
# предложения, начинающиеся с тире, перед которым могут находиться только пробельные
# символы.

import re

if __name__ == '__main__':
    t = open("инд.txt", "r")
    tx= t.read()
    t.close()
    text = re.compile(r'[.|!|?|…]')
    s=(filter(lambda y: y[0:1]=="-", [y.strip() for y in text.split(tx)]))
    print(sorted(s))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#11. Для задания 1 лабораторной работы 7 необходимо дополнительно
# реализовать сохранение и чтение данных из файла формата JSON.

import re
import json


if __name__ == '__main__':
     p = input("Предложение для записи в словарь:")
     with open("t.json", 'w') as f:
        json.dump(p, f)
     with open("t.json", "r") as f:
        tx= json.load(f)
        text = re.compile(r'[.|!|?|…]')
        s = (filter(lambda y: y[0:1] == "-", [y.strip() for y in text.split(tx)]))
        print(sorted(s))

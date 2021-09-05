import numpy as np


class MyCanal:
    def __init__(self, num: int = 0):
        # предварительная настройка типа номеров каналов
        self.canal_name = ['q', 'Твн.пов', 'Твн', 'Тнар']
        if num == 0:
            self.canal_number = [0, 3, 6, 9]
        elif num == 1:
            self.canal_number = [1, 4, 7, 9]
        else:
            self.canal_number = [2, 5, 8, 9]
        # предварительная настройка параметров каналов
        self.name = ''
        self.ro1 = 0.0
        self.ro2 = 0.0
        self.dr = 0.0
        self.canal_value = [0.0, 0.0, 0.0, 0.0]
        self.canal = np.array([])
        self.ro = np.array([])
        self.canal_koef = []
        for i in range(0, 4):
            self.canal_koef.append([0, 0.0, 1])

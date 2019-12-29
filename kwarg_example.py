class Animal:
    def __init__(self, blood, temperature, **kwargs):
        self.blood = blood
        self.dt = kwargs
        self.temperature = temperature

    def warmer(self):
        return self.temperature > 0


class Pig(Animal):
    def __init__(self, breed, *args, **kwargs):
        super(Pig, self).__init__(**kwargs)
        self.breed = breed
        self.order = args


class Dog(Animal):
    def __init__(self, blood, **kwargs):
        super().__init__(blood, **kwargs)


pig = Pig('vanilla', 1, 2, blood='O', temperature=10, sound='oink')
pig.warmer()

pig.order[0]
pig.order[1]
pig.dt['sound']
pig.blood

dog = Dog('AB', name='lucky', age=10, sex='male')

dog.dt


def foo(a, b, c):
    print(a, b, c)


d1 = dict(a=1, b=2, c=3)
d2 = dict(a=1, b=0, c=3)
d3 = dict(a=1, b=0, c=3)
d4 = dict(a=1, b=0, c=3)
d5 = dict(a=1, b=0, c=3)
d6 = dict(a=1, b=0, c=3)
d7 = dict(a=1, b=0, c=3)

foo(**d1)
foo(**d2)
foo(**d3)
foo(**d1)

foo(a=1, b=2, c=3)


class Loss:
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e


class Loss1(Loss):
    def __init__(self, special1, **kwargs):
        self.special1 = special1
        super().__init__(**kwargs)


class Loss2(Loss):
    def __init__(self, special2, a, b, c, d, **kwargs):
        super().__init__(a, b, c, d, **kwargs)
        self.special2 = special2


loss1 = Loss1(10, 1, 2, 3, 4, 5)
loss2 = Loss2(10, 1, 2, 3, 4, 5)


import keras
keras.losses.Loss
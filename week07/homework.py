# Author Andy Fang
# -*- coding:utf-8 -*-

import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def __init__(self, animal_type, animal_shape,animal_character):
        self.animal_type = animal_type
        self.animal_shape = animal_shape
        self.animal_character = animal_character

        #判断是否属于凶猛动物(“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”)
        if animal_type == '食肉' and animal_shape != '小' and animal_character == '凶猛':
            self.is_ferocious = 'Y'
        else:
            self.is_ferocious = 'N'


class Cat(Animal):
    sound = '喵'
    def __init__(self,name,animal_type, animal_shape,animal_character):
        self.name = name
        super(Cat,self).__init__(animal_type,animal_shape,animal_character)

        if self.is_ferocious == 'N':
            self.is_pet = 'Y'
        else:
            self.is_pet = 'N'

class Zoo():
    def __init__(self,name):
        self.name = name

    def add_animal(self, cls):
        obj = cls.__class__.__name__
        if not hasattr(self, obj):
            li = []
            li.append(cls)
            setattr(self, obj, li)
        else:
            li = getattr(self, obj)
            #判断是否已经存在该动物，没有的话添加到该动物列表
            if cls not in li:
                li.append(cls)


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫1', '食肉', '小', '温顺')
    cat2 = Cat('大花猫2', '食肉', '中', '凶猛')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)
    z.add_animal(cat2)
    # 动物园是否有猫这种动物

    have_cat = getattr(z, 'Cat')
    for i in have_cat:
        print(i.name,i.animal_type, i.animal_shape,i.animal_character, i.is_pet)








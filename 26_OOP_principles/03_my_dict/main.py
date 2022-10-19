class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


new_dict = MyDict()
new_dict['Вася'] = 20
new_dict['Саша'] = 25
new_dict['Степа'] = 30
print(new_dict)
print(new_dict.get('Вася'))

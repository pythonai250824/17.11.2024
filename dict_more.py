info_dict = {"name": "oren",
             "age": 31,
             "height": 1.98,
             "smoker": False,
             "siblings": [18, 20],
             "address": {"city": "tel-aviv", "street": "ben-yehuda", "number": 12}}
print(info_dict)

print('keys', list(info_dict.keys()))

print('values', list(info_dict.values()))

for key in info_dict.keys():
    print(f"{key}: {info_dict.get(key)}")

print(info_dict.items())
print('from items:', dict(info_dict.items()))

for one_item in info_dict.items():
    key = one_item[0]
    value = one_item[1]
    print(f'key = {key}, value = {value}')

for key, value in info_dict.items():
    print(f'key = {key}, value = {value}')

# unpack
list_num = [[1, 2], [3, 4], [5, 6, 99]]
for item in list_num:
    print(item[0], item[1])
    x = item[0]
    y = item[1]
for x, y, *z in list_num:
    print(x, y, z)

info_dict_dup = info_dict.copy()  # the same dict
info_dict_dup['name'] = 'suzi'
print(info_dict_dup['name'], info_dict['name'])

# I have a cool dict , I want a new one with the same keys but empty values
print(dict.fromkeys(info_dict.keys(), None))
print(info_dict.fromkeys(info_dict.keys(), None))

#del info_dict_dup['name']  # delete
# get name value , and then delete
print(info_dict_dup)
name = info_dict_dup.pop('name')
print(name)
print(info_dict_dup)

print(len(info_dict_dup))
print(info_dict_dup['address']['street'])
print(len(info_dict_dup['address']))

print(str(info_dict_dup).replace("{", "").replace("}", "")
      .replace(",", ""))

# Bonus
import json
print(type(json.loads('{"name": "Alice", "age": 30, "city": "New York"}')))

# Bonus

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

# match oper:
#     case "+": plus(x, y)
#     case "-": minus(x, y)
#     case "*": mul(x, y)
#     case "/": div(x, y)

dict_oper = {"+": plus, "-": minus, "*": mul, "/": div}

x = int(input('enter x: '))
oper = input('enter oper: ')
y = int(input('enter y: '))
#          plus(x, y)

dict_oper_lm = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
                "*": lambda a, b: a * b, "/": lambda a, b: a / b}
print(dict_oper_lm[oper](x, y))
# 4 * 3 + 4

# expre = input('enter exp: ')  # 4 + 5 * 2 / 3
# exp = expre.split()  # 4, +, 5, *, 2, /, 3
#                      # 18 /, 3
# result = int(exp.pop(0))
# while len(exp) > 0:
#           dict_oper_lm = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
#                 "*": lambda a, b: a * b, "/": lambda a, b: a / b}
#           result = dict_oper_lm[exp[0]](result, int(exp[1]))
#           exp.pop(0)
#           exp.pop(0)
# print(result)

print('1. print 5 + 10')
print('2. print hello')
print('3. print ***')
oper = {'1': lambda : 5 + 10, '2': lambda: 'hello', '3': lambda: '***'}
choice = input('whats your choice')
print(oper[choice]())








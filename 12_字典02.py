# 遍历字典
person = {"name":"zwj","age":"18","address":"macheng"}
for key,value in person.items():
    print(key + ":" + value);

# 遍历字典的key
for key in person.keys():
    print(key + ":" + person[key]);

# 遍历字典的value
for value in person.values():
    print(value);

numbers = [1,2,1,4,3,2,5,6];
# set()去重
for number in set(numbers):
    print(number);

person01 = {"name":"zwj","age":23}
person02 = {"name":"dyz","age":22}

# 字典列表
persons = [person01,person02];
for p in persons:
    print(p);

alias = []
for number in range(1,30):
    if number % 3 == 0:
        alia = {"name": "aaa", "age": "18", "address": "macheng"};
    else:
        alia = {"name": "bbb", "age": "32", "address": "beijing"};
    alias.append(alia);

print(alias[:4]);




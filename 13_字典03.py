# 字典中存储列表
student = {"name":"zwj","courses":["math","chinese","english"]};
print(student);

for course in student["courses"]:
    print(course);

name_languages = {"zwj":["java","python"],"zth":["java","c"]}

for name,languages in name_languages.items():
    print(name);
    for language in languages:
        print(language)

users = {
    "zwj":{"age":"22","address":"mahceng"},
    "dyz":{"age":"21","address":"huangzhou"}
}

for username,userinfo in users.items():
    print(username);
    print(userinfo["age"] + ":" + userinfo["address"]);

# 切片

# 含头不含尾
names = ["zwj","dyz","aaa","bbb","ccc"];
print(names[0:3]);

# 从开头开始
print(names[:3]);
# 从末尾结束
print(names[1:]);

# 负数索引返回离列表末尾相应距离的元素
print(names[-2:]);


for num in names[-2:]:
    print(num);

# 浅拷贝 复制数组的引用
usernames = names;
print(usernames);

# 深拷贝
names1 = names[:];
print(names1)


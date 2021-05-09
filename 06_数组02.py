# 遍历数组
# 每个缩进的代码行都是循环的一部分
names = ["James","Davis","Kury"];
for name in names:
    print(name);
    print(name.upper());

print("循环结束");


# range()
for num in range(1,10):
    print(num);

# list()转换为列表
numbers = list(range(1,10));
print(numbers);

# range()指定步长
for num in range(2,11,2):
    print(num);

squares = [];
for num in range(1,10):
    squares.append(num ** 2);
print(squares);


# 数字数组常用函数
print(min(squares));
print(max(squares));
print(sum(squares));

# 列表解析
squares = [value ** 2 for value in range(1,6)];
print(squares);

arr = list(range(1,1000001));
print(sum(arr));

for num in range(1,21,2):
    print(num);


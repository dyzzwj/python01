# 定义一个列表
numbers = [1,2,3,4,5,6];
print(numbers);

# 数组的元素从0开始
print(numbers[0]);
print(numbers[-1]);

numbers[1] = 11;
print(numbers[1]);

# 向数组末尾追加元素
numbers.append(100);
print(numbers[-1]);

# 指定位置添加一个元素
numbers.insert(0,200);
print(numbers);

# 数组长度
print(len(numbers));

# 删除一个元素
del numbers[0];
print(numbers);
print(len(numbers));

# 弹出最后一个元素 并返回
num = numbers.pop();
print(num);
print(numbers);

# 弹出指定位置的元素
num = numbers.pop(1);
print(num);
print(numbers);

# 删除指定元素
numbers.remove(3);
print(numbers)


# sort():修改数组本身
strs = ["cba","abc","bca"];
print(strs);
strs.sort();
print(strs);

numbers.sort(reverse=True);
print(numbers);

# sorted():临时排序
print(sorted(numbers));
print(numbers);

# 反转
names = ["zwj","dyz","ay"];
print(names);
names.reverse();
print(names);

# 数组长度
print(len(names));
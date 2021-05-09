numbers1 = [1,2,5,7];
numbers2 = [2,3,7,9];

for num in numbers1:
    if num in numbers2:
        print(str(num) + "在numbers中");
    else:
        print(str(num) + "不在在numbers中");
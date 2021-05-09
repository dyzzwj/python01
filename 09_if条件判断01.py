cars = ["audi","bmw","byd","jili"];
for car in cars:
    if "bmw" == car:
        print(car.upper());
    else:
        print(car);


name = "zwj";
print("zjw" == name);
if "zjw" == name:
    print("aaaa");


# and or

ages = [32,23];
if ages[0] > 30 and ages[1] > 30:
    print(ages[1]);
ages[1] = 33;
if ages[0] > 30 and ages[1] > 30:
    print(ages[1]);

if (ages[0] > 22) or ages[1] > 22:
    print("or")


print("jili" in cars);
print("jili" not in cars);


if True:
    print("True");
if False:
    print("False");

age = 18

if (age > 10):
    print("年龄大于10");
else:
    print("年龄小于10");


num = 51;
i = 0;
if num > 50:
    print("大于50");
    i = 10;
elif num < 70:
    print("小于70");
    i = 20;
else:
    print("大于70");
    i = 30;

print(i);

names = [];

# 数组不包含元素时返回false
if names:
    print("names不为空");
else:
    print("names为空");

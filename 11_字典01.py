# 字典"一系列键值对
person = {"name":"zwj","age":18}
print(person["name"]);
print(person["age"]);
print(person);

position = {}
position["x"] = 100;
position["y"] = 200;
print(position);

alien = {"x": 20, "y" : "30","speed": "slow"};
if alien["speed"] == "slow":
    move = 1;
elif alien["speed"] == "meddium":
    move = 2;
else:
    move = 3;

alien["x"] = alien["x"] + move;
print(alien)

student = {"name":"zwj","age":"22","sex":"female"};
print(student);
del student["age"];
print(student);








# 创建一个名为guests的列表，并将其元素设置为"Alice", "Bob", "Charlie"。
guests = ["Alice", "Bob", "Charlie"]
# 打印guests列表
print(guests)

# Alice来不了了，将其从列表中删除，并打印出来它来不了了。
break_guest = "Alice"
guests.remove(break_guest)
print(f"{break_guest} will not come")

# 修改嘉宾名单，将Alice替换为David。
guests[0] = "David"
print(guests)

# 给每位嘉宾发送邀请函
for guest in guests:
    print(f"Dear {guest}, please come to my party on Saturday! \n")

# 再邀请三位嘉宾
guests.append("Eve")
guests.append("Frank")
guests.append("Grace")
print(guests)
print("We have a new batch of guests! And I found a bigger table!\n")

guests.insert(0, "Henry")
guests.insert(2, "Ivy")
guests.append("John")
print(guests)

for guest in guests:
    print(f"Dear {guest}, please come to my party on Saturday!\n")

# 打印我只能邀请两位嘉宾
print("Sorry, I can only invite two guests. \n")

# 使用pop()方法不断删除列表中的元素，直到只剩下两位嘉宾，并发送道歉信。
while len(guests) > 2:
    cancled_peopele = guests.pop()
    print(f"Sorry for {cancled_peopele}, we don't have enough seat!")

for guest in guests:
    print(f"Dear {guest}, You are still in the list!\n")

del guests[0]
del guests[0]

print(guests)


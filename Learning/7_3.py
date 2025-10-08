unconfirmed_users = ['Alice', 'Bob', 'Charlie']
confirmed_users=[]

# 另一种遍历列表的方式
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


pets = ['cat', 'dog', 'fish','cat','rabbit']
print(pets)
# 还可以这么访问列表吗？
while 'cat' in pets:
    pets.remove('cat')

print(pets)
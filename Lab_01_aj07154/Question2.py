def remove_user(users_data, user_name):
    #Removing Values
    for i in users_data:
        if user_name in users_data[i][1]:
            users_data[i][1].remove(user_name)
    #Removing
    for i in users_data:
        if i == user_name:
            del users_data[i]
            return

# DO NOT EDIT
users_data = {
'Alice': ('123-456-7890', ['Bob', 'Charlie']),
'Bob': ('987-654-3210', ['Alice', 'David']),
'Charlie': ('111-222-3333', ['Alice']),
'David': ('555-666-7777', ['Bob'])
}
remove_user(users_data, 'Alice')
assert users_data == {
   'Bob': ('987-654-3210', ['David']),
   'Charlie': ('111-222-3333', []),
   'David': ('555-666-7777', ['Bob'])
}

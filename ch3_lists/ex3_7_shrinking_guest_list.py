guest_list = ['boet', 'janna', 'jimmy hendrix']
message = f"Hi {guest_list[0].title()}, would you like to join for dinner?"
print(message)

message = f"Hi {guest_list[1].title()}, would you like to join for dinner?"
print(message)

message = f"Hi {guest_list[2].title()}, would you like to join for dinner?"
print(message)

print("janna can't make it")
guest_list[1] = 'anna may'

message = f"Hi {guest_list[0].title()}, would you like to join for dinner?"
print(message)

message = f"Hi {guest_list[1].title()}, would you like to join for dinner?"
print(message)

message = f"Hi {guest_list[2].title()}, would you like to join for dinner?"
print(message)


# 3.6 More guests

print("Ah, nice, we've got a bigger table!")

guest_list.insert(0, "Jaap")
print(guest_list)
guest_list.insert(2, "Pietje")
print(guest_list)
guest_list.append("Lotje")
print(guest_list)

message = f"Hi {guest_list[0].title()}, would you like to join for dinner?"
print(message)
message = f"Hi {guest_list[1].title()}, would you like to join for dinner?"
print(message)
message = f"Hi {guest_list[2].title()}, would you like to join for dinner?"
print(message)
message = f"Hi {guest_list[3].title()}, would you like to join for dinner?"
print(message)
message = f"Hi {guest_list[4].title()}, would you like to join for dinner?"
print(message)
message = f"Hi {guest_list[5].title()}, would you like to join for dinner?"
print(message)


# 3.7 Shrinking guest list

print("Oh noo, we only can invite 2 people!")

popped_guest = guest_list.pop()
message = f"Hi {popped_guest.title()}, sorry we've had to cancel you."
print(message)
popped_guest = guest_list.pop()
message = f"Hi {popped_guest.title()}, sorry we've had to cancel you."
print(message)
popped_guest = guest_list.pop()
message = f"Hi {popped_guest.title()}, sorry we've had to cancel you."
print(message)
popped_guest = guest_list.pop()
message = f"Hi {popped_guest.title()}, sorry we've had to cancel you."
print(message)

message = f"Hi {guest_list[0].title()}, you're still invited!"
print(message)
message = f"Hi {guest_list[1].title()}, you're still invited!"
print(message)

del guest_list[0]
del guest_list[0]
print(guest_list)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Creed"]
friends.extend(lucky_numbers)
friends.append("Toby")
friends.insert(1, "Kelly")
friends.remove("Kevin")
friends.pop()
lucky_numbers.sort()
lucky_numbers.reverse()

friends2 = friends.copy()
print(friends.index("Oscar"))
print(friends.count("Jim"))
print(friends2)
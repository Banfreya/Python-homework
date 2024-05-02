links = {}
while True:
    link = input()
    if not link:
        break
    person1, person2 = link.split()
    links.setdefault(person1, set()).add(person2)
    links.setdefault(person2, set()).add(person1)
friends_second_level = {}
for person in sorted(links):
    second_level_friends = set()
    for friend in links[person]:
        for friend_of_friend in links.get(friend, set()):
            if friend_of_friend != person and friend_of_friend not in links[person]:
                second_level_friends.add(friend_of_friend)
    second_level_friends -= {person} | links[person]
    friends_second_level[person] = second_level_friends
for person, second_level_friends in sorted(friends_second_level.items()):
    print(f"{person}: {', '.join(sorted(second_level_friends))}")

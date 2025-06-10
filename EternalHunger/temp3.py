from encounters import eventable


def look(e):
    return e.diff


eventable.sort(key=look)
for i in range(len(eventable)):
    print(str(i) + ":", eventable[i].name)


print(len(eventable))
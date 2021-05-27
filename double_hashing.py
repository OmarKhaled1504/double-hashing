hash_table = [None] * 13


def search(hash_table, item):
    h1 = item % 13
    h2 = (7 - item) % 13
    for i in range(len(hash_table)):
        if hash_table[(h1 + i * h2) % 13] is item:
            return (h1 + i * h2) % 13


def double_hashing(hash_table, item):
    h1 = item % 13
    h2 = (7 - item) % 13
    for i in range(len(hash_table)):
        if hash_table[(h1 + i * h2) % 13] is None:
            hash_table[(h1 + i * h2) % 13] = item
            break


double_hashing(hash_table, 18)
double_hashing(hash_table, 41)
double_hashing(hash_table, 22)
double_hashing(hash_table, 44)
item = int(input("search: "))
if not search(hash_table, item) == None:
    print("index of searched item is: {}".format(search(hash_table, item)))
else:
    print("Not Found!")
print(hash_table)

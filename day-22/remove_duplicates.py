"""
Write a function to remove duplicates from a list.
"""


def remove_duplicates(mylist: []) -> []:
    tmp_lst = []
    for i in range(len(mylist)):
        counter = 0
        for j in range(len(mylist)):
            if mylist[i] == mylist[j]:
                counter += 1
        if counter <= 1:
            tmp_lst.append(mylist[i])
    return tmp_lst


if __name__ == "__main__":
    arr = [5, 9, 4, 7, 9, 2, 3]
    print(remove_duplicates(arr))

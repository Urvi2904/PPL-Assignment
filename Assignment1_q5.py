#Find a missing page number from given page number list of a 25-page book for example : page number list is [2,4-6,12,16,17,20,21]

given = set([2, 4, 6, 12, 16, 17, 20, 21])
pages = set(range(1, 26))
print("Missing pages : ")
print(pages - given)

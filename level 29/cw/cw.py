# 1)შექმენით ფუნქცია რომელსაც გადაეცემა სია,გამოითვალეთ რიცხვების ჯამი for ციკლის საშუალებითაც და sum() ფუნქციის გამოყენებითაც აუცილებლად დააბრუნეთ შედეგი return ის გამოყენებით.

# პირველი გზა
def list(li):
    return sum(li)
print(list([1,2,3]))

#მეორე გზა
def list2(li):
    sum = 0
    for i in li:
        sum += i
    return sum
print(list([1,2,3]))
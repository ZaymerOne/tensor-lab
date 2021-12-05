"""
Проверка пароля на надежность
"""

def password_check(passwd):
    word = "password"
    val = True
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
    if all(char.isdigit() for char in passwd):
        print('Password should dont have all numeral')
        val = False
    if word.isupper() or word.islower:
        print('Password should dont have word "password"')
        val = False
    return val

passwd = (input("Enter password: "))
      
if (password_check(passwd)):
    print("Password is valid!")
else:
    print("Invalid Password!")


"""
Функция, возвращающая сумму введенных занчений
"""


def sumnum(*nums):
    try:    
        sum = 0
        for n in nums:
            sum += n
        print("Sum: ", sum)
    except:
        print("Input error! You need to enter numbers!")
        
sumnum(1, 2, 3, 5, 6)

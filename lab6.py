"""
Преобразование списка строк в байты и обратно
"""
"""
def encode(str):
    print(bytes(str[0].encode('utf-8')))
    print(bytes(str[1].encode('utf-8')))

def decode(str):
    print((str[0].decode('utf-8')))
    print((str[1].decode('utf-8')))

str = ["Привет", "Мир"]
encode(str)
str1 = [b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82', b'\xd0\x9c\xd0\xb8\xd1\x80']
decode(str1)
"""
with open('input.txt', 'w+') as f:
    f.write('hello')

    print(f)    




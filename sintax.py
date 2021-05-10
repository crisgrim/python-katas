a, b = 2, "5"

total = a + int(b)
print("The result is: " + str(total))

number = 5
print(number, type(number))

number = "5"
print(number, type(number))

x, y, z = 80, 90, "100"
print(x, type(x))
print(y, type(y))
print(z, type(z))

c = d = e = True
print(c, type(c))

print('-------------')

globalVariable = "global variable"


def change_global_variable():
    global globalVariable
    globalVariable = "global variable modified"
    # localVariable = "testing local variable"


print(globalVariable)
change_global_variable()
print(globalVariable)
# print(localVariable)

print('-------------')

print(int(10))
# print(long(10))
print(float(10))
print(complex(10))

text = "whatever"
num = 2 ** 0.5
print("The result is: %s and %.2f" % (text, num))

# %c character
# %s string
# %d int
# %f float
# %o octal
# %x hexadecimal

print('-------------')

fruits = ['coconut', 'apple', 'strawberries', 'bananas', 'melon']
print(fruits)
print(type(fruits))
print(fruits[1])
# length
print(len(fruits))
print(fruits)
# put a new element at the end
fruits.append('apple')
print(fruits)
# count times that element appears on array
print(fruits.count('apple'))
# put a new iterable element
fruits.extend('peach')
print(fruits)
# return index
print(fruits.index('apple'))
# insert an element in a position (index)
fruits.insert(1, 'pineapple')
print(fruits)

print('-------------')
# remove the last item
last = fruits.pop()
print(last)
print(fruits)
fruits.remove('apple')
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)

# append vs extend

print('-------------')

dogs = ("Chopper", "Jacky")
print(type(dogs))
print("Jacky -> ", dogs.count("Jacky"))

print('-------------')

dog = {'name': 'Chopper', 'age': 7}
print(type(dog))
print(dog)

print('-------------')

age = 19

if age < 18:
    print('You don\'t have the age needed')
elif age == 18:
    print('I need to verify your documentation')
else:
    print('Ok, you can enter')

print('-------------')

a = 0
if a and b:
    print('These variables have truth values')
else:
    print('One of these variables have false value')

print('-------------')

result, increment = 0, 1

while increment <= 10:
    result = increment + result
    increment = increment + 1
    print(increment, result)

print('The result is: ' + str(result))
print('The result is: %d' % result)

print('-------------')

sentence = 'with great power comes great responsibility'

character = iter(sentence)

next(character)
next(character)

print('-------------')


def sum(a, b):
    return a + b


print(3+3)
print(30+30)


def rest(a, b):
    return a - b


print(rest(30, 2))
print(rest(3, 3))

print('-------------')


def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print('Booom!')
    print('Function end', str(numero))


cuenta_regresiva(10)

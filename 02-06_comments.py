list_a = [1, 2, 3]

print(list_a)

list_b = [1, 2, 3,
          4, 5]

print(list_b)

list_c = [1,  # item 1
          2]

print(list_c)

tuple_a = (1,  # comment
           2  # comment
           , 3)

print(tuple_a)

dict_a = {'k_1': 'val_1'  # comment
          }
print(dict_a)


def my_function(a,  # prvi parametar
                b,  # drugi parametar
                c):  # treći parametar
    print(a, b, c)


my_function(1,  # prvi unet parametar
            2,  # Drugi unet parametar
            3)  # treći unet parametar

a = 5
b = 10
c = 20

if a > 1 \
        and b > 5 \
        and c > 10:
    print('Yeah, bebe!')

a = '''This is a 
               string!'''

print(a)

b = '''Lista:
1. jedan
dva. 2'''

print(b)
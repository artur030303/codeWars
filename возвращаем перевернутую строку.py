# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"




# def reverse_string(a):
#      my_list =  a.split(' ')
#      my_list.reverse()
#      return " ".join(my_list)
     


# print (reverse_string('This is an example!'))


def reverse_string(a):
     return ' '.join(word[::-1] for word in a.split(' '))

print (reverse_string('This is an example!'))
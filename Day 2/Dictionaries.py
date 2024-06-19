my_dict = dict()
my_dict = dict(one=1,two=2,three=3)
print(my_dict)
#from keys 
keys = ["one","two","three"]
values = 45
my_dict_new = dict.fromkeys(keys,values)
print(my_dict_new)
#get
print('getting values from dictionary : ',my_dict.get('one'))
print("clearing dictionary : ",my_dict_new.clear())

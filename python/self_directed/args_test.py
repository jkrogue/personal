def one_req_arg(one_arg):
	print(one_arg)

#Missing 1 required positional argument
#one_req_arg()

one_req_arg(1)

#Takes 1 positional argument but 2 were given
#one_req_arg(1,2)

one_req_arg(one_arg = 1)

def one_opt_arg(one_arg = "yes"):
	print(one_arg)

one_opt_arg()

#takes from 0 to 1 positional arguments but 2 were given
#one_opt_arg(1, 2)

one_opt_arg(one_arg = 2)

def var_numb_arg(one_arg = "yes", *args, **kwargs):
	print(one_arg)

	for each in args:
		print(each)

	for key in kwargs:
		print("%s: %s" % (key, kwargs[key]))

var_numb_arg()

var_numb_arg(1)

#var_numb_arg(1,2,3,4,5,6)

args = ("two", 3)

print("trying with tuple 'args'")
#var_numb_arg(1,args)
print()

print("trying with explicit dict")
var_numb_arg(1,one=1,two=2)
print()

args = {"first":"1st","second":"2nd"}
print("trying with dict 'args'")
var_numb_arg(1,**args)
print()

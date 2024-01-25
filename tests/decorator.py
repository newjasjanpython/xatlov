

import datetime


###### CLOSURE




# def my_function(b):
#     a = 5
    
#     a += b
    
#     def my_closure(d):
#         nonlocal a
#         a += d
#         return a
    
#     return my_closure, a


# my_A_func, my_A = my_function(5)
# print(my_A)
# my_A_B = my_A_func(5)

# print(my_A_B)



def decorator(function):
    function.starter_time = datetime.datetime.now()
    
    def wrapper(*args, **kwargs):
        kwargs['time_check'] = True
        kwargs['__me'] = function
        function(*args, **kwargs)
    return wrapper


@decorator
def main(*args, **kwargs):
    starter_time = "HELLO"
    print("FUNC", args, kwargs)
    print("Hello fucker")
    
    print(datetime.datetime.now() - kwargs['__me'].starter_time)



main(213123, 12313, 3121312, a=1, b=2)


'''
main()


decorator(main)
'''

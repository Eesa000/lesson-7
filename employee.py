# create class
class employee:

    # initializing
    def __init__(self):
        print('employee created')

    # calling destructor
    def __del__(self):
        print("destructor called")

def create_obj():
    print('making object...')
    obj = employee()
    print('function end...')
    return obj

print('calling create_obj() function...')
obj = create_obj()
print('program end...')
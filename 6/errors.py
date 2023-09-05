try:
    a = 10
    b = 2
    raise Exception('division by zero')
    print(a / b)
    ...
except Exception as e:
    print('Unknown error:', e)
except ZeroDivisionError as e:
    print(e)
else:
    print('Success')
finally:
    print('Work done')

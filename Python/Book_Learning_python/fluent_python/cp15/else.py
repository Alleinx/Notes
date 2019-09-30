try:
    dangerous_call()
    after_call()
except OSError:
    log('OSError')

# Better be:
# after_call() will be executed when no exception is raised during execution.
try:
    dangerous_call()
except OSError:
    log('OSerror')
else:
    after_call()


# for-else: Raise Exception if there is no 'banana' flavor.
# could be replaced with: if 'banana' not in a: raise ValueError()
for item in my_list:
    if item.flavor == 'banana':
        break
else:
    raise ValueError('No banana flavor found!')

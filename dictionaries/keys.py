# Adding keys to dictionaries

my_self = {'first_name':'allan', 'last_name':'chepkoy'}
print(my_self)

my_self['job_description'] = 'Software Developer'

print(my_self)

# Adding multiple keys

my_self.update({'first_name':'Allan', 'age':'24'})
print(my_self)

# Adding single values

my_self['age'] = '25'

print(my_self)
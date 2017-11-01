# Packing and unpacking in python

def packer(**kwargs):
    print(kwargs)

packer(name = 'allan', language = 'swahili', country = 'Kenya', tribal = None)

# Explicit definition of an argument


def packer(tribal = None, **kwargs):
    print(kwargs)

packer(name = 'allan', language = 'swahili', country = 'Kenya', tribal = False)

# Unpacking


def unpacker(first_name =None, last_name=None):
    if first_name and last_name:
        print("Hi {} {} !".format(first_name, last_name))
    else:
        print("Hi no name")

unpacker(**{"last_name":"chepkoy", "first_name": "allan"})


course_minutes = {'python basics': 232, 'django basics':237, 'flask basics':
                  189, 'java basics': 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))

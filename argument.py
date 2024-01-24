#  python3 myscript.py -o test.txt -l DEBUG -c

def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

# myfunction('hey', True, 19, 'wow', KEYONE="TEST", KEYTWO=7)

# python3 argument_parsing.py -f  text.txt -m hello\ world
    
import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)

print(opts)
print(args)


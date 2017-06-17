def do_twice ( fn, args ):
    fn(args)
    fn(args)

def print_twice (s):
    print (s)
    print (s)

def do_four ( fn, args ):
    do_twice(fn, args)
    do_twice(fn, args)

do_twice(print_twice, "spam")

def print_attributes(obj):
    for attr in vars(obj):
        print("{0}: {1}"format(attr, getattr(obj, attr)))
        
        
        
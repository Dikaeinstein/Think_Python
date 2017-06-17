class Kangaroo:
    """Represents a kangaroo."""
    
    def __init__(self, contents=None):
        """initialize the pouch contents; the default value is
        an empty list"""
        contents = contents or []
        self.pouch_contents = contents
    
    def __str__(self):
        return "{ pouch_contents: %s }" % self.pouch_contents
        
    def put_in_pouch(self, obj):
        """Add a new item to the pouch contents"""
        self.pouch_contents.append(obj)
        
        
if __name__ == "__main__":
    bad_kangaroo = Kangaroo()
    print(bad_kangaroo)
    bad_kangaroo.put_in_pouch("toda")
    bad_kangaroo.put_in_pouch("loves boxing")
    print(bad_kangaroo)
    
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('car keys')
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)
        
#!/usr/bin/env python
# Example file object used by execute_code functions
# Example comment for unit testing
class Hello(object):
    def __init__(self):
        self.msg = 'Hello, ' + 'world!'

    def out(self):
        return self.msg

world = Hello()
print world.out()

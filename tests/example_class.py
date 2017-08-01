#!/usr/bin/env python
""" Example program used by execute_code functions """
# Example comment for unit testing

# pylint: disable=too-few-public-methods
class Hello(object):
    """ Simple class to show imports """
    def __init__(self):
        self.msg = 'Hello, ' + 'world!'

    def out(self):
        """ returns Hello, world!"""
        return self.msg

if __name__ == "__main__":
    print Hello().out()

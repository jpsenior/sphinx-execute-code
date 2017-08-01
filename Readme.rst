sphinx-execute-code
===================

Sphinx-execute-code is an extension for Sphinx that allows a document author
to insert arbitrary python code samples in code blocks, or run python code
from python files on the filesystem.

This was written as an alternative to other code execution functions which
relied on doctest formats, and attempts to be more flexible, similar to
literal-block and code-block statements.

.. warning:: This module allows you to run arbitrary code, and should be treated with caution.

Options
-------
Options right now (as of version 0.2) are:

linenos
    If specified, will show line numbers
output_language
    Customizes pygments lexxer for specified language (Eg, Javascript, bash)
hide_code
    If specified, will hide the code block and only show results
hide_headers
    If specified, hides the 'Code' and 'Results' caption headers around
    the literal blocks
filename
    If specified, will load code from a file (relative to sphinx doc root)
    and ignore content.

execute_code
------------
Running 'execute_code' as a directive allows the administrator to embed exact
python code as if it was pasted in a normal code-block.

Executing python code and showing the result output::

    .. execute_code::
        :linenos:

        print 'python highlight code'

        class Foo(object):
            def __init__(self):
                self.bar = 'baz'
            def out(self):
                print self.bar

        f = Foo()
        f.out()

Output language
---------------
Customizing the output syntax can be helpful to make it easy to document
any other pygments lexxer - eg ini, javascript

We can customize the output language parser (for JSON/Javascript)::

    .. execute_code::
        :output_language: javascript

        print "'{foo-bar-baz}'"

Hiding code
-----------
You may want to hide the example code that is executing
(avoiding highlighting/etc) and display the results only.

We can also hide the code input, showing only the executed code results::

    .. execute_code::
        :hide_code:

        print 'This should not print the example code'

Suppressing output headers
--------------------------
Suppressing the 'Headers' outputs for Code and Results header::

    .. execute_code::
       :hide_headers:

       foo = 32
       print 'This will hide the Code and Results text - and foo is %d' % foo

Executing python code from a file
---------------------------------
execute_code also allows you to import a python file and execute
it within a document.

Running a Python file from filename from the .py example::

    .. execute_code::
       :filename: tests/example_class.py

This function also supports the argument 'hide_filename'::

    .. execute_code::
       :filename: tests/example_class.py
       :hide_filename:

Installation
============

Installation from source::

    $ git clone git@github.com:jpsenior/sphinx-execute-code.git
    $ python setup.py install

Installation from pypi::

    $ pip install sphinx-execute-code

Activating on Sphinx
====================

To activate the extension, add it to your extensions variable in conf.py
for your project.

Activating the extension in sphinx::

    extensions.append('sphinx_execute_code')

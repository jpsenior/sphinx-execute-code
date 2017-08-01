"""

    test_execute_code
    =================

    Tests the execute_code directive

    :copyright: Copyright 2017, JP Senior <jp.senior@gmail.com>
    :license: MIT

"""
import json
from textwrap import dedent
import pytest
from sphinx_execute_code import ExecuteCode
from tests.example_class import Hello




def test_execute_code_function():
    """ Ensure simple code functions execute """
    code = dedent('''
    print "foo"
    print "bar"
    ''')

    expected_output = dedent('''\
    foo
    bar
    ''')
    results = ExecuteCode.execute_code(code)

    assert expected_output == results

def test_execute_and_import():
    """ Import a generic module, make sure we do not get any type errors """
    code = dedent('''
    import os
    print os.path
    ''')
    results = ExecuteCode.execute_code(code)

    assert results != None
    assert results != ''

def test_execute_empty():
    """ execute_code function should be able to take empty content """
    code = ''
    results = ExecuteCode.execute_code(code)
    assert results == ''

def test_execute_code_sample():
    """ Just makes sure the sample code output of this sample works as expected """
    hello = Hello()
    assert hello.out() == 'Hello, world!'


# sphinx tests
# pylint: disable=unused-argument
@pytest.mark.sphinx('text', testroot='ext-execute-code', freshenv=True,
                    confoverrides={})
def test_sphinx_execute_code(app, status, warning):
    """ Runs a sphinx 'text' renderer and uses roots/test-ext-execute-code/index.rst
        to perform specific code rendering unit tests
    """
    app.builder.build_all()

    if app.statuscode != 0:
        assert False, 'Failures in execute_code: ' + status.getvalue()
    content = (app.outdir / 'index.txt').text()

    # Make sure the module is loaded
    assert 'sphinx_execute_code' in app.extensions

    # Ensure sample_1 executes
    assert 'execute_code:sample_1' in content

    # Ensure linenos argument is accepted
    assert 'execute_code_linenos:sample_2' in content

    # Ensure that we can format output language properly
    data = {'execute_code': 'sample_3', 'output_language': 'javascript', 'sample3': True}

    assert json.dumps(data) in content
    assert 'Hello, world!' in content
    assert 'Example comment for unit testing' in content

    # Ensure :hidecode: works to hide example code
    assert '#execute_code_sample_5_comment_is_hidden' not in content
    assert 'execute_code_should_not_run' not in content

    # Ensure :hidecode: works
    assert 'execute_code_hide_code:sample_6' in content
    assert 'This comment is hidden' not in content

    # Ensure headers render
    results_header = dedent('''\
    Results
    
       execute_code_show_header:sample_7
    ''')

    assert results_header in content

    results_header = dedent('''\
    Results

       execute_code_hide_header:sample_8
    ''')

    # Ensure filename is hidden with :hide_filename:
    assert results_header not in content

    assert 'execute_code_hide_filename:sample_9' in content
    assert 'hidden_filename' not in content

"""

    test_execute_code
    =================

    Tests the execute_code directive

    :copyright: Copyright 2017, JP Senior <jp.senior@gmail.com>
    :license: MIT

"""
from sphinx_execute_code import ExecuteCode
from textwrap import dedent
from example_class import Hello
import pytest
from sphinx.testing.util import etree_parse
import json


def test_execute_code_function():
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

def test_execute_with_import_function_does_not_raise_error():
    code = dedent('''
    import os
    print os.path
    ''')
    results = ExecuteCode.execute_code(code)

    assert None != results
    assert '' != results

def test_execute_code_with_empty_codeblock_returns_nothing():
    code = ''
    results = ExecuteCode.execute_code(code)
    assert '' == results

def test_execute_code_sample():
    """ Just makes sure the sample code output of this works as expected """
    hello = Hello()
    assert 'Hello, world!' == hello.out()


# sphinx tests
@pytest.mark.sphinx('text', testroot='ext-execute-code', freshenv=True,
                    confoverrides={})
def test_sphinx_execute_code(app, status, warning):
    print app, status, warning
    #app.builder.build(['only'])
    #doctree = app.env.get_doctree('only')
    app.builder.build_all()

    if app.statuscode != 0:
        assert False, 'Failures in execute_code: ' + status.getvalue()
    content = (app.outdir / 'index.txt').text()

    assert 'sphinx_execute_code' in app.extensions

    assert 'execute_code:sample_1' in content

    assert 'execute_code_linenos:sample_2' in content

    data = {'execute_code': 'sample_3', 'output_language': 'javascript', 'sample3': True}

    assert json.dumps(data) in content
    assert 'Hello, world!' in content
    assert 'Example comment for unit testing' in content

    assert '#execute_code_sample_5_comment_is_hidden' not in content
    assert 'execute_code_should_not_run' not in content

    assert 'execute_code_hide_code:sample_6' in content
    assert 'This comment is hidden' not in content

    results_header = dedent('''\
    Results
    
       execute_code_show_header:sample_7
    ''')

    assert results_header in content

    results_header = dedent('''\
    Results

       execute_code_hide_header:sample_8
    ''')

    assert results_header not in content
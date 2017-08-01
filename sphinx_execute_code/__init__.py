from docutils.parsers.rst import Directive, directives
from docutils import nodes
import sys
import StringIO
import os

# execute_code function thanks to Stackoverflow code post from hekevintran
# https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python

__author__ = 'jp.senior@gmail.com'
__docformat__ = 'restructuredtext'
__version__ = '0.2a1'





class ExecuteCode(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 5

    option_spec = {
        'linenos': directives.flag,
        'output_language': directives.unchanged,  # Runs specified pygments lexer on output data
        'hide_code': directives.flag,
        'hide_headers': directives.flag,
        'filename': directives.path,
    }

    @classmethod
    def execute_code(cls, code):
        """ Executes supplied code as pure python and returns a list of stdout, stderr

        Args:
            code (string): Python code to execute

        Results:
            (list): stdout, stderr of executed python code

        Raises:
            ExecutionError when supplied python is incorrect

        Examples:
            >>> execute_code('print "foobar"')
            'foobar'
        """

        output = StringIO.StringIO()
        err = StringIO.StringIO()

        sys.stdout = output
        sys.stderr = err

        try:
            exec code
        # If the code is invalid, just skip the block - any actual code errors
        # will be raised properly
        except TypeError:
            pass
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        results = list()
        results.append(output.getvalue())
        results.append(err.getvalue())
        results = ''.join(results)

        return results

    def run(self):
        """ Executes python code for an RST document, taking input from content or from a filename

        :return:
        """
        language = self.options.get('language') or 'python'
        linenos = 'linenos' in self.options
        output_language = self.options.get('output_language') or 'none'
        hide_code = 'hide_code' in self.options
        hide_headers = 'hide_headers' in self.options
        filename = self.options.get('filename')
        code = ''

        if not filename:
            code = '\n'.join(self.content)
        if filename:
            try:
                with open(filename, 'r') as f:
                    code = f.read()
                    self.warning('code is %s' % code)
            except (IOError, OSError) as e:
                # Raise warning instead of a code block
                error = 'Error opening file: %s, working folder: %s' % (e, os.getcwd())
                self.warning(error)
                return [nodes.warning(error, error)]

        output = []

        # Show the example code
        if not hide_code:
            input_code = nodes.literal_block(code, code)

            input_code['language'] = language
            input_code['linenos'] = linenos
            if not hide_headers:
                output.append(nodes.caption(text='Code %s' % filename or ''))
            output.append(input_code)

        # Show the code results
        if not hide_headers:
            output.append(nodes.caption(text='Results'))
        code_results = self.execute_code(code)
        code_results = nodes.literal_block(code_results, code_results)

        code_results['linenos'] = linenos
        code_results['language'] = output_language
        output.append(code_results)
        return output

def setup(app):
    app.add_directive('execute_code', ExecuteCode)
    return {'version': __version__}

tests
=====

This is a test

.. execute_code::

    print 'execute_code:' + 'sample_1'

.. execute_code::
   :linenos:

   print 'execute_code_linenos:' + 'sample_2'

.. execute_code::
   :output_language: javascript

   data = {'execute_code': 'sample_3', 'output_language': 'javascript', 'sample3': True}
   import json
   print json.dumps(data)

.. sample_4:

.. execute_code::
   :filename: tests/example_class.py

.. execute_code::
   :filename: tests/example_class.py

   print 'execute_code_should_not_run:' + 'sample_5'
   #execute_code_sample_5_comment_is_hidden

.. execute_code::
   :hide_code:

   print 'execute_code_hide_code:sample_6'
   # This comment is hidden


.. execute_code::

   print 'execute_code_show_header:' + 'sample_7'

.. execute_code::
   :hide_headers:

   print 'execute_code_hide_header:' + 'sample_8'
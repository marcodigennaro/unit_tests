'''
Free up resources by defining setup_*
and teardown_* modules
'''

from student_class import StudentDB

db=None

def setup_module(module):
    print('------- setup_module -------')
    global db
    db = StudentDB()
    db.connect('data.json')

def teardown_module(module):
    print('------- teardown_module -------')
    db.close()

def test_scott_data():
     scott_data = db.get_data('Scott')
     assert scott_data['id'] == 1
     assert scott_data['name'] == 'Scott'
     assert scott_data['result'] == 'pass'

def test_mark_data():
     mark_data = db.get_data('Mark')
     assert mark_data['id'] == 2
     assert mark_data['name'] == 'Mark'
     assert mark_data['result'] == 'fail'

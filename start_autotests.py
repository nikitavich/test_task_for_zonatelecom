import os


def cons_read(test):
    a = os.popen(
        f'python -m pytest --no-header -q --tb=line --disable-warnings tests/test_yandex.py::TestYandex::{test}')
    res = a.read()
    a.close()
    return res


def start_autotests():
    result1 = ''
    tests = ['test_input_field',
             'test_enter_button',
             'test_check_validation',
             'test_success_auth',
             'test_check_password_error']
    for test in tests:
        result = cons_read(test)
        if 'passed' in result:
            result1 = result1 + test + ': passed' + '\n'
        if 'FAILED' in result:
            result1 = result1 + test + ': failed' + '\n'
        if 'ERROR' in result:
            result1 = result1 + test + ': ERROR' + '\n'
    print(result1)
    with open('file.txt', 'w') as file:
        file.write(result1)

start_autotests()
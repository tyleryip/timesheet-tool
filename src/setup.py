from setuptools import setup

setup(
    name='timesheet',
    version='0.1.0',
    py_modules=['main', 'parse'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'timesheet = timesheet:cli',
        ],
    },
)
from setuptools import setup

setup(
    name='propofol_study_tools',
    version='0.2',
    py_modules=['pat_data_entry', propofol_data_setup'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pat_data_entry=pat_data_entry.py:entry,
        pat_csv_init=propofol_data_setup.py:go
    ''',
)
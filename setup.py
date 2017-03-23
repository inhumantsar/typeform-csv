from setuptools import setup

setup(
    name='task1',
    author='Shaun Martin',
    author_email='shaun@samsite.ca',
    version='1.0.0',
    description='Task 1 - Dump CSV from Typeform',
    url='https://github.com/inhumantsar/somerepo',
    install_requires=open('requirements.txt', 'r').readlines(),
    packages=['task1'],
    entry_points={
        'console_scripts': [
            'task1 = task1.cli:run'
        ]
    }
)

from setuptools import setup

setup(
    name='jsonformat',
    version='1.0',
    packages=['scripts'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        jsonformat=jsonformat.formatter:format
    ''',
)

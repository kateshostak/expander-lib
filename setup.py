from setuptools import setup

setup(
    name='expandergraphs',
    version='1.2',
    description='Implementation of several expander construction algorithms',
    url='http://github.com/',
    author='Kate Shostak',
    author_email='katherine.shostak@gmail.com',
    license='MIT',
    packages=[
        'expanders', 
        'graphs',
        'expansion_constant',
    ],
    zip_safe=False
)

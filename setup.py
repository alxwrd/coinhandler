from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='coinhandler',
    packages=['coinhandler'],
    version='0.3',
    description='A Python module to handle interacting with coins',
    author='Alex Ward',
    author_email='alxwrd@googlemail.com',
    url='https://github.com/alxwrd/coins',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
    license='MIT',
    python_requires='>=3.6',
    project_urls={
        'Source': 'https://github.com/alxwrd/coinhandler',
        'Bug Reports':  'https://github.com/alxwrd/coinhandler/issues',
    }
)

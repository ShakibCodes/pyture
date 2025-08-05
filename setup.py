from setuptools import setup, find_packages

setup(
    name='pyture',
    version='0.1.0',
    author='Shakib Sayyed',
    author_email='shakibonit@gmail.com',
    description='A simple and powerful Python tool to capture variables, prints, outputs, and more — effortlessly.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ShakibCodes/pyture',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Debuggers',
    ],
    python_requires='>=3.7',
)

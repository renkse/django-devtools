import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-devtools',
    version='0.1',
    packages=['devtools'],
    include_package_data=True,
    license='BSD License',
    description='A Django package which contains a set of useful utils for web development',
    long_description=README,
    url='https://github.com/renkse/django-devtools',
    download_url='https://github.com/renkse/django-devtools/tarball/0.1',
    author='renkse',
    author_email='solomon_art@mail.ru',
    classifiers=[
	'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)


from setuptools import setup, find_packages

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']


setup(name='S-R-P',
      version='0.1.0',
      author='Mohsen',
      author_email='mohsen000069@gmail.com',
      description='simple app to play with and learn.',
      install_requires=[
          'Adafruit-GPIO>=0.7',
          'psycopg2',
          'Adafruit-PureIO',
          'Flask',
          'Flask-API',
          'Flask-Cors',
          'Flask-SQLAlchemy',
          'SQLAlchemy'
      ],
      entry_points={
          'console_scripts': ['srp = server.py']
      },
      packages=find_packages())

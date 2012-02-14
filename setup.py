from setuptools import setup

setup(
    name = 'exc',
    version = '0.91',
    packages = ['exc'],
    
    # Metadata
    author = 'Olivier Breuleux',
    author_email = 'olivier@breuleux.net',
    url = 'https://github.com/breuleux/exc',
    download_url = 'https://github.com/downloads/breuleux/exc/exc.tar.gz',
    license = 'BSD',

    description = 'Easy on-the-fly exception subclassing.',
    long_description = (
        'Provides exception classes which can be subclassed'
        ' with [] notation, allowing developers to easily'
        ' raise a different exception on every raising site.'),

    keywords = 'exceptions',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Topic :: Utilities',
    ],
)

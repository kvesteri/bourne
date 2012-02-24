try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='sqlalchemy-serializers',
    version='0.1.0',
    description='Serializers for SqlAlchemy',
    long_description=__doc__,
    author='Konsta Vesterinen',
    author_email='konsta.vesterinen@gmail.com',
    url='http://github.com/kvesteri/sqlalchemy-serializers',
    packages=['flask_generic_views'],
    include_package_data=True,
    license='BSD',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'setuptools',
        'Flask',
        'Flask-SQLAlchemy'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
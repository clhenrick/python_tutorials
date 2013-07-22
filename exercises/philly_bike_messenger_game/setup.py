try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Philly Bike Messenger interactive text game',
    'author': 'Chris Henrick',
    'url': 'github.ocm/https://github.com/cups49/python_tutorials',
    'download_url': 'https://github.com/cups49/python_tutorials',
    'author_email': 'chrishenrick@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [philly_bicycle_messenger],
    'scripts': [],
    'name': 'Philly Bike Messenger beta'
}

setup(**config)

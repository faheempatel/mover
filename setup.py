try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A tool to help move/copy RAW files',
 	'author': 'Faheem Patel',
	'url': 'URL to get it at.',
	'download_url': 'https://github.com/faheempatel/mover',
	'author_email': 'faheem@faheempatel.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['mover'],
	'scripts': [],
	'name': 'mover'
}

setup(**config)

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A tool to help move/copy RW2 files',
 	'author': 'Faheem Patel',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'faheem@faheempatel.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['mover'],
	'scripts': [],
	'name': 'mover'
}

setup(**config)

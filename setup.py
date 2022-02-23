import setuptools

with open('README.md','r') as file:
	long_desciption = file.read()


setuptools.setup(
	name = 'preprocess_nitishraj37',   # this should be unique
	version = '0.0.4',
	author = 'Nitish Raj',
	author_email = 'nitish.raj37@gmail.com',
	description = 'This is preprocessing package',
	long_desciption = 'long_desciption',
	long_desciption_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)
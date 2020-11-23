import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_hscode', # harus unik biar ga konflik
	version = '0.0.1',
	author = 'Lazuardi Zulfikar Wicaksana',
	author_email = 'lzulfikarw@gmail.com',
	description = 'This is preprocessing package for HS Code Goos Description',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)
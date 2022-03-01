from setuptools import setup
setup(name='yo'
      version='1.0'
      description='Module for backdoor design and implementation.',
      author='Ethelom'
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
	  )

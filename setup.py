from setuptools import setup, find_packages

setup(name='check',
      version='1.0',
      description='Python Distribution Utilities',
      author='ramanaidu alla',
      author_email='alla.ramanaidu',
      url='https://github.com/allaramanaidu/',
      packages=find_packages(),
      data_files=[('/var/task', ['config.ini'])],
      )

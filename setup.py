from setuptools import setup
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'automation-report',
  packages = ['automation_report'],
  version = '1.0.3',
  license='MIT',
  description = 'Simple report for your test automation including various cases/steps specifying its valid status.',
  author = 'Bibek Adhikari',
  author_email = 'bbekad94@gmail.com',
  url = 'https://github.com/bibekad123/automation-report',
  download_url = 'https://github.com/bibekad123/automation-report/archive/1.0.3.tar.gz',
  keywords = ['automation report', 'report', 'automation'],  
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Testing',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
  include_package_data=True,
  long_description=long_description,
  long_description_content_type='text/markdown'
)
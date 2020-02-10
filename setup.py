from setuptools import setup
setup(
  name = 'automation-report',
  packages = ['automation-report'],
  version = '0.0.4',
  license='MIT',
  description = 'Simple report for your test automation including various cases/steps specifying its valid status.',
  author = 'Bibek Adhikari',
  author_email = 'bbekad94@gmail.com',
  url = 'https://github.com/bibekad123/automation-report',
  download_url = 'https://github.com/bibekad123/automation-report/archive/0.0.4.tar.gz',
  keywords = ['automation report', 'report', 'automation'],  
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
  include_package_data=True,
)
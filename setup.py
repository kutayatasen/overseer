from setuptools import setup

version = '0.1'

setup(name='overseer',
      version=version,
      description="Data tools for data engineers",
      long_description=open("./README.md", "r").read(),
      author='Kutay Ata Şen',
      author_email='kutayatasen@gmail.com',
      url='https://github.com/kutayatasen/overseer',
      license='MIT Software License',
      packages=['psycopg2'],
      include_package_data=True,
      zip_safe=True,
      )
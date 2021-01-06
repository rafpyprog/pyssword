from pathlib import Path
from setuptools import setup


setup(name='getpwd',
      version='0.1.0',
      description='Python tool to get a password from the user and display a masked value at the prompt.',
      long_description= (Path(__file__).parent / 'README.md').read_text(),
      long_description_content_type='text/markdown',
      keywords='getch password mask',
      url='https://github.com/rafpyprog/pyssword',
      author='Rafael Alves Ribeiro',
      author_email='rafael.alves.ribeiro@gmail.com',
      license='MIT',
      packages=['getpwd'],
      install_requires=[
          'readchar==2.0.1',
      ],
      python_requires='>=3.4',
      )
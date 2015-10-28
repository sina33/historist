from setuptools import setup

setup(name='historist',
      version='0.1.0.dev1',
      description='activity logger',
      url='http://github.com/sina33/historist',
      author='Sina Saeedi',
      author_email='sina.saeedi@outlook.com',
      license='MIT',
      packages=['historist'],
      entry_points={
        "console_scripts": [
            "historist = historist:hi",
        ]
      },
      zip_safe=False)

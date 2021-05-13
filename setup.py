from setuptools import setup, find_packages
setup(name="jobkiller",
      py_modules=["jobkiller"], packages=find_packages())

packages=(
            'jobkiller',
            'jobkiller.indeed',
            'jobkiller.models'
        )

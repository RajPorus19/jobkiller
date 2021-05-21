from setuptools import setup, find_packages
setup(name="jobscrapper",
      py_modules=["jobscrapper"], packages=find_packages())

packages=(
            'jobscrapper',
            'jobscrapper.indeed',
            'jobscrapper.models'
        )

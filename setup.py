from setuptools import setup, find_packages
setup(name="jobscraper",
      py_modules=["jobscraper"], packages=find_packages())

packages=(
            'jobscraper',
            'jobscraper.indeed',
            'jobscraper.models'
        )

import unittest
from jobscraper.indeed.indeed_job_list import IndeedJobList

class IndeedJobListTest(unittest.TestCase):

    def test_scrape_indeed_job_list_up_to_3(self):
        for i in range(1,4):
            indeed_list = IndeedJobList("test","Ile-de-France",i)
            jobs = indeed_list.get_jobs()
            self.assertEqual(i, len(jobs))

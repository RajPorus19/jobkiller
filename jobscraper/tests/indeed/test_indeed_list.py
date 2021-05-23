import unittest
import random
from jobscraper.indeed.indeed_job_list import IndeedJobList

class IndeedJobListTest(unittest.TestCase):

    def test_scrape_indeed_job_list_up_to_3(self):
        for i in range(1,4):
            indeed_list = IndeedJobList("test","Ile-de-France",i)
            jobs = indeed_list.get_jobs()
            self.assertEqual(i, len(jobs))


    def test_indeed_job_json_to_job_object(self):
        indeed_list = IndeedJobList("Informatique","Ile-de-France",10)
        jobs = indeed_list.get_jobs()
        randomJobNum = random.randint(0,9)
        randomJobJson = jobs[2]
        jobDetail = indeed_list.getIndeedJobDetailFromJson(randomJobJson)
        jobObject = jobDetail.get_job_object()
        self.assertNotEqual(jobObject.jobDesc,None)

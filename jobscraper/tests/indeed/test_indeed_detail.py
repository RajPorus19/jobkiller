import unittest
from jobscraper.indeed.indeed_job_detail import IndeedJobDetail

class IndeedJobDetailTest(unittest.TestCase):

    def test_job_description_not_empty(self):
        url = "https://fr.indeed.com/voir-emploi?q=R&D+Vision&t=D%C3%A9veloppeurs(ses)+informatique&jk=3fc9219d69b065f4"
        indeedJobDetail = IndeedJobDetail("id",url,"sfr","dev")
        jobObject = indeedJobDetail.get_job_object()
        jobDesc = jobObject.jobDesc
        empty_string = ""
        self.assertNotEqual(jobDesc,empty_string)


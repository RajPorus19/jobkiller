import unittest
from jobscrapper.indeed.indeed_job_detail import IndeedJobDetail

class IndeedJobDetailTest(unittest.TestCase):

    def test_job_details_not_empty(self):
        url = "https://fr.indeed.com/voir-emploi?q=R&D+Vision&t=D%C3%A9veloppeurs(ses)+informatique&jk=3fc9219d69b065f4"
        indeedJobDetail = IndeedJobDetail(url)
        jobObject = indeedJobDetail.get_job_object()
        empty_string = ""
        print(jobObject.status)
        self.assertEqual("",empty_string)


import unittest
from jobkiller.indeed.indeed_job_detail import fetchIndeedJobDetailJson

class IndeedJobDetailTest(unittest.TestCase):

    def test_job_details_not_empty(self):
        url = "https://fr.indeed.com/voir-emploi?q=R&D+Vision&t=D%C3%A9veloppeurs(ses)+informatique&jk=3fc9219d69b065f4"
        result = fetchIndeedJobDetailJson(url)
        empty_string = ""
        for field in result:
            self.assertNotEqual(result[field],empty_string)


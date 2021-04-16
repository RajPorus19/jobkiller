class Job:
    def __init__(self, jobTitle, companyName, datePublished, status, jobUrl, recruiterEmail):
        self.jobTitle = jobTitle
        self.companyName = companyName
        self.datePublished = datePublished
        self.dateApplied = None
        self.status = status
        self.jobUrl = jobUrl
        self.recruiterEmail = recruiterEmail

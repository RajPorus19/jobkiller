class Job:
    def __init__(self, id, jobTitle, companyName, jobDesc, datePublished, status, jobUrl, recruiterEmail):
        self.id = id
        self.jobTitle = jobTitle
        self.companyName = companyName
        self.jobDesc = jobDesc
        self.datePublished = datePublished
        self.dateApplied = None
        self.status = status
        self.jobUrl = jobUrl
        self.recruiterEmail = recruiterEmail


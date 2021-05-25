import gi
from jobscraper.indeed.indeed_job_list import IndeedJobList

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Main(Gtk.Window):
    def __init__(self):

        Gtk.Window.__init__(self,title="Jobscraper")

        self.indeedList = IndeedJobList("Informatique","Paris",10)
        self.jobs = self.indeedList.get_jobs()

        self.box = Gtk.Box(spacing=6,orientation="vertical")
        self.add(self.box)

        self.greetings = Gtk.Label()
        self.greetings.set_markup("<b>Welcome to Jobscrapper</b>")
        self.box.pack_start(self.greetings, True, True, 0)

        self.listView = Gtk.ListBox()
        for job in self.jobs:
            self.listView.add(ListBoxRowWithData(job))
        self.listView.connect("row-activated",self.show_job)
        self.box.pack_start(self.listView, True, True, 0)

        self.backButton = Gtk.Button.new_with_label("Go back")
        self.backButton.connect("clicked",self.show_list)
        self.box.pack_start(self.backButton, True, True, 0)


    def show_job(self,widget,data):
        self.backButton.show()
        self.listView.hide()
        self.jobDescLabel = Gtk.Label()
        jobDetail = self.indeedList.getIndeedJobDetailFromJson(data.data)
        job = jobDetail.get_job_object()
        self.jobDescLabel.set_markup("<b>"+job.jobDesc+"</b>")
        self.box.pack_start(self.jobDescLabel, True, True, 0)
        self.jobDescLabel.show()
    def show_list(self,widget):
        self.backButton.hide()
        self.jobDescLabel.hide()
        self.listView.show()


class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self,data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.listViewString = data["cmp"] + ": " + data["title"]
        self.label = Gtk.Label(label=self.listViewString)
        #self.label.connect("row-activated",self.print_data)
        self.add(self.label)

    def print_data(self,widget):
        print(self.data)

win = Main()
win.connect("destroy",Gtk.main_quit)
win.show_all()
Gtk.main()


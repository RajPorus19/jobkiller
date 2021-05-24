import gi
from jobscraper.indeed.indeed_job_list import IndeedJobList

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Main(Gtk.Window):
    def __init__(self):

        Gtk.Window.__init__(self,title="Jobscraper")

        self.jobs = IndeedJobList("Informatique","Paris",50).get_jobs()

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.debugButton = Gtk.Button(label="Debug")
        self.debugButton.connect("clicked",self.print_debug)
        self.box.pack_start(self.debugButton, True, True, 0)

        self.greetings = Gtk.Label(label="Welcome to Jobscraper")
        self.box.pack_start(self.greetings, True, True, 0)

        self.listView = Gtk.ListBox()
        for job in self.jobs:
            self.listView.add(ListBoxRowWithData(job))
        self.listView.connect("row-activated",self.print_debug)
        self.box.pack_start(self.listView, True, True, 0)

    def print_debug(self,widget,data):
        print(data.listViewString)


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


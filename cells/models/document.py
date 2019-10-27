from cells.observer import Observer
from cells import events


class Document(Observer):
    def __init__(self, subject):
        super().__init__(subject)

        self.add_responder(events.file.Open, self.open_responder)

    def save_responder(self, e):
        self.save()

    def save(self):
        pass

    def open_responder(self, e):
        self.notify(events.document.Load(self))
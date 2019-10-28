from rx import operators as op


class Observation:
    def __init__(self, subject):
        self.subject = subject
        self.number = 0

    def add_responder(self, event_type, responder):
        self.subject.pipe(
            op.filter(lambda e: isinstance(e, event_type))
        ).subscribe(responder)

    def notify(self, event):
        self.subject.on_next(event)
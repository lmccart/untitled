import urllib2

class Http(object):
  def __init__(self):
    self.running = False;
    self.registered_events = [];

  def start(self):
    self.running = True;

  def stop(self):
    self.running = False;

  def register(self, event):
  	return;

  def fire(self, event, args):
  	return;

  def do_input(self, event, args):
  	return;
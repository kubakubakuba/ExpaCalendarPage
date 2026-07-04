class Config:
	def __init__(self):
		self.calendar_link = '3fo3jbnh8fq15h3g59uakeiv6s@group.calendar.google.com'
		self.calendar_shortlink = 'http://goo.gl/WCkXKv'
		self.output_folder = 'programy2026'
		self.name = 'Astronomická expedice'
		self.start_date = '2026;07;02'
		self.end_date = '2026;07;20'
		self.qr_size = 40
		self.lang = 'cz'
		self.rick_probability = 5
		self.lat = 49.971980
		self.lng = 16.271130
		self.tmz = 'Europe/Prague'
		self.min_elevation = 10
		self.satellite_names = ['NOAA 15', 'NOAA 18', 'NOAA 19', 'METEOR-M 2', 'ISS (ZARYA)']
		self.timezone = 'Europe/Prague'

from ExpaCalendar import ExpaCalendar as ec

calendar = ec(Config())

events = calendar.get_calendar_events()

calendar.generate_pdf(events)
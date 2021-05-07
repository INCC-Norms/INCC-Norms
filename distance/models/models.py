# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from math import sin, cos, sqrt, atan2, radians

class partner(models.Model):
	_inherit = 'res.partner'

	distance = fields.Float(string='Distance', compute='distance_km')
	def distance_km(self):
		# approximate radius of earth in km
		R = 6373.0
		lat1 = radians(48.73681)
		lon1 = radians(2.44753)
		lat2 = radians(self.partner_latitude)
		lon2 = radians(self.partner_longitude)

		dlon = lon2 - lon1
		dlat = lat2 - lat1

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))

		distances = R * c

		self.distance = distances


# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from math import sin, cos, sqrt, atan2, radians
from odoo import models, fields, api, _
import qrcode
import base64
from io import BytesIO

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
		
class Rapport(models.Model):
	_inherit = "x_rapport"
	qr_code = fields.Binary("QR Code", attachment=True, store=True)
	@api.onchange('x_studio_partner_id')
	def generate_qr_code(self):
		qr = qrcode.QRCode(
		    version=1,
		    error_correction=qrcode.constants.ERROR_CORRECT_L,
		    box_size=20,
		    border=8,
		)
		qr.add_data(self.x_name)
		qr.make(fit=True)
		img = qr.make_image()
		temp = BytesIO()
		img.save(temp, format="PNG")
		qr_image = base64.b64encode(temp.getvalue())
		self.qr_code = qr_image


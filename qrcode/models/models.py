# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import qrcode
import base64
from io import BytesIO
		
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
		donnees = self.x_name + self.x_studio_partner_id.name
		qr.add_data(donnees)
		qr.make(fit=True)
		img = qr.make_image()
		temp = BytesIO()
		img.save(temp, format="PNG")
		qr_image = base64.b64encode(temp.getvalue())
		self.qr_code = qr_image
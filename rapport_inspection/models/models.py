# -*- coding: utf-8 -*-
import qrcode
import base64
from io import BytesIO
from odoo import models, fields, api

class Rapport(models.Model):
	_name = 'rapport.inspection'
	qr_code = fields.Binary("QR Code", attachment=True, store=True)
	client_id = fields.Many2one('res.partner', )
	
	#api.onchange('client_id')
	def generate_qr_code(self):
		rec = self.env['x_rapport'].search([])
		for r in rec:
			ident = str(r.id).replace('NewId_', '')
			base_url = 'https://incc-norms-incc-norms.odoo.com'
			base_url += '/web#id='+ident+'&view_type=form&model=x_rapport'

			qr = qrcode.QRCode(
			    version=1,
			    error_correction=qrcode.constants.ERROR_CORRECT_L,
			    box_size=10,
			    border=4,
			)
			qr.add_data(base_url)
			qr.make(fit=True)
			img = qr.make_image()
			temp = BytesIO()
			img.save(temp, format="PNG")
			qr_image = base64.b64encode(temp.getvalue())
			r.x_qr_code = qr_image

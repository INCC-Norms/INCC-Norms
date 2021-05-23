# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import qrcode
import base64
from io import BytesIO

class Rapport(models.Model):
	_inherit = 'x_rapport'
	@api.onchange('x_studio_partner_id')
	def generate_qr_code(self):
		base_url = self.env['ir.config_parameter'].get_param('web.base.url')
		iden = str(self.id).replace('NewId_', '')
		base_url += '/web#id='+iden+'&view_type=form&model=product.template'

		qr = qrcode.QRCode(
		    version=1,
		    error_correction=qrcode.constants.ERROR_CORRECT_L,
		    box_size=10,
		    border=4,
		)
		qr.add_data('test')
		qr.make(fit=True)
		img = qr.make_image()
		temp = BytesIO()
		img.save(temp, format="PNG")
		qr_image = base64.b64encode(temp.getvalue())
		self.x_qr_code = qr_image

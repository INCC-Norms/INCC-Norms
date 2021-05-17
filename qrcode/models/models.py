# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import qrcode
import base64
from io import BytesIO
		
class Rapport(models.Model):
	_inherit = "sale.order"
	

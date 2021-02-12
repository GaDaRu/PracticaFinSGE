#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Lugar(models.Model):
	_name = 'lugar.dato'
	pais = fields.Text('Pais', required = True)
	provincia = fields.Text('Provincia', required = True)
	municipio = fields.Text('Municipio')
	calle = fields.Text('Calle')
	fecha = fields.Date('Fecha')

	def name_get(self):
		res=[]
		for record in self:
			muni = record.municipio
			res.append((record.id, muni))
		return res
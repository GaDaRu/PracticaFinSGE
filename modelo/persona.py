#-*- coding: utf-8 -*-

from odoo import models, fields, api

class persona(models.Model):
	_name = 'persona.dato'
	nombre = fields.Text('Nombre', required = True)
	apellido = fields.Text('Apellido', required = True)
	dni = fields.Text('dni')
	edad = fields.Date('edad')

	def name_get(self):
		res=[]
		for record in self:
			nom = record.nombre
			res.append((record.id, nom))
		return res
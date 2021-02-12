#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Producto(models.Model):
	_name = 'producto.dato'
	codigo = fields.Integer('Codigo', required = True)
	nombre = fields.Text('Nombre', required = True)
	foto = fields.Binary('Imagen', Help='Seleccionar imagen')
	marca = fields.Text('Marca')
	precio = fields.Char('Precio', size=20)
	tamano = fields.Text('Tamaño')

	def name_get(self):
		res=[]
		for record in self:
			produc = record.nombre
			res.append((record.id, produc))
		return res
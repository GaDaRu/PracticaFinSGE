#-*- coding: utf-8 -*-

from odoo import models, fields, api

class subasta(models.Model):
	_name = 'subasta.dato'
	producto = fields.Many2one('producto.dato', 'Producto')
	precioCom = fields.Char('Precio Alcanzado', size=20)
	vendedor = fields.Many2one('persona.dato', 'Vendedor')
	comprador = fields.Many2one('persona.dato', 'Comprador')
	subastador = fields.Many2one('persona.dato', 'Subastador')
	lugar = fields.Many2one('lugar.dato', 'Lugar')

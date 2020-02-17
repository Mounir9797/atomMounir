# -*- coding: utf-8 -*-

from odoo import models, fields, api

class instituto_alumno(models.Model):
    _name = 'instituto.alumno'
    name= fields.Char(string="Nombre", required= True)
    apellido= fields.Char(string="Apellido", required= True)
    fechaNac= fields.Date(string="Fecha de Nacimiento", required= True)
    cursoAcademico= fields.Selection([('0', '19/20'), ('1', '20/21')], string= "Curso", help="Selecciona tu curso actual")
    correoElectronico= fields.Char(string="Correo Elctrónico", required= False)
    telefono= fields.Integer(string="Teléfono", required= False)
    cicloFormativo= fields.Selection([('0', 'DAM'), ('1', 'DAW'), ('2', 'ASIR')], string= "Ciclo Formativo", help="Selecciona tu ciclo")
    periodoPractica= fields.Selection([('0', 'Marzo'), ('1', 'Septiembre')], string= "Prácticas", help="Selecciona tu mes de prácticas", required= True)
    notaMedia= fields.Float(string= "Nota Media", required= True)
    notaMediaTxt= fields.Char(string="Nota Media", compute="_notaMediaTxt", store=True)
    empresa= fields.Many2one("instituto.empresa", string="Empresa", required= True, ondelete="cascade")
    @api.depends('notaMedia')
    def _notaMediaTxt(self):
        for r in self:
            if r.notaMedia <5:
                r.notaMediaTxt = "Suspenso"
            elif r.notaMedia >=5 and r.notaMedia <=6:
                r.notaMediaTxt = "Aprobado"
            elif r.notaMedia >=7 and r.notaMedia <=8:
                r.notaMediaTxt = "Notable"
            else:
                r.notaMediaTxt = "Sobresaliente"

class instituto_empresa(models.Model):
    _name = 'instituto.empresa'
    name = fields.Char(string="nombre", requires=True)
    personaContacto = fields.Char(string="Persona de contacto", requires=True)
    telefonoContacto= fields.Integer(string="Telefono de contacto", requires=True)
    correoElctronico= fields.Char(string="Correo Electrónico", requires=True)
    direccion= fields.Char(string="Dirección", requires=True)
    alumnos= fields.One2many("instituto.alumno", "empresa", string="Alumnos", required= True)

from odoo import models, fields

class Professeur(models.Model):
    _name = 'absence.professeur'
    _description = 'Professeur'

    name = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    email = fields.Char(string='Email')
    specialite = fields.Char(string='Spécialité')

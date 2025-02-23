from odoo import models, fields

class Session(models.Model):
    _name = 'session'
    _description = 'Session'

    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor') #string es la etiqueta del campo 
    name = fields.Char(string='Session', required=True)
    date_start = fields.Datetime(string='Date start', required=True)
    #date_start = fields.Datetime('Date start', required=True)
    #date_start = fields.Datetime(required=True) # valor por defecto, en caso de no usar el string del campo: Date Start
    duration = fields.Float(string='Duration')
    course_id = fields.Many2one(comodel_name='course', string='Course')
    active = fields.Boolean()
    
    #Campo Relacional
    #Primera forma- Reducida
    attendee_ids=fields.Many2many('res.partner', string ="Session attendees")
    
    #Para realizar una relacion de muchos a muchos y hacer relacion a la misma tabla mas de 1 vez
    #Fuerzas la tabla con el nombre de la tabla Origen_destino_rel
    #instructor_ids=fields.Many2Many('res.partner','session_instructor_rel','session_id','instructor_id', string ="Session instructors")

 




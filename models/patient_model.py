from odoo import fields, models


class Patient(models.Model):
    _name = "patient.model"
    _description = "Patient Information"
    _rec_name = "patient_name"

    # Basic information----------------------------------------------------------------------------->
    patient_image = fields.Image(max_width=128, max_height=128)
    patient_name = fields.Char(string="Name", required=True)
    patient_age = fields.Char(string="Age", required=True)

    patient_gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], default="female", string="Gender")

    patient_blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-')
    ], string="Blood Group", default="a+")

    patient_phone = fields.Char(string="Phone")
    patient_email = fields.Char(string="Email")
    patient_address = fields.Text(string="Address")

    doctor_id = fields.Many2one("doctor.model", string="Select Doctor", required=True)
    appointment_ids = fields.One2many('appointment.model', 'patient_id', string='Appointments')

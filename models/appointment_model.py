from odoo import models, fields


class Appointment(models.Model):
    _name = "appointment.model"
    _description = "Appointment Information"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one("patient.model", string="Select Patient", required=True)
    appointment_date = fields.Date(string="Appointment Date", required=True)
    is_fee_pay = fields.Boolean(string="Paid", required=True)
    state = fields.Selection([
        ("draft", "Draft"),
        ("confirm", "Confirmed"),
        ("done", "Done"),
        ("canceled", "Canceled")
    ], string="Status", default="draft")
    patient_note = fields.Text(string="Description")
    doctor_id = fields.Many2one("doctor.model", string="Select Doctor", required=True)
    doctor_fee = fields.Float(string="Doctor Fee", related="doctor_id.doctor_fees", readonly=True)

    def action_fee_details_view(self):
        return {
            "name": "Patient Bill",
            "res_model": "patient.bill.model",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "target": "new",
            "context": {"default_patient_id": self.id},
        }


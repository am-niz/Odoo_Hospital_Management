from odoo import fields, models, api


class PatientBillWizard(models.TransientModel):
    _name = "patient.bill.model"
    _description = "Patient Bill Details"

    patient_name = fields.Char(string="Patient Name", readonly=True)
    doctor_name = fields.Char(string="Doctor Name", readonly=True)
    appointment_date = fields.Date(string="Appointment Date", readonly=True)
    note = fields.Text(string="Description", readonly=True)
    fee_paid = fields.Float(string="Fee Paid", readonly=True)

    @api.model
    def default_get(self, fields): # 'fields parameter is mandatory because default_get is inbuilt function
        res = super(PatientBillWizard, self).default_get(fields)
        if self._context.get("default_patient_id"):
            appointment = self.env["appointment.model"].browse(self._context["default_patient_id"])
            res.update({
                "patient_name": appointment.patient_id.patient_name,
                "doctor_name": appointment.doctor_id.doctor_name,
                "appointment_date": appointment.appointment_date,
                "note": appointment.patient_note,
                "fee_paid": appointment.doctor_fee,
            })
        return res

from odoo import fields, models, api


class Doctor(models.Model):
    _name = "doctor.model"
    _description = "Doctor Information"
    _rec_name = "doctor_name"

    # Basic information------------------------------------------------------------------------------------>
    user_id = fields.Many2one('res.users', string='Related User')
    doctor_image = fields.Image(max_width=100, max_height=100, string="Image")
    doctor_name = fields.Char(string="Name", required=True)
    specialization = fields.Selection([
        ("cardiologist", "Cardiologist"),
        ("psychiatrist", "Psychiatrist"),
        ("neurologist", "Neurologist"),
        ("ent", "ENT"),
        ("pediatrics", "Pediatrics"),
        ("radiologist", "Radiologist"),
        ("gastroenterology", "Gastroenterology")
    ], default="cardiologist", string="Specialization")
    doctor_age = fields.Char(string="Age")
    doctor_gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], default="female", string="Gender")
    doctor_nationality = fields.Char(string="Nationality")

    # Contact Information------------------------------------------------------------------------------------->
    doctor_phone = fields.Char(string="Phone")
    doctor_email = fields.Char(string="Email")
    doctor_address = fields.Text(string="Address")
    doctor_active_status = fields.Boolean(string="Active", default=True)

    # Professional Details------------------------------------------------------------------------------------->
    #specialisation
    doctor_dob = fields.Date(string="Date of Birth")
    doctor_join_date = fields.Date(string="Join Date")
    doctor_fees = fields.Float(string="Doctor Fee")

    # patients have to visit------------------------------------------------------------------------------------->
    # patient_list = fields.One2many("patient.model", "doctor_id", string="Patients Allotted")
    patient_appointed_list = fields.One2many("appointment.model", "doctor_id", string="Patients Booked")

    confirmed_patient_count = fields.Integer(compute="_compute_confirmed_patient_count", string="Confirmed Patients")

    @api.depends("patient_appointed_list.state")
    def _compute_confirmed_patient_count(self):
        for doctor in self:
            doctor.confirmed_patient_count = self.env["appointment.model"].search_count([
                ("doctor_id", "=", doctor.id),
                ("state", "=", "confirm")
            ])

    def display_confirmed_patients(self):
        self.ensure_one()
        return {
            "name": "Patients Confirmed",
            "res_model": "appointment.model",
            "type": "ir.actions.act_window",
            "target": "new",
            "view_mode": "tree",
            "domain": [("doctor_id", "=", self.id), ("state", "=", "confirm")],
            "context": {"create": False},
            "views": [(self.env.ref("hospital.appointment_doctor_tree_view_id").id, "tree")]
        }

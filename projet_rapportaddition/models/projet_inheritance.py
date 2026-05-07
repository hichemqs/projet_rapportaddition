from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    mission_order_ref = fields.Char(
        string="Référence Ordre de Mission",
        copy=False,
        readonly=True,
        default="Nouveau",
    )

    moyen_transport = fields.Char(string="Moyen de transport")
    materiel_disposition = fields.Char(string="Matériel mis à disposition")
    StartDate  = fields.Date(string="start date")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('mission_order_ref', 'Nouveau') == 'Nouveau':

                # ✅ FIX : force la recherche de séquence pour la société active
                company_id = self.env.company.id

                sequence = self.env['ir.sequence'].search([
                    ('code', '=', 'project.task.mission.order'),
                    '|',
                    ('company_id', '=', company_id),
                    ('company_id', '=', False),
                ], order='company_id desc', limit=1)

                if sequence:
                    vals['mission_order_ref'] = sequence.next_by_id()
                else:
                    vals['mission_order_ref'] = 'Nouveau'

        return super().create(vals_list)
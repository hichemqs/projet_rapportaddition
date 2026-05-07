from odoo import models, fields, api

class PlanningSlot(models.Model):
    _inherit = 'planning.slot'

    assigned_by = fields.Many2one('res.users', string='Assigned By', default=lambda self: self.env.user)


    mission_order_ref = fields.Char(
        string='Référence Ordre de Mission',
        readonly=True,
        copy=False,
        default='N/A',
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('mission_order_ref') or vals['mission_order_ref'] == 'N/A':
                vals['mission_order_ref'] = self.env['ir.sequence'].next_by_code('planning.slot') or 'N/A'
        return super().create(vals_list)

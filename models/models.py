# -*- coding: utf-8 -*-

from odoo import models, fields


class BidcomStatePropertyInherited(models.Model):
    _inherit = "bidcom_state_property"

    invoice_id = fields.Many2one(
        'account.move',
        string="Factura",
        readonly=True
    )

    def button_sold(self):
        for record in self:
            journal = self.env['account.journal'].search(
                [("type", "=", "sale")], limit=1
            )

            if not journal:
                raise ValueError(
                    "No se encontró un diario de ventas para generar la factura.")

            invoice = self.env['account.move'].with_context(default_move_type='out_invoice').create({
                'partner_id': record.partner_id.id,
                'journal_id': journal.id,
                "invoice_line_ids": [
                    (
                        0,
                        0,
                        {
                            "name": record.name,
                            "quantity": 1,
                            "price_unit": record.selling_price,
                        },
                    )
                ],
            })

            record.invoice_id = invoice.id
            invoice.action_post()

        return super().button_sold()

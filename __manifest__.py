# -*- coding: utf-8 -*-
# Copyright 2018 Dominic Krimmer, dominic.krimmer@gmail.com, Plastinorte S.A.S
# Copyright 2018 Luis Alfredo da Silva, luis.adasilvaf@gmail.com,  Plastinorte S.A.S
# Copyright 2018 https://github.com/exaap, EXA Auto Parts S.A.S
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Colombia - Impuestos',
    'category': 'Localization',
    'version': '0.1',
    'author': 'Luis Alfredo da Silva, Dominic Krimmer, Plastinorte S.A.S',
    'license': 'AGPL-3',
    'maintainer': 'dominic.krimmer@gmail.com',
    'website': 'https://www.plastinorte.com',
    'summary': 'Colombian Taxes: Invoice Module - Odoo 10.0',
    'images': ['images/'],
    'description': """
Colombia Impuestos:
======================
    * This module calculates some Colombian taxes that have to apply
    * First tax: withholding tax, which is calculated by 2,4% from the untaxed amount and calculated with the total amount
    """,
    'depends': [
        'account',
        'sale',
        'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/l10n_co_tax_extension.xml',
        #'views/report_invoice.xml',
        'views/ir_sequence_view.xml'
    ],
    'installable': True,
}



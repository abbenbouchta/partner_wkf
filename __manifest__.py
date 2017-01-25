# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : ' Process Partenaire',
    'version' : '0.1',
    'sequence': 165,
    'category': 'Partneiare',

    'description' : """
Main Features
-------------
* Add write/create access group
* Add a workflow to manage partners
* Add filters to confirmed partner in other objects (sale, purchase ,etc)

""",
    'depends': [
        'base',

    ],
    'data': [
        'security/security.xml',
    ],

    'demo': [],

    'installable': True,
    'application': False,
}

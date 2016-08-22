# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Operating Unit in CRM Claims",
    "version": "9.0.1.0.0",
    "author": "Eficent",
    "website": "http://www.eficent.com",
    "category": "CRM",
    "depends": ["crm_claim", "operating_unit"],
    "description": """
Operating Unit in CRM Claims
============================
This module introduces the security rules of operating unit to CRM Claims.
A user can only view and manage the claims associated to the warehouse of
the operating units that he has access to.

    """,
    "data": [
        "security/crm_security.xml",
        "views/crm_claim_view.xml"
    ],
    'installable': True,
    'active': False,
}

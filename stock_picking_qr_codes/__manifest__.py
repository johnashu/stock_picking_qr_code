# -*- coding: utf-8 -*-
{
    "name": "Stock Picking QR Codes",
    "version": "18.0.1.0.0",
    "category": "Inventory/Inventory",
    "author": "SJR Nebula",
    "website": "https://sjr.ie",
    "maintainer": "SJR Nebula",
    "support": "info@sjr.ie",
    "summary": "Replace barcodes with QR codes on stock picking and return slip reports.",
    "description": """
Stock Picking QR Codes
======================

Renders QR codes on the standard Stock Picking (Picking Operations) and
Return Slip PDF reports.

Picking Operations report (``stock.report_picking``):

* Document / picking name barcode -> QR
* Lot / Serial Number barcode -> QR
* Product barcode -> QR
* Package barcode -> QR

Return Slip report (``stock.report_return_slip``):

* Return reference barcode (``o.name``) -> QR
* OBTRETU barcode -> QR

The module inherits the standard QWeb templates with ``xpath`` overrides,
so no Python code or report template duplication is required.
    """,
    "depends": ["stock"],
    "data": [
        "views/stock_picking_qr_codes.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
    "license": "LGPL-3",
}

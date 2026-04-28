# -*- coding: utf-8 -*-
{
    "name": "Stock Picking QR Codes",
    "version": "17.0.1.0.3",
    "category": "Inventory/Inventory",
    "author": "SJR Nebula",
    "website": "https://sjr.ie",
    "maintainer": "SJR Nebula",
    "support": "info@sjr.ie",
    "summary": "Replace all barcodes with QR codes on stock picking reports.",
    "description": """
Stock Picking QR Codes
======================

Replaces every barcode on the standard Stock Picking (Delivery Slip) PDF
report with a QR code, including:

* Document / picking name
* Lot or Serial Number
* Product barcode
* Package barcode

The module inherits ``stock.report_picking`` and swaps the ``barcode``
widget options to use the ``QR`` symbology, so no Python code or report
template duplication is required.
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

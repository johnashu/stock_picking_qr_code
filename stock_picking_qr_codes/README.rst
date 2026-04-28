======================
Stock Picking QR Codes
======================

.. |badge1| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge2| image:: https://img.shields.io/badge/odoo-17.0-blueviolet.png
    :alt: Odoo 17.0

|badge1| |badge2|

Replaces every barcode on the standard Stock Picking (Delivery Slip) PDF
report with a QR code.

Features
========

The following barcodes are converted to QR codes on the picking report:

* **Document / picking name** — the header barcode identifying the transfer
* **Lot / Serial Number** — per move-line lot or serial barcode
* **Product barcode** — per move-line product barcode
* **Package barcode** — package label barcode

How it works
============

The module inherits the ``stock.report_picking`` QWeb template and uses
``xpath`` overrides with ``position="attributes"`` to swap each
``t-options`` ``barcode`` widget to use the ``QR`` symbology. No Python
code is added and no report templates are duplicated, so the module stays
compatible with future Odoo updates as long as the upstream xpath targets
remain stable.

Configuration
=============

No configuration required. After installing the module, print any stock
picking and the barcodes on the PDF will render as QR codes.

Usage
=====

#. Install the **Stock Picking QR Codes** module.
#. Open *Inventory → Transfers* and select a picking.
#. Click *Print → Picking Operations* (or *Delivery Slip*).
#. The PDF will now contain QR codes in place of the original barcodes.

Customisation
=============

The QR code dimensions can be tweaked in
``views/stock_picking_qr_codes.xml`` via the ``width``, ``height`` and
``img_style`` keys on each ``t-options`` attribute.

Bug Tracker
===========

Issues and feature requests can be sent to info@sjr.ie.

Credits
=======

Authors
~~~~~~~

* SJR Nebula

Maintainers
~~~~~~~~~~~

This module is maintained by `SJR Nebula <https://sjr.ie>`_.

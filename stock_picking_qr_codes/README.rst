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

For readability on printed reports, the encoded value is also shown as text
under the **Lot / Serial**, **Product**, and **Package** QR codes.

How it works
============

The module inherits the ``stock.report_picking`` QWeb template and uses
``xpath`` overrides with ``position="attributes"`` to swap each
``t-options`` ``barcode`` widget to use the ``QR`` symbology. No Python
code is added and no report templates are duplicated, so the module stays
compatible with future Odoo updates as long as the upstream xpath targets
remain stable.

For lot/serial, product, and package entries, additional ``xpath`` inserts
(``position="after"``) add a text label below each QR code with the same
value that was encoded.

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

Customisation — changing the QR code size
=========================================

The default sizes are tuned to roughly match the original barcodes, but
each QR code can be resized independently if it doesn't suit your paper
size or label layout. Edit
``views/stock_picking_qr_codes.xml`` and adjust the values inside each
``t-options`` attribute:

* ``width`` and ``height`` — the rendered image resolution in pixels
  (controls QR sharpness; defaults to ``200`` x ``200``).
* ``img_style`` — the on-page CSS size, e.g.
  ``'width:80px;height:80px;'`` for the document and package codes, and
  ``'width:60px;height:60px;'`` for the lot/serial and product codes.

After changing the file, upgrade the module (*Apps → Stock Picking QR
Codes → Upgrade*) for the new sizes to take effect.

Example — make the document QR code larger::

    <attribute name="t-options">{'widget': 'barcode', 'symbology': 'QR',
        'width': 300, 'height': 300,
        'img_style': 'width:120px;height:120px;'}</attribute>

Known conflicts
===============

**stock_picking_totals_report**

If both this module and ``stock_picking_totals_report`` are installed on
the same database, the picking report will fail to render unless two of
the four QR templates are deactivated.

Why: ``stock_picking_totals_report`` rewrites the per-move-line row of
the picking report (``<tr t-as='ml'>``) to show consolidated product /
location totals instead. That row is where the lot/serial and product
barcodes used to live, so the xpath targets for those two QR conversions
no longer exist.

How to fix:

#. Go to *Settings → Technical → User Interface → Views*.
#. Search for the External ID ``stock_report_picking_qr_lot``,
   open it and untick **Active**, then save.
#. Repeat for ``stock_report_picking_qr_product``.

The document-name and package barcodes will still render as QR codes;
only the per-line lot/serial and product barcodes are skipped (they are
no longer printed by the totals report anyway).

If you later uninstall ``stock_picking_totals_report``, re-tick **Active**
on both views to bring the lot/serial and product QR codes back.

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

# -*- coding: utf-8 -*-
# Copyright (c) 2021, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from ghdiff import diff
from frappe import _
	
class WikiPagePatch(Document):
	def validate(self):
		self.orignal_code = frappe.db.get_value("Wiki Page", self.wiki_page, "content")
		self.diff = diff(self.orignal_code, self.new_code)
		self.orignal_preview_store = frappe.utils.md_to_html(self.orignal_code)
		self.new_preview_store = frappe.utils.md_to_html(self.new_code)

	def on_submit(self):
		if self.status != "Approved":
			frappe.throw(_('Please approve the Request before submitting'))
		wiki_page = frappe.get_doc("Wiki Page", self.wiki_page)
		wiki_page.update_page(wiki_page.title, self.new_code, self.message)
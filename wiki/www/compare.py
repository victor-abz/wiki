
import frappe

def get_context(context):
	context.no_cache = 1
	context.doc = frappe.get_doc('Wiki Page', frappe.form_dict.wiki_page)
	context = context.doc.get_context(context)

	return context
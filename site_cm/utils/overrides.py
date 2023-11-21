import frappe


def before_request():
	"""
	Can be used to setup global flags, do some headers changes, etc.
	Available all frappe.local variables:
		frappe.local.form_dict
		frappe.local.request
	"""
	# print("site_cm:overrides.before_request", frappe.local.request)
	# frappe.log_error("site_cm:overrides.before_request", frappe.local.request.__dict__)

	# Force homepage to "index"
	# If not defined by "Role"
	# frappe.local.flags.home_page = "index"
	pass


def after_request(response, request):
	"""
	Available response and request parameters.
	"""
	# print("site_cm:overrides.after_request")
	pass


def context_extend(context):
	if context.name == "app":
		return

	context.lang = frappe.local.lang or frappe.lang or frappe.db.get_default("lang")

	path = getattr(frappe.local, "path", "")
	# context.dfp_path = path if path != "index" else ""
	# context.dfp_url = frappe.utils.get_url(context.ae_path)


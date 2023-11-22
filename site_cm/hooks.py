app_name = "site_cm"
app_title = "Site ComoMejorar"
app_publisher = "DFP"
app_description = "Site ComoMejorar.info"
app_email = "developmentforpeople@gmail.com"
app_license = "agpl-3.0"
# required_apps = []


# Global overrides
# ----------------

# Prompt: "Create a friendly animal to be used as logo for a learn more and educational university. It must be simple and friendly."
app_logo_url = "/assets/site_cm/images/comomejorar-logo.svg"
# base_template = 'templates/base.html'
website_context = {
	# "favicon": "/assets/erpnext/images/erpnext-favicon.svg",
	"splash_image": "/assets/site_cm/images/comomejorar-logo.svg",
}
update_website_context = [
	"site_cm.utils.overrides.context_extend",
]


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/site_cm/css/site_cm.css"
# app_include_js = "/assets/site_cm/js/site_cm.js"

# include js, css files in header of web template
# web_include_css = "/assets/site_cm/css/site_cm.css"
# web_include_js = "/assets/site_cm/js/site_cm.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "site_cm/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}


# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "site_cm/public/icons.svg"


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }


# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]


# Website redirects 301
# ---------------------

website_redirects = [
	# # Absolute location
	# { "source": "/from", "target": "https://mysite/from" },
	# # Relative location
	# { "source": "/from", "target": "/main" },
	# # RegEx
	# # Use r as a string prefix if you use regex groups or want to escape any string literal
	# { "source": r"/from/(.*)", "target": r"/main/\1" }
	# dict(source=r'/testfrom', target=r'://testto1'),
	# dict(source=r'/testfromregex.*', target=r'://testto2'),
	# dict(source=r'/testsub/(.*)', target=r'://testto3/\1'),

	{ "source": "/test", "target": "/" }, # Frappe test page
	{ "source": "/all-products", "target": "/" }, # ERP page
	{ "source": "/index", "target": "/" },
	{ "source": "/request-to-delete-data", "target": "/" }, # Maybe to be enabled/customized
	{ "source": "/request-data", "target": "/" }, # Maybe to be enabled/customized

	# # Knowledge Base / KB / Support / Ayuda / Base de conocimiento
	# { "source": "/support", "target": "/preguntas-frecuentes" },
	# { "source": "/help", "target": "/preguntas-frecuentes" },
	# { "source": "/kb", "target": "/preguntas-frecuentes" },
	# { "source": r"/kb/(.*)", "target": r"/preguntas-frecuentes/\1" },
]


# Website rewrites
# IMPORTANT!!! EMPTY CACHE AFTER UPDATING RULES: bench --site all clear-cache
# https://werkzeug.palletsprojects.com/en/1.0.x/routing/#werkzeug.routing.Rule
website_route_rules = [
	# Avoid error with charset as gzip: LookupError: unknown encoding: gzip
	{"from_route": "/sitemap.xml.gz", "to_route": "sitemap.xml"},
	{"from_route": "/sitemap_news.xml.gz", "to_route": "sitemap_news.xml"},
	# {"from_route": "/preguntas-frecuentes/<category>", "to_route": "Help Article"},
	# {"from_route": "/contact", "to_route": "contacto"},
	# {"from_route": "/blog/<category>", "to_route": "Blog Post"},
	# {"from_route": "/kb/<category>", "to_route": "Help Article"},
]


# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "site_cm.utils.jinja_methods",
#	"filters": "site_cm.utils.jinja_filters"
# }


# Installation
# ------------

# before_install = "site_cm.install.before_install"
# after_install = "site_cm.install.after_install"


# Uninstallation
# ------------

# before_uninstall = "site_cm.uninstall.before_uninstall"
# after_uninstall = "site_cm.uninstall.after_uninstall"


# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "site_cm.utils.before_app_install"
# after_app_install = "site_cm.utils.after_app_install"


# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "site_cm.utils.before_app_uninstall"
# after_app_uninstall = "site_cm.utils.after_app_uninstall"


# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "site_cm.notifications.get_notification_config"


# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }


# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }


# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }


# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"site_cm.tasks.all"
#	],
#	"daily": [
#		"site_cm.tasks.daily"
#	],
#	"hourly": [
#		"site_cm.tasks.hourly"
#	],
#	"weekly": [
#		"site_cm.tasks.weekly"
#	],
#	"monthly": [
#		"site_cm.tasks.monthly"
#	],
# }


# Testing
# -------

# before_tests = "site_cm.install.before_tests"


# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "site_cm.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "site_cm.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# Request Events
# ----------------
before_request = ["site_cm.utils.overrides.before_request"]
after_request = ["site_cm.utils.overrides.after_request"]


# Job Events
# ----------
# before_job = ["site_cm.utils.before_job"]
# after_job = ["site_cm.utils.after_job"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]


# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"site_cm.auth.validate"
# ]


# Fixtures
# --------

# fixtures = ['Custom Field', 'Custom Script', 'Property Setter', 'Translation']
fixtures = [
	"System Settings",
	"Language",
	"Website Settings",
	"Web Page",
	"Blog Post",
	"Translation",
	# "List View Settings",
	# "List Filter",
	# "Global Defaults",
	# "Role Profile",
	# {'doctype': 'Translation', 'filters': [{'source_name', '', }]},
	# {'doctype':'Email Account', 'filters': [{'is_standard':0}]},
]
# Then: bench --site comomejorar.localhost export-fixtures

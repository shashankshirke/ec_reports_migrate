from . import __version__ as app_version

app_name = "ec_reports_migrate"
app_title = "EC Reports Migrate"
app_publisher = "Shashank"
app_description = "Migrate"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "s@s.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ec_reports_migrate/css/ec_reports_migrate.css"
# app_include_js = "/assets/ec_reports_migrate/js/ec_reports_migrate.js"

# include js, css files in header of web template
# web_include_css = "/assets/ec_reports_migrate/css/ec_reports_migrate.css"
# web_include_js = "/assets/ec_reports_migrate/js/ec_reports_migrate.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ec_reports_migrate/public/scss/website"

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

# Installation
# ------------

# before_install = "ec_reports_migrate.install.before_install"
# after_install = "ec_reports_migrate.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ec_reports_migrate.uninstall.before_uninstall"
# after_uninstall = "ec_reports_migrate.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ec_reports_migrate.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ec_reports_migrate.tasks.all"
# 	],
# 	"daily": [
# 		"ec_reports_migrate.tasks.daily"
# 	],
# 	"hourly": [
# 		"ec_reports_migrate.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ec_reports_migrate.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ec_reports_migrate.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ec_reports_migrate.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ec_reports_migrate.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ec_reports_migrate.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ec_reports_migrate.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []

fixtures = [
    "EC Leads Child",
    "EC Liquidity Child",
    "EC Sales Child",
    "EC Fixed Costs Child",
    "EC Sales Pipeline Onetime Child",
    "EC Sales Pipeline Retainer Child",
    "EC Leads Report",
    "EC Liquidity Report",
    "EC Fixed Costs Report",
    "EC Sales Report",
    "EC Sales Pipeline Report",
    "EC Retainers Child",
    "EC Retainers Report",
    "EC Outstanding Child",
    "EC Outstanding Report",
    "EC Expense Report",
    "EC Income Report",
    "EC General Ledger",
    "EC Expense Voucher"
]

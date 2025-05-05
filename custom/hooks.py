# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# App Information
app_name = "custom"
app_title = "Custom"
app_publisher = "Your Name"
app_description = "Custom app for ERPNext"
app_email = "your@email.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/custom/css/custom.css"
# app_include_js = "/assets/custom/js/custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/custom/css/custom.css"
# web_include_js = "/assets/custom/js/custom.js"

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

# before_install = "custom.install.before_install"
# after_install = "custom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in function called in "has_permission"

# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
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
# 		"custom.tasks.all"
# 	],
# 	"daily": [
# 		"custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"custom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"custom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["custom.utils.before_request"]
# after_request = ["custom.utils.after_request"]

# Job Events
# ----------
# before_job = ["custom.utils.before_job"]
# after_job = ["custom.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"custom.auth.validate"
# ] 
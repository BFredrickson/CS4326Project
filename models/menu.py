# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

#response.logo = A(B('web', SPAN(2), 'py'), XML('&trade;&nbsp;'),
#                  _class="navbar-brand", _href="http://www.web2py.com/",
#                  _id="web2py-logo")
#response.title = request.application.replace('Make Your Appointments. Keep Your Appointments.', ' ').title()
response.title = 'Make Your Appointments. Keep Your Appointments.'
response.subtitle = ' '

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('Group 10')
response.meta.description = myconf.get('Keep your appointments scheduled.')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('How It Works'), False, URL('default', 'index')),
        #(T('This App'), False, '#', [
            #(T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
            #LI(_class="divider"),
            #(T('Controller'), False,
            #URL(
            #     'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
            #(T('View'), False,
            # URL(
            #     'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
            #(T('DB Model'), False,
            # URL(
            #     'admin', 'default', 'edit/%s/models/db.py' % app)),
            #(T('Menu Model'), False,
            # URL(
            #     'admin', 'default', 'edit/%s/models/menu.py' % app)),
            #(T('Config.ini'), False,
            # URL(
            #     'admin', 'default', 'edit/%s/private/appconfig.ini' % app)),
            #(T('Layout'), False,
            # URL(
            #     'admin', 'default', 'edit/%s/views/layout.html' % app)),
            #(T('Stylesheet'), False,
            # URL(
            #     'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % app)),
            #(T('Database'), False, URL(app, 'appadmin', 'index')),
            #(T('Errors'), False, URL(
            #    'admin', 'default', 'errors/' + app)),
            #(T('About'), False, URL(
            #    'admin', 'default', 'about/' + app)),
        #]),
        (T('Help'), False, '#', [
            (T('Frequently Asked Questions'), False, ' '),
            LI(_class="divider"),
            (T('Contact'), False, ' '),
            (T('Submit a Ticket'), False, ' '),
            (T('Give Feedback'), False, ''),
            #(T('Overview'), False, ''),
            #(T('The Core'), False, ''),
            #(T('The Views'), False, ''),
            #(T('Database'), False, ''),
            #(T('Forms and Validators'), False, ''),
            #(T('Email and SMS'), False, ''),
            #(T('Access Control'), False, ''),
            #(T('Services'), False, ''),
            #(T('Ajax Recipes'), False, ''),
            #(T('Components and Plugins'), False, ''),
            #(T('Deployment Recipes'), False, ''),
            #(T('Other Recipes'), False, ''),
            #(T('Helping web2py'), False, ''),
            #(T("Buy web2py's book"), False, ''),
            ]),
        (T('Community'), False, None, [
            (T('Groups'), False, ' '),
            (T('Twitter'), False, ' '),
            (T('Live Chat'), False, ' '),]),
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()

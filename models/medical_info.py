# -*- coding: utf-8 -*-

db.define_table('form_info', 
                Field('first_name', requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
                Field('last_name', requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
                Field('age', 'integer', requires=IS_NOT_EMPTY()),
                Field('height', 'integer', requires=IS_NOT_EMPTY()),
                Field('weight', 'integer', requires=IS_NOT_EMPTY()))

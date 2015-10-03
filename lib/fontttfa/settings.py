#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
# Application Name
# ------------------------------------------------------------------------------
app_name = 'font-ttfa'

# ------------------------------------------------------------------------------
# Version Number
# ------------------------------------------------------------------------------
major_version = "0"
minor_version = "9"
patch_version = "0"

# ------------------------------------------------------------------------------
# Debug Flag (switch to False for production release code)
# ------------------------------------------------------------------------------
debug = False

# ------------------------------------------------------------------------------
# Usage String
# ------------------------------------------------------------------------------
usage = 'Usage: font-ttfa [font path] <..font path 2>'

# ------------------------------------------------------------------------------
# Help String
# ------------------------------------------------------------------------------
help = """---------------------------------------------------------
 font-ttfa
 TTFA table reporting for fonts hinted with ttfautohint
 Copyright 2015 Christopher Simpkins
 MIT license
 Source: https://github.com/source-foundry/font-ttfa
---------------------------------------------------------

DESCRIPTION

 The font-ttfa executable provides a report of the ttfautohint settings contained in the TTFA font table.

 The TTFA table is optionally added at hinting time with ttfautohint. Please refer to the ttfautohint documentation for details.

USAGE

 font-ttfa [font path 1] <font path 2> <...font path x>
"""

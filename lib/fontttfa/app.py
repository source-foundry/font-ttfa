#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
# font-ttfa
# Copyright 2016 Christopher Simpkins
# MIT license
# ------------------------------------------------------------------------------


# Application start
def main():
    import sys
    from commandlines import Command
    from Naked.toolshed.system import stderr, file_exists
    from fontTools import ttLib

    # Instantiate commandlines Command object
    c = Command()

    # Command line argument validation testing
    if c.does_not_validate_missing_args():
        from fontttfa.settings import usage as fontttfa_usage
        stderr("ERROR: missing arguments\n")
        stderr(fontttfa_usage)
        sys.exit(1)

    # Tests for help, usage, and version requests
    if c.is_help_request():  # User requested font-ttfa help information
        from fontttfa.settings import help as fontttfa_help
        print(fontttfa_help)
        sys.exit(0)
    elif c.is_usage_request():  # User requested font-ttfa usage information
        from fontttfa.settings import usage as fontttfa_usage
        print(fontttfa_usage)
        sys.exit(0)
    elif c.is_version_request():  # User requested font-ttfa version information
        from fontttfa.settings import app_name, major_version, minor_version, patch_version
        version_display_string = app_name + ' ' + major_version + '.' + minor_version + '.' + patch_version
        print(version_display_string)
        sys.exit(0)
    # ------------------------------------------------------------------------------------------
    # [ PRIMARY COMMAND LOGIC ]
    #   Enter your command line parsing logic below
    # ------------------------------------------------------------------------------------------

    try:
        for fontpath in c.arguments:
            if file_exists(fontpath):
                if fontpath.endswith('.ttf'):
                    tt = ttLib.TTFont(fontpath)
                    if 'TTFA' in tt.keys():
                        length_fontpath = len(fontpath)
                        if length_fontpath < 80:
                            outline_string = "=" * length_fontpath
                        else:
                            outline_string = "=" * 80
                        print(" ")
                        print(outline_string)
                        print(fontpath)
                        print(outline_string)
                        ttfautohint = (tt['TTFA'].__dict__['data']).strip()
                        print(ttfautohint)
                    else:
                        stderr(
                            "[font-ttfa]: Unable to detect a TTFA table in '" + fontpath +
                            "'.  Please confirm that ttfautohint has been used on this file and that the TTFA table was added.")
                else:
                    stderr("[font-ttfa]: The file '" + fontpath + "' does not appear to be a TrueType font file.")
            else:
                stderr("[font-ttfa]: The path '" + fontpath + "' is not a valid file path.")
    except Exception as e:
        stderr("[font-ttfa]: Error: " + str(e))


if __name__ == '__main__':
    main()

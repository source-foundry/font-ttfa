#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
# font-ttfa
# Copyright 2015 Christopher Simpkins
# MIT license
# ------------------------------------------------------------------------------


# Application start
def main():
    import sys
    from Naked.commandline import Command
    from Naked.toolshed.system import stderr, file_exists
    from fontTools import ttLib

    # ------------------------------------------------------------------------------------------
    # [ Instantiate command line object ]
    #   used for all subsequent conditional logic in the CLI application
    # ------------------------------------------------------------------------------------------
    c = Command(sys.argv[0], sys.argv[1:])
    # ------------------------------------------------------------------------------------------
    # [ Command Suite Validation ] - early validation of appropriate command syntax
    # Test that user entered at least one argument to the executable, print usage if not
    # ------------------------------------------------------------------------------------------
    if not c.command_suite_validates():
        from fontttfa.settings import usage as fontttfa_usage
        print(fontttfa_usage)
        sys.exit(1)
    # ------------------------------------------------------------------------------------------
    # [ NAKED FRAMEWORK COMMANDS ]
    # Naked framework provides default help, usage, and version commands for all applications
    #   --> settings for user messages are assigned in the lib/font-ttfa/settings.py file
    # ------------------------------------------------------------------------------------------
    if c.help():  # User requested font-ttfa help information
        from fontttfa.settings import help as fontttfa_help
        print(fontttfa_help)
        sys.exit(0)
    elif c.usage():  # User requested font-ttfa usage information
        from fontttfa.settings import usage as fontttfa_usage
        print(fontttfa_usage)
        sys.exit(0)
    elif c.version():  # User requested font-ttfa version information
        from fontttfa.settings import app_name, major_version, minor_version, patch_version
        version_display_string = app_name + ' ' + major_version + '.' + minor_version + '.' + patch_version
        print(version_display_string)
        sys.exit(0)
    # ------------------------------------------------------------------------------------------
    # [ PRIMARY COMMAND LOGIC ]
    #   Enter your command line parsing logic below
    # ------------------------------------------------------------------------------------------

    try:
        for fontpath in c.argv:
            if file_exists(fontpath):
                if fontpath.endswith('.ttf'):
                    tt = ttLib.TTFont(fontpath)
                    if 'TTFA' in tt.keys():
                        length_fontpath = len(fontpath)
                        if length_fontpath < 80:
                            outline_string = "=" * length_fontpath
                        else:
                            outline_string = "=" * 80
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

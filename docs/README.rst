Source Repository: `<https://github.com/source-foundry/font-ttfa>`_

What is font-ttfa?
----------------------------

font-ttfa is a command line executable that provides a standard output stream report of font hinting settings from the TTFA table of fonts that were hinted with `ttfautohint <http://www.freetype.org/ttfautohint/>`_.  It is built with the fantastic FontTools library.


Install
--------------

Install with ``pip`` using the command:

::

    $ pip install font-ttfa


or `download the source repository <https://github.com/source-foundry/font-ttfa/tarball/master>`_, unpack it, and navigate to the top level of the repository.  Then enter:


::

    $ python setup.py install


Usage
------------


::

    $ font-ttfa [font path 1] [font path 2] [...font path x]

# checksum-comparator
Yet another comparison tool for checksum files... Compare two non-identical, or identical checksum files.

# In the beginning...

Two CSV files of checksums are required for this comparison to work, on the comparison that you put crap in, you get crap out. 

Feed it two 'similar' files, and you should get a sensible comparison. Two lists of the form below should return a result of identical. 

    e0861941c1ac038836097a8f2a3e729482fe1acd,Files/speech.doc
    318e91cdfca61d11a250a907bad6fd039c91b5d0,Files/revised DRAFT.doc
    203a7c3aebf65f93552774accd7fa268a587667b,Files/2006-07.dot
    0bc546eafd5d12b16c4d2ff27ff3bb7789adef26,Files/Barnet.doc

Part of the principle of keeping this tool so simple, is that, using tools like SHA1DEEP, it is easy to pre-condition the shape of a checksum file e.g. convert to Linux paths, where it isn't necessarily easy to compare dissimilar lists, that is, checksum lists from different points in time following disposal actions and pre-conditioning actions. 

Tool should return simple output, identical, lists of differences, lists of similarities. 

That is what it does. More below. 

###Unit Tests

One cannot emphasise enough the importance of unit tests in code for this purpose. Tests will continue to be added to this repository.

###Example Use

> python checksumcomparator.py --check1 2015-01-26-e3-hashes-normalized.txt --check2 2015-05-18-checksums-sha1-normalized.txt --pre --v

    usage: checksumcomparator.py [-h] [--check1 CHECK1] [--check2 CHECK2] [--pre]
                                 [--v]

    Compare two non-identical, or identical checksum files.

    optional arguments:
      -h, --help       show this help message and exit
      --check1 CHECK1  Checksum file one.
      --check2 CHECK2  Checksum file two.
      --pre            Pre-conditioned objects.
      --v              Verbose: Output comparison list.

###License

Copyright (c) 2015 Ross Spencer

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.

Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

This notice may not be removed or altered from any source distribution.

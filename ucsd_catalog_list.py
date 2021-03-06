#! /usr/bin/env python

'''
    Command Line Utility to return a list of Catalog Options
'''


import requests
import json
from ucsd_library import catalog_list

if __name__ == '__main__':

    import sys
    from pprint import pprint
    from argparse import ArgumentParser, FileType

    p = ArgumentParser()
    p.add_argument('-g', '--group',                          # Name stored in namespace
                   metavar = 'UCSD End User Group',            # Arguement name displayed to user
                   help = 'The UCSD End User Group to Query for.  - Default to "Default Group"',
                   type = str, default="Default Group"
                    )
    p.add_argument('-f',                          # Name stored in namespace
                   metavar = 'A field to return',            # Arguement name displayed to user
                   help = 'Which detail fields to return.  Can be used multiple times.',
                   type = str, action="append", default = []
                    )
    p.add_argument('-k',
                   metavar = "The field to search.  ",
                   help = "Which detail field to search for.",
                   type = str
                   )
    p.add_argument('-v',
                   metavar = "The value to search for.  ",
                   help = "What value to search the detail field for.",
                   type = str
                   )

    ns = p.parse_args()
    if (ns.k and ns.v): rf = {ns.k:ns.v}
    else: rf = {}

    result = catalog_list(group=ns.group, key_filter=ns.f, result_filter = rf)

    pprint (result)


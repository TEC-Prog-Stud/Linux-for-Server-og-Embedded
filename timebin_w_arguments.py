#!/usr/bin/env python3
"""
Write current time in binary
"""
__docformat__ = 'reStructuredText'
import argparse
from datetime import datetime
from email.policy import default

def main():
    """
    Entry point into the program.
    """
    # Create command line parameter parser object.
    parser = argparse.ArgumentParser(description="Hello world type program for greeting someone.")
    # Add optional command line parameters.
    parser.add_argument('--hour', action='store', 
                        dest='hFormat', 
                        default='24',
                        help='Whether to use 12h or 24h format',
                        choices=['12', '24'])
    parser.add_argument('--rows', 
                        type=int,
                        action='store',
                        dest='nRows',
                        help='Whether to display in 3 or 6 rows',
                        choices=[3, 6]
                        )
#default="6",
                        
    # Perform actual command line parameter parsing.
    args = parser.parse_args()
    
    # Display greeting
    print('Hello! you chose, ' + args.hFormat + '!')
    t = datetime.now()
    h = t.hour
    if args.hFormat == '12':
        if h > 12:
            h -= 12
        elif h == 0:
            h = 12

    print(f"klokken er: {h :8b} : {t.minute :8b}")
    print(f"klokken er: {h :8d} : {t.minute :8d}")
    print(f"number of rows: {args.nRows}, {type(args.nRows)}")
if __name__ == '__main__':
    exit(main())

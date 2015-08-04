#!/usr/bin/env python
'''
Write a Python program using ciscoconfparse that parses cisco_ipsec.txt. The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.
'''
from ciscoconfparse import CiscoConfParse

def main():
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

    intf = cisco_cfg.find_objects(r"^crypto map CRYPTO")

    for i in intf:
        print i.text
        for j in i.children:
            print j.text
        print

if __name__ == "__main__":
    main()

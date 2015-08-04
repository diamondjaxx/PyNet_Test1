#!/usr/bin/env python
'''
Find all of the crypto map entries that are using PFS group2
'''
from ciscoconfparse import CiscoConfParse

def main():
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

    intf = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

    print "Crypto maps using PFS group2:"
    for i in intf:
        print i.text

if __name__ == "__main__":
    main()

#!/usr/bin/env python
'''
Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.
'''
from ciscoconfparse import CiscoConfParse

def main():
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

    intf = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

    print "Crypto maps not using AES:"
    for i in intf:
        print i.text
        for j in i.children:
            if 'transform' in j.text:
                print j.text

if __name__ == "__main__":
    main()

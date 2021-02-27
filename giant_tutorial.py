import scapy as scapy
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP Address/Adresses")
    options = parser.parse_args()

    if not options.target:
        parser.error("[-] Please, specify an IP address or Adresses, use --help for more info.")
    return options

options = get_args()
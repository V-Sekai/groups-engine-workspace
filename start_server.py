#!/usr/bin/python3
# https://gist.github.com/Faless/1e228325ced0662aee59dc92fa69efd7
# Note: You also need to be in a secure context, for WebAssembly threads to be enabled, 
# so you have to visit the page via http://127.0.0.1:8060/ or http://localhost:8060/, 
# other addresses will not work without SSL.
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import os, sys, logging
import argparse

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=8060, type=int)
    parser.add_argument('-r', '--root', default='', type=str)
    args = parser.parse_args()
    if args.root:
        os.chdir(args.root)
    test(CORSRequestHandler, HTTPServer, port=args.port)
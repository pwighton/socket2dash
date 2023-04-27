#!/usr/bin/env python3

import argparse
import socket
import traceback
import time

parser = argparse.ArgumentParser(description="Parse command line options")
parser.add_argument("host")
parser.add_argument("port")
parser.add_argument("infile")
parser.add_argument('-c', '--chunk-size', type=int, default=2048, help='Max chunk size to read')

args = parser.parse_args()

try:
  print("Opening " + args.infile + " for reading..")
  f = open(args.infile, 'rb')

  s = socket.socket()
  s.connect((args.host,int(args.port)))
  print(f'Sending data to {args.host}:{args.port} with max chunk of {args.chunk_size}')
  
  start_time = time.time()
  num_bytes_read = 0  
  while True:
    data = f.read(args.chunk_size)
    if not data or len(data)==0: break
    num_bytes_read += len(data)
    s.send(data)
  end_time = time.time()  
  
  print(f'Sent a total of {num_bytes_read} bytes in max chunks of {args.chunk_size} to {args.host}:{args.port} in {end_time - start_time} seconds')
    
except Exception as e:
  print("!!!!! Caught an exception:", e)
  if 'start_time' in locals():
    end_time = time.time()    
    print(f'Sent a total of {num_bytes_read} bytes in max chunks of {args.chunk_size} to {args.host}:{args.port} in {end_time - start_time} seconds')

  traceback.print_exc()
  
finally:
  if 's' in locals():
    print("Closing Socket")
    s.close()
  if 'f' in locals():
    print("Closing File")
    f.close()

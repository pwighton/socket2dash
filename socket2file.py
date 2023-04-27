#!/usr/bin/env python3

import argparse
import socket
import traceback

parser = argparse.ArgumentParser(description="Parse command line options")
parser.add_argument("port")
parser.add_argument("outfile")
args = parser.parse_args()

host = "0.0.0.0"

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # https://docs.python.org/3/library/socket.html#socket.socket.settimeout
  s.settimeout(15000)
  s.bind((host, int(args.port)))
  s.listen(1)
  print("Listening on: ", (host, int(args.port)) )
  conn, addr = s.accept()
  conn.settimeout(15000)
  print("Connected to ", addr)

  print("Opening " + args.outfile + " for writing..")
  f = open(args.outfile, 'wb')
   
  num_bytes_read = 0  

  # old way
  #while True: 
  #  data = conn.recv(2048)
  #  if not data or len(data)==0: break
  #  num_bytes_read += len(data)
  #  f.write(data)
  
  while True:
    try:
      data = conn.recv(2048)
      if not data or len(data)==0: break
      num_bytes_read += len(data)
      f.write(data)
    except socket.error as e:
      # Reestablish connection of disconnected
      # https://stackoverflow.com/questions/21027949/python-tcp-disconnect-detection
      if e.errno == errno.ECONNRESET:
        print("Connection was reset, re-opening..")
        conn.close()
        conn, addr = s.accept()
        conn.settimeout(15000)
        print("Re-connected to ", addr)
      else:
        raise
  
  print("Read a total of "+str(num_bytes_read)+" bytes")
  
  f.close()
  
except Exception as e:
  print("!!!!! Caught an exception:", e)
  traceback.print_exc()

finally:
  if 'conn' in locals():
    print("Closing Connection")
    conn.close()
  if 's' in locals():
    print("Closing Socket")
    s.close()
  if 'f' in locals():
    print("Closing File")
    f.close()

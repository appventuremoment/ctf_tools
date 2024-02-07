from pwn import *
from Crypto.Util.number import *
from randcrack import RandCrack

rc = RandCrack()
conn = remote('challenge1.whitehacks.whitehats.live', 5002)

#CHANGE INPUT HOW MANY TIMES YOU SEND & RECEIVE
for i in range(624):
	conn.recv()
	conn.sendline(b'1')
	conn.recv()
	conn.sendline(b'1')

	#CHANGE THE TEXT RIGHT AFTER THE RANDOM-GENERATED NUMBER ("\nCapy") in this case
	temp = conn.recvuntil("\nCapy", drop = True).decode("utf-8")
	temp = temp.split("ID: ")
	#print(temp)
	rc.submit(int(temp[-1]))
	conn.recv()
	conn.sendline(b'1')


print("------------DONE-------------")

print(conn.recv())

#CHANGE INPUT
conn.sendline(b'1')

#CHANGE WHAT IS GENERATED AND SENT
for i in range(1):
	conn.sendline(bytes(str(rc.predict_getrandbits(32)), "utf-8"))

#CHANGE WHAT IS RECEIVED AND HOW MANY TIMES
for i in range(3):
	print(conn.recv())
conn.close()

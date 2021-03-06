import struct

N = 25


greetingMessage = struct.pack ("25B", *[0x59,0x6f,0x75,0x20,0x68,0x61,0x76,0x65,0x20,0x6e,0x6f,
                                        0x77,0x20,0x65,0x6e,0x74,0x65,0x72,0x65,0x64,0x20,0x74,
                                        0x68,0x65,0x20])

sekrutBuffer = struct.pack ("25B", *[0x29,0x06,0x16,0x4f,0x2b,0x35,0x30,0x1e,0x51,0x1b,0x5b,
                                     0x14,0x4b,0x08,0x5d,0x2b,0x56,0x47,0x57,0x50,0x16,0x4d,
                                     0x51,0x51,0x5d])



print(greetingMessage)
print(sekrutBuffer)

password = [0]* N

for i in range(N):
    password[i] = greetingMessage[i] ^ sekrutBuffer[i]

print("PASSWORD: "+''.join(map(lambda x:chr(x), password)))
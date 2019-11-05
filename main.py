keyMatrix = [[0] * 3 for i in range(3)] 

#vector for the message 
messageVector = [[0] for i in range(3)] 

#vector for the cipher 
cipherMatrix = [[0] for i in range(3)] 

#key matrix function
def getKeyMatrix(key): 
	k = 0
	for i in range(3): 
		for j in range(3): 
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1

#encrypting function 
def encrypt(messageVector): 
	for i in range(3): 
		for j in range(1): 
			cipherMatrix[i][j] = 0
			for x in range(3): 
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j]) 
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key): 

	#Getting key matrix 
	getKeyMatrix(key) 

	#vector 
	for i in range(3): 
		messageVector[i][0] = ord(message[i]) % 65

	#encrypted vector 
	encrypt(messageVector) 
 
	#encrypted text 
	CipherText = [] 
	for i in range(3): 
		CipherText.append(chr(cipherMatrix[i][0] + 65)) 

	#ciphertext 
	print("Ciphertext: ", "".join(CipherText)) 

#main Function
def main(): 

	message = "USA"

	key = "YBNQKURPG"

	HillCipher(message, key) 

if __name__ == "__main__": 
	main() 


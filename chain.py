import time
# Used for the hasing function
import hashlib

class block:
    def __init__(self, blockID, hash):
        self.timeStamp = time.now()
        self.blockID = blockID
        self.hash = hash

class chain:
    # Used to initialize the chain containing the transaction blocks
    def __init__(self):
        # Contains the linked blocks
        self.chain = []
        
        self.current_transaction = []

    # Hash generator function used to generate a proof hash using the users private key and public key
            # Using the sha256 algorithm
    def generateAuthenticationHash(self, transactionID, privateKey, publicKey):
        generatedHash = hashlib.new("sha256")
        generatedHash.update((transactionID + privateKey + publicKey).encode("utf-8"))

        return generatedHash.hexdigest()
    
    def transaction(self, senderKey, recipientKey, amount):
        self.current_transaction.append({"sender" : senderKey,
                                         "recipient" : recipientKey,
                                         "amount" : amount})

newChain = chain()
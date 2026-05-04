import hashlib   # Used to create SHA256 hashes
import time      # Used to get current timestamp
# -----------------------------
# Block class (represents a single block)
# -----------------------------
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index                  # Block number
        self.timestamp = timestamp          # Time when block is created
        self.data = data                    # Transaction data
        self.previous_hash = previous_hash  # Hash of previous block
        self.hash = self.calculate_hash()   # Hash of current block
    # Function to calculate SHA256 hash of the block
    def calculate_hash(self):
        # Combine block data into a single string
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        # Generate SHA256 hash
        return hashlib.sha256(value.encode()).hexdigest()
# -----------------------------
# Blockchain class (manages the chain of blocks)
# -----------------------------
class Blockchain:
    def __init__(self):
        # Initialize blockchain with the genesis block
        self.chain = [self.create_genesis_block()]
    # Create the first block of the blockchain
    def create_genesis_block(self):
        return Block(0, time.ctime(), "Genesis Block", "0")
    # Get the most recent block in the chain
    def get_latest_block(self):
        return self.chain[-1]
    # Add a new block to the blockchain
    def add_block(self, data):
        previous_block = self.get_latest_block()   # Get last block
        new_block = Block(
            index=len(self.chain),                # New block index
            timestamp=time.ctime(),               # Current time
            data=data,                            # Transaction data
            previous_hash=previous_block.hash     # Link to previous block
        )
        self.chain.append(new_block)               # Add block to chain
    # Display all blocks in the blockchain
    def display_chain(self):
        for block in self.chain:
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("-" * 50)
# -----------------------------
# Creating the Blockchain
# -----------------------------
my_blockchain = Blockchain()   # Create blockchain object
# Add 4 blocks with transaction data
my_blockchain.add_block("Transaction 1: A pays B")
my_blockchain.add_block("Transaction 2: B pays C")
my_blockchain.add_block("Transaction 3: C pays D")
my_blockchain.add_block("Transaction 4: D pays E")
# Display original blockchain
print("🔗 Original Blockchain:")
my_blockchain.display_chain()
# -----------------------------
# Tampering with a block
# -----------------------------
print("\n Modifying Block 2 Data...\n")
# Change data of block at index 2
my_blockchain.chain[2].data = "Hacked Transaction"
# Recalculate hash after modification
my_blockchain.chain[2].hash = my_blockchain.chain[2].calculate_hash()
# Display blockchain after tampering
print("🔗 Blockchain After Tampering:")
my_blockchain.display_chain()
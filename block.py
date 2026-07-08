import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

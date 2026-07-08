from block import Block
from transaction import Transaction


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, "0", [])
        self.chain.append(genesis)

    def add_transaction(self, sender, receiver, amount):
        tx = Transaction(sender, receiver, amount)
        self.pending_transactions.append(tx)

    def mine_pending_transactions(self):
        previous_block = self.chain[-1]
        block = Block(
            len(self.chain),
            previous_block.hash,
            self.pending_transactions
        )
        self.chain.append(block)
        self.pending_transactions = []

    def print_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Transactions: {block.transactions}")

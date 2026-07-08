import secrets
import hashlib


class Wallet:
    def __init__(self):
        self.private_key = secrets.token_hex(32)
        self.public_key = hashlib.sha256(self.private_key.encode()).hexdigest()
        self.address = "NVX" + self.public_key[:32]
        self.balance = 0

    def show_wallet(self):
        print("=== NovaX Wallet ===")
        print("Address:", self.address)
        print("Balance:", self.balance, "NVX")

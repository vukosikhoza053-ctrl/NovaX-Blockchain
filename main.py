from blockchain import Blockchain

def main():
    blockchain = Blockchain()

    print("=== Welcome to NovaX Blockchain ===")
    blockchain.add_transaction("Alice", "Bob", 10)
    blockchain.add_transaction("Bob", "Charlie", 5)

    blockchain.mine_pending_transactions()

    blockchain.print_chain()

if __name__ == "__main__":
    main()

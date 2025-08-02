import torch
import numpy as np
import faiss
from ecdsa import SigningKey, SECP256k1
from bitcoinlib.keys import Key

print(f"Torch CUDA available: {torch.cuda.is_available()}")
print(f"FAISS version: {faiss.__version__}")

# ECC signing test for CryptoForge
sk = SigningKey.generate(curve=SECP256k1)
signature = sk.sign(b"Test CryptoForge Transaction")
print("ECC Test: Success")

# Bitcoinlib test
key = Key()
print(f"Bitcoin Address: {key.address()}")

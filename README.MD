# One-Time Pad
- The one-time pad is a way of encrypting and decrypting a plaintext with a shared randomly generated key
- If the key is randomly generated (it's only pseudorandomly generated in this case), then it is completely unbreakable
- The key cannot be reused, otherwise it may be possible for an attacker to spot a pattern and then decrypt the ciphertext
- Only the sender and the recipient should know the key, which they should decide on in advance
- The key should be shared in person between the communicating parties otherwise the security is limited by the cryptography used when sending it
# Security of This Implementation
- This implementation is only as secure as the method used to generate the key
- In this case, it uses the most secure source of randomness available from the operating system, but this still isn't as secure as a true random generator
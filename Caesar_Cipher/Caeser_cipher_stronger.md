# Stronger Caesar Cipher

An extended Caesar Cipher implementation using a **52-character alphabet** (`A-Z` + `a-z`) and a randomly generated shift key.

> This is an educational implementation and is not secure modern encryption.

## Features

- Uses a 52-character alphabet.
- Supports uppercase and lowercase letters.
- Generates a random key using `secrets.randbelow(52)`.
- Supports encryption and decryption.
- Preserves spaces and punctuation.
- Uses modular arithmetic.

___

## How It Works

The alphabet is:

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
```

Each character is assigned an index from 0 to 51.

```Encryption

C = (P + K) mod 52 
```

Where:

P = plaintext character index

K = random shift

C = ciphertext character index


```Decryption

P = (C - K) mod 52
```
The same key is used to reverse the transformation.

### Key Generation

The script generates the key with:
```python
secrets.randbelow(52)
```
This produces a value from 0 to 51.

The key is generated when the program starts and is not saved, so ciphertext from a previous execution cannot be decrypted unless the original key is known.

**Example**

If:

**Key** = 5

then:

A → F
B → G
...
Z → e

The exact output varies because the key is randomly generated.

### Security Limitations

Although this version uses   `52 characters instead of 26,` it still has only 52 possible keys. An attacker can easily try every key.

It is also vulnerable to frequency analysis because the same plaintext character always maps to the same ciphertext character for a given key.

Therefore, this cipher should not be used for protecting real-world sensitive information.

#### Complexity

For a message containing n characters:

Time:  O(n)
Space: O(n)

___

## Refrences

[Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) <br>
[Python Documentation - `secrets` module](https://docs.python.org/3/library/secrets.html)


___

## Disclaimer

This project is intended for educational purposes only.

___

## License

[MIT License](https://github.com/noob42-cyber/Scripts/blob/main/LICENSE)


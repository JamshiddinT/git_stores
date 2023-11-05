import hashlib

def calculate_hmac(message, key):
    key = bytes.fromhex(key)
    message_bytes = message.encode('utf-8')
    hmac = hashlib.sha256(key + message_bytes).hexdigest()
    return hmac

def verify_hmac(received_hmac, message, key):
    calculated_hmac = calculate_hmac(message, key)
    return received_hmac == calculated_hmac

partner_received_hmac = "685f94578bfaf927f31eb6248a42264da1ec69ac7e19ac6561e4befcb5cce44c"
your_key = "9533EEF7905A742AFA3AD8712D1D599ACE3D07906F1A755BC8362A31816ACB79"
your_message = "rock"

if verify_hmac(partner_received_hmac, your_message, your_key):
    print("HMAC is valid. The data is authentic. :) ")
else:
    print("HMAC is invalid. The data may have been tampered with.")

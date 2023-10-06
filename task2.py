import hashlib

def calculate_sha3_256(file_path):
    try:
        # Open the file in binary mode for reading
        with open(file_path, 'rb') as file:
            # Read the file content
            file_content = file.read()

            # Calculate SHA3-256 hash
            sha3_256_hash = hashlib.sha3_256(file_content).hexdigest()

            return sha3_256_hash

    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)

# Specify the path to the file you want to hash
file_path = 'home/j/Documents/Task2/task2.zip'

# Calculate SHA3-256 hash and print the result
sha3_256_hash = calculate_sha3_256(file_path)
if sha3_256_hash:
    print(f'SHA3-256 hash of {file_path}: {sha3_256_hash}')
else:
    print('Error calculating hash.')




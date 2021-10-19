from os import kill


def convert_bytes (bytes):
    return (bytes / 1024.0, bytes/ 1048576.0 )
    
bytes = 30000

kb, mb = convert_bytes (bytes)
print('bytes', bytes)
print('kilobytes', kb)
print('Megabytes', mb)


message = ' Hello There. My name is Nursima ÖNER'

# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()
# message = message.strip()
# message = message.split('.')

index = message.find('Nur')

message = '*'.join(message)
print(message)
print(message[2])
# isFound = message.startswith('N')
# isFound = message.endswith('r')

# message = message.replace('Nursima','ÖNER')
# message = message.replace('ç','c') 
#                  .replace('ö','o') 
#                  .replace(' ','-')
message = message.center(50, '*')

print(message)
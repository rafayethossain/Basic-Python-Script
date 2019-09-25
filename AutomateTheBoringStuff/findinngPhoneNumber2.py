import re
message = 'Call me 415-555-1013 tomorrow or at 15-555-9999'

phoneNumberRegx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegx.findall(message) # all instance

print(mo)


# Using regualar expression1
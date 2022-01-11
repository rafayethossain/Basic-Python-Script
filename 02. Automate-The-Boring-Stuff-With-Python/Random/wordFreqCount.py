import pprint
message = '''
    
People who are looking to stay well as they age may want to adopt a pet,
according to new data from the University of Michigan National Poll on Healthy Aging.
 
For the survey,
researchers polled about 2,000 U.S. adults from ages 50 to 80.
Fifty-five percent said they owned at least one pet. Dogs were the most common pet,
followed by cats and small animals, such as birds and hamsters. But no matter the
type of animal, the vast majority of owners said their pets boosted their mental
and physical health.

Nearly 90% of older pet owners said their animals helped them enjoy life and 
feel loved; roughly 80% said their pets reduced stress; and almost three-quarters
said their furry friends provided a sense of purpose, according to the poll.
In addition, 64% of pet owners — and 78% of dog owners — said their pets helped
them stay physically active. Sixty percent also said their pets helped them cope
with physical and emotional health issues.


'''
message = message.upper()
wordlist = message.split()



count = {}

for word in wordlist:
    count.setdefault(word, 0)
    count[word] = count[word] + 1

maximum = max(count, key=count.get)
minimum = min(count, key=count.get)


print("Number of word found:", len(wordlist))
print("Maximum times:",  maximum, "And minimum times:", minimum)
print("\n\n")

pprint.pprint(count)
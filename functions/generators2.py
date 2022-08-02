# wap to generates a list of acronyms from a list of words using generators

def acronym(*words):
    for words in words:
        yield ''.join([i[0].upper() for i in words.split()])

#example call:
for item in acronym('Project Manager','Software Engineer','Data Analyst'):
    print(item)

print(list(acronym('Project Manager','Software Engineer','Data Analyst','Team Lead')))
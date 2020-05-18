import re
doc_splitter = re.compile(r"^(?:Section\ )?\d+[\.\d+]?", re.MULTILINE)
text="""hi"""

starts = [match.span()[0] for match in doc_splitter.finditer(text)] + [len(text)]

sections = [text[starts[idx]:starts[idx+1]] for idx in range(len(starts)-1)]
for section in sections:
    print([section])


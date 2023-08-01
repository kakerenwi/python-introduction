traffic_signals = ("red", "green", "yellow", "red") # with tuple you cannot modify the list or append it.

medical_report = (25.7, 8.2)

travel_docs = ("visa", "passport", "RT PCR")

print(travel_docs)
print(type(travel_docs))

print(travel_docs[1])   

print("yellow" in traffic_signals)
print(len(travel_docs))

# dir(()) for tuple has just two functions. Count and Index.
print(traffic_signals.count("red"))

print(travel_docs.index("passport"))

for i in travel_docs:
    print(i)


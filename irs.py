
import math
def krishna(corpus)
    docs=[docs.lower().split() for doc in corpus]
    voc=set(sum(docs,[]))
    n=len(docs)
    krishna={}
    for term in voc:
        count_contining_term=0
        for doc in docs:
            if term in doc:
                count_contining_term+=1
                krishna[term]=math.log10(N/count_contining_term)
                krishna_weights=[]
                for doc in docs:
                    doc_weights    =()
                    for in doc:
                        tf=doc.count(term)/len(doc)
                        idf=krishna[term]
                    doc_weights[term]=tf*idf
                    krishna_weights.append(doc_weights)
                    return krishna_weights
            
"""
Example of two iterations in one Dumbo program:

>>> import dumbo
>>> opts = [('input','brian.txt'),('output','counts.txt')]
>>> logfile = open('log.txt','a')
>>> dumbo.start('itertwice.py',opts,stdout=logfile,stderr=logfile)
0
>>> output = dict(dumbo.loadcode(open('counts.txt')))
>>> int(output['e'])
14
"""

def mapper1(key,value):
    for word in value.split(): yield word,1

def mapper2(key,value):
    for letter in key: yield letter,1

def reducer1(key,values):
    count = sum(values)
    if count > 1: yield key,count

def reducer2(key,values):
    yield key,sum(values)

if __name__ == "__main__":
    import dumbo
    job = dumbo.Job()
    job.additer(mapper1,reducer1,reducer2)
    job.additer(mapper2,reducer2,reducer2)
    job.run()

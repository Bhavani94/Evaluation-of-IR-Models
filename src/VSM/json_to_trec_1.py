# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:47:48 2015

@author: ruhansa
"""
import json
# if you are using python 3, you should 
import urllib 
import urllib2

iteration=0

f = open('/home/dnyanada/newqueries.txt','r')
for line in f.readlines():
    
    #process queries one by one--------------------------------
    iteration=iteration+1
    query=''
    words=line.split()
    qid= words[0]
    
    dismaxargs=''
    deftype=''
    model='partb'
    opfile='Submit_Results/VSM/'
    
    """
    #Change1 results------------------------------------------------
    deftype='defType=dismax&'
    langhint=words[1].split(':')
    lang=langhint[1]
    
    
    
    
    #print qid
    #print lang
    if lang=="en":
        dismaxargs='&qf=text_en^2+text_de^0.5+text_ru^0.5'
    
    if lang=="de":
        dismaxargs='&qf=text_de^2+text_en^0.5+text_ru^0.5'

    if lang=="ru":
        dismaxargs='&qf=text_ru^2+text_de^0.5+text_en^0.5'
    
    
    #change1 ends--------------------------------------------------
    
    """
    """
    #Change2 results-hAshtags -----------------------------------------------
    deftype='defType=dismax&'
    langhint=words[1].split(':')
    lang=langhint[1]
    
    
    
    
    #print qid
    #print lang
    if lang=="en":
        dismaxargs='&qf=tweet_hashtags^4+text_en^2+text_de^0.5+text_ru^0.5'
    
    if lang=="de":
        dismaxargs='&qf=tweet_hashtags^4+text_de^2&qf=text_en^0.5+text_ru^0.5'

    if lang=="ru":
        dismaxargs='&qf=tweet_hashtags^4+text_ru^2+text_de^0.5+text_en^0.5'
    
    
    #change2 ends--------------------------------------------------
    """
    for word in words[2:]:
        query= query+word+' '
    
    
    query=query[:-1]
    
    query_args= {'q':query}
    encoded_args = urllib.urlencode(query_args)
    #print encoded_args
    
    #original code------------------------------------------------
# change the url according to your own koding username and query
    inurl = 'http://localhost:8983/solr/'+model+'/select?'+deftype+encoded_args+dismaxargs+'&fl=id%2Cscore&wt=json&indent=true&rows=1000'
    outfn = '/home/dnyanada/'+opfile+str(iteration)+'.txt'


# change query id and IRModel name accordingly
    
    IRModel='default'
    outf = open(outfn, 'a+')
    data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
# data = urllib.request.urlopen(inurl)

    docs = json.load(data)['response']['docs']
# the ranking should start from 1 and increase
    rank = 1
    for doc in docs:
        outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
        rank += 1
    outf.close()

    
    
f.close()

"""    
# change the url according to your own koding username and query
    inurl = 'http://localhost:8983/solr/irproj/select?q=Russia%27s+intervention+in+Syria&fl=id%2Cscore&wt=json&indent=true&rows=10'
    outfn = '/home/dnyanada/testTREC.txt'


# change query id and IRModel name accordingly
    qid = ''
    IRModel='default'
    outf = open(outfn, 'a+')
    data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
# data = urllib.request.urlopen(inurl)

    docs = json.load(data)['response']['docs']
# the ranking should start from 1 and increase
    rank = 1
    for doc in docs:
        outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
        rank += 1
    outf.close()
"""
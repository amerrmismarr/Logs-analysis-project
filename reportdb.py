import psycopg2



query1 = ''' select articles.title , count(*) as sum
 from articles join log
 on log.path = concat('/article/', articles.slug )
 group by articles.title
 order by sum desc
 limit 3;'''

query2 = ''' select author_with_slug.name, count(*) as views
 from log, author_with_slug 
 where log.path = concat('/article/', author_with_slug.slug) 
 group by author_with_slug.name
 order by views desc; '''

query3 = ''' 
select errors.day, round(100* errors.sum/total.totalnum,2) as percentage 
from errors, total 
where errors.day = total.day
and 100*errors.sum/total.totalnum  > 1;

'''


def executeQuery1(query):    

    conn = psycopg2.connect(database = "news")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print('\n What are the most popular three articles of all time?\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

    conn.close()

def executeQuery2(query):    

    conn = psycopg2.connect(database = "news")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print('\n Who are the most popular article authors of all time?\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

    conn.close()

def executeQuery3(query):    

    conn = psycopg2.connect(database = "news")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print('\n On which days did more than 1% of requests lead to errors?\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) )
        print(" ")

    conn.close()
    


executeQuery1(query1)
executeQuery2(query2)
executeQuery3(query3)

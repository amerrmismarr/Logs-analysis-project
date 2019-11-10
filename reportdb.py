#!/usr/bin/env python3

# Import postgresql library
import psycopg2


# query for question 1
query1 = '''SELECT articles.title,count(*) as sum
FROM articles join log
ON log.path = concat('/article/', articles.slug)
GROUP BY articles.title
ORDER BY sum desc
LIMIT 3;
'''

# Check the views for question 2 and 3 in the Readme.md file

# query for question 2
query2 = '''SELECT author_with_slug.name, count(*) as views
FROM log, author_with_slug
WHERE log.path = concat('/article/', author_with_slug.slug)
GROUP BY author_with_slug.name
ORDER BY views desc;
'''

# query for question 3
query3 = '''SELECT errors.day, round(100.0* errors.sum/total.totalnum,2)
AS percentage
FROM errors, total
WHERE errors.day = total.day
AND 100.0*errors.sum/total.totalnum  > 1;
'''


def executeQuery(query):
    """
    execute_query returns the results of an SQL query.

    execute_query takes an SQL query as a parameter,
    executes the query and returns the results as a list of tuples.
    args:
    query - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def print_favourite_articles():
    results = executeQuery(query1)
    print('\n Who are the most popular article authors of all time?\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")


def print_popular_authors():
    results = executeQuery(query2)
    print('\n Who are the most popular article authors of all time?\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")


def print_errors():
    results = executeQuery(query3)
    print('\n On which days did more than 1% of requests lead to errors?\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' % ' + 'errors')
        print(" ")


print_favourite_articles()
print_popular_authors()
print_errors()


def main():
    """Generate report."""
    executeQuery(query1)
    executeQuery(query2)
    executeQuery(query3)


if __name__ == '__main__':
    main()

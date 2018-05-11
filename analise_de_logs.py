# encoding: utf-8

import psycopg2

title1 = "1. Quais são os três artigos mais populares de todos os tempos?"

title2 = "2. Quem são os autores de artigos mais populares de todos os tempos?"

title3 = "3. Em quais dias mais de 1% das requisições resultaram em erros?"

query_1 = (
    "select title, count(*) as views "
    "from articles join log on log.path = CONCAT('/article/',articles.slug) "
    "group by title order by views desc limit 3")

query_2 = (
    "select name, sum(views) as total_views from authors "
    "join (  select author, title, count(*) as views "
    "from articles join log on log.path = CONCAT('/article/',slug) "
    "group by title, author) as most_popular "
    "on most_popular.author = authors.id "
    "group by name order by total_views desc;")

query_3 = (
    "select ok.dia as dia, "
    "(cast(conta_nok as float)/cast(conta_ok as float)) as pct "
    "from (  select date_trunc('day', time) as dia, count(*) as CONTA_OK "
    "from log where status like '%200%' group by dia) as ok "
    "join (  select date_trunc('day', time) as dia, count(*) as CONTA_NOK "
    "from log where status like '%404%' group by dia) as nok "
    "on ok.dia = nok.dia "
    "where (cast(conta_nok as float)/cast(conta_ok as float)) > 0.01 "
    "order by pct desc;")


def get_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


db = psycopg2.connect(database="news")
c = db.cursor()

print(title1 + '\n')
query_result = get_query(c, query_1)
for result in query_result:
    print('\t' + str(result[0]) + " -- " + str(result[1]) + " views")

print('\n' + title2 + '\n')
query_result = get_query(c, query_2)
for result in query_result:
    print('\t' + str(result[0]) + " -- " + str(result[1]) + " views")

print('\n' + title3 + '\n')
query_result = get_query(c, query_3)
for result in query_result:
    print('\t' + result[0].strftime("%B %d, %Y:") +
          " -- " + "{0:.2f}".format(result[1]*100) + "% errors")

db.close

create view author_with_slug as select authors.name, articles.slug from articles, authors where articles.author = authors.id;

create view total as select cast(time as date) as day, count(*) as totalnum from log group by day;

create view errors as select cast(time as date) as day, count(*) as sum from log where status = '404 NOT FOUND' group by day;

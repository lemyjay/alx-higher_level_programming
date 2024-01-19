--  A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT ts.title, tg.name
FROM tv_genres AS tg 
JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
RIGHT JOIN tv_shows AS ts ON ts.id = tsg.show_id
ORDER BY ts.title ASC, tg.name ASC;

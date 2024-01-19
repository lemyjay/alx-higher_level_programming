-- A script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT ts.title, COALESCE(tsg.genre_id, 'NULL') AS genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
ORDER BY ts.title ASC, genre_id ASC;

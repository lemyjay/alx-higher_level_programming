--  A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tg.name
FROM tv_genres AS tg, tv_show_genres AS tsg, tv_shows AS ts
WHERE ts.title = 'Dexter' AND ts.id = tsg.show_id AND tg.id = tsg.genre_id
ORDER BY tg.name ASC;

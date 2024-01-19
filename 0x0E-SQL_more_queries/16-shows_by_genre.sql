--  A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT ts.title, tg.name
FROM tv_genres AS tg, tv_show_genres AS tsg, tv_shows AS ts
WHERE ts.id = tsg.show_id AND tg.id = tsg.genre_id
ORDER BY ts.title ASC, tg.name ASC;

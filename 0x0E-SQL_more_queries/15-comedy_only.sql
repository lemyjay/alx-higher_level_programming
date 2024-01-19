--  A script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT ts.title
FROM tv_genres AS tg, tv_show_genres AS tsg, tv_shows AS ts
WHERE tg.name = 'Comedy' AND ts.id = tsg.show_id AND tg.id = tsg.genre_id
ORDER BY ts.title ASC;

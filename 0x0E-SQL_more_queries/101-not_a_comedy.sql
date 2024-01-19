--  A script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (
	SELECT tsg.show_id
	FROM tv_genres AS tg, tv_show_genres AS tsg
	WHERE tg.name = 'Comedy' AND tsg.genre_id = tg.id
)
ORDER BY ts.title ASC;

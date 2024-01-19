--  A script that uses the hbtn_0d_tvshows database to lists all genres not linked to the show Dexter.
SELECT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN (
	SELECT tsg.genre_id
	FROM tv_shows AS ts, tv_show_genres AS tsg
	WHERE ts.title = 'Dexter' AND tsg.show_id = ts.id
)
ORDER BY tg.name ASC;

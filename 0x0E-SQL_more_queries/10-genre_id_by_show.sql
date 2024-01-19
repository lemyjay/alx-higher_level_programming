-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT ts.title, tsg.genre_id
FROM (
	(tv_genres AS tg JOIN tv_show_genres AS tsg ON tg.id AND tsg.genre_id)
	JOIN tv_shows AS ts ON ts.id AND tsg.show_id
)
WHERE tg.id = tsg.genre_id AND tsg.show_id = ts.id
ORDER BY ts.title ASC, tsg.genre_id ASC;

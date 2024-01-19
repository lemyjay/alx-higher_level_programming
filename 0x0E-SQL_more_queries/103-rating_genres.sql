--  A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_genres tg, tv_show_genres tsg, tv_show_ratings tsr, tv_shows ts
WHERE tg.id = tsg.genre_id AND tsg.show_id = ts.id AND ts.id = tsr.show_id
GROUP BY tg.id
ORDER BY rating DESC;

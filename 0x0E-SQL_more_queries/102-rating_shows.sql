--  A script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT ts.title, SUM(tsr.rate) AS rating
FROM tv_show_ratings tsr, tv_shows ts
WHERE ts.id = tsr.show_id
GROUP BY ts.id
ORDER BY rating DESC;

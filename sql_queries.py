get_actors = """
SELECT 
    actors.id, 
    actors.name, 
    title, 
    CASE 
        WHEN on_tour = 0 THEN 'В театре'
        WHEN on_tour = 1 THEN 'В отъезде'
    END AS on_tour_status,
    gender,
    age,
    voice_type,
    height,
    directors.name,
    start_date,
    salary
FROM 
    actors
LEFT JOIN 
    directors ON actors.director_id = directors.id
"""

get_musicians = """
SELECT 
    musicians.id, 
    musicians.name, 
    role, 
    CASE 
        WHEN on_tour = 0 THEN 'В театре'
        WHEN on_tour = 1 THEN 'В отъезде'
    END AS on_tour_status,
    instruments.name,
    directors.name,
    start_date,
    age,
    salary
FROM 
    musicians
LEFT JOIN 
    instruments ON musicians.instrument_id = instruments.id
LEFT JOIN 
    directors ON musicians.director_id = directors.id
"""

get_producers = """
SELECT 
    producers.id, 
    producers.name, 
    CASE 
        WHEN on_tour = 0 THEN 'В театре'
        WHEN on_tour = 1 THEN 'В отъезде'
    END AS on_tour_status,
    total_played,
    producer_targets.name,
    directors.name,
    start_date,
    age,
    salary
FROM 
    producers
LEFT JOIN 
    producer_targets ON producers.target_id = producer_targets.id
LEFT JOIN 
    directors ON producers.director_id = directors.id
"""

get_staffs = """
SELECT 
    staffs.id, 
    staffs.name, 
    CASE 
        WHEN on_tour = 0 THEN 'В театре'
        WHEN on_tour = 1 THEN 'В отъезде'
    END AS on_tour_status,
    staff_positions.name,
    directors.name,
    start_date,
    age,
    salary
FROM 
    staffs
LEFT JOIN 
    staff_positions ON staffs.position_id = staff_positions.id
LEFT JOIN 
    directors ON staffs.director_id = directors.id
"""

get_shows = """SELECT 
    p.id,
    p.title AS performance_title,
    a.name AS author_name,
    g.name AS genre_name
FROM 
    perfomances p
JOIN 
    authors a ON p.author_id = a.id
JOIN 
    genres g ON p.genre_id = g.id;
ORDER BY
    p.id;
"""

get_schedule = """SELECT 
    p.id,
    p.title AS performance_title,
    p.date AS performance_date,
    a.name AS author_name,
    g.name AS genre_name,
    pr.name AS producer_name,
    p.total_seats AS total_seats_count
FROM 
    perfomances p
JOIN 
    authors a ON p.author_id = a.id
JOIN 
    genres g ON p.genre_id = g.id
JOIN
    producers pr ON p.producer_id = pr.id
GROUP BY
    p.id, p.title, p.date, a.name, g.name, pr.name, p.total_seats
ORDER BY
    p.date;
"""
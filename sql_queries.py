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
    directors.name
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
    directors.name
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
    directors.name
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
    directors.name
FROM 
    staffs
LEFT JOIN 
    staff_positions ON staffs.position_id = staff_positions.id
LEFT JOIN 
    directors ON staffs.director_id = directors.id
"""
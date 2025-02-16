USE ig_clone;
SHOW TABLES;
DESC comments;
DESC `follows`;
DESC likes;
DESC photo_tags;
DESC photos;
DESC tags;
DESC users;

-- A Task1
SELECT username
FROM users
ORDER BY created_at ASC
LIMIT 5;

-- A Task2
SELECT u.id,u.username
FROM users u
LEFT JOIN photos p ON u.id = p.user_id
WHERE p.id IS NULL;

-- A Task3
SELECT u.id as user_id,u.username,p.id as photo_id,COUNT(l.user_id) as likes
FROM users u
JOIN photos p ON u.id = p.user_id
JOIN likes l ON p.id = l.photo_id
GROUP BY p.id
ORDER BY COUNT(l.user_id) DESC
LIMIT 1;


SELECT p.id,COUNT(l.user_id)
FROM photos p
JOIN likes l ON p.id = l.photo_id
GROUP BY p.id 
ORDER BY COUNT(l.user_id) DESC;

-- A Task4
SELECT t.tag_name,COUNT(pt.photo_id) as use_count
FROM tags t
JOIN photo_tags pt ON t.id = pt.tag_id
GROUP BY t.id
ORDER BY COUNT(pt.photo_id) DESC
LIMIT 5;

-- A Task5
SELECT dayname(created_at) as `day`,COUNT(u.id) as users_registered
FROM users u
GROUP BY dayname(created_at);

-- B Task1
SELECT u.id,u.username,AVG(posts) as avg_posts
FROM users u,
(SELECT u.id,COUNT(p.id) as posts FROM users u JOIN photos p ON u.id = p.user_id GROUP BY u.id) as sq1
GROUP BY u.id;

-- B Task2
SELECT u.id,u.username,COUNT(l.photo_id) as photos_liked
FROM users u 
JOIN likes l ON u.id = l.user_id
GROUP BY u.id
ORDER BY COUNT(l.photo_id) DESC;

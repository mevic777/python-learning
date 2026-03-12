select * from votes;

select * from posts;
select * from users;

-- select p.id as post_id, p.title as post_title, u.email as user_email, count(*)
--        from votes v
--        inner join users u
-- 	   on v.user_id = u.id
-- 	   inner join posts p
-- 	   on p.user_id = v.user_id
-- 	   where v.user_id = 13
-- 	   group by p.id, p.title, u.email;

-- select posts.id, posts.title, posts.content, STRING_AGG(users.email, ', ' ORDER BY users.email) AS user_emails, count(votes.post_id) as votes from votes
-- 	   inner join posts
-- 	   on posts.id = votes.post_id
-- 	   inner join users
-- 	   on users.id = votes.user_id
-- 	   group by posts.id, posts.title, posts.content;

select posts.*, count(votes.post_id) as votes from posts 
                left join votes on posts.id = votes.post_id 
				group by posts.id order by posts.id;


use udemy;

alter table priyaprem08 drop _class;
alter table priyadharshini170898 drop _class;
alter table priyadharshini221099 drop _class;

alter table priyaprem08 add primary key(id);
alter table priyadharshini170898 add primary key(id);
alter table priyadharshini221099 add primary key(id);

alter table udemy_course add time_number float;

alter table udemy_course add time_unit varchar(10);

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = N'udemy_course';

alter table course_time add user int;

select id, content_info from priyaprem08;

select id, content_info from priyadharshini170898;

select id, content_info from priyadharshini221099;

ALTER TABLE course_time ADD duration varchar(20) AFTER id;

alter table course_time drop primary key;

alter table course_time drop id;

select ct.id, ct.duration, ct.time, ct.units, ct.user, 
ifnull(user1.title, ifnull(user2.title, user3.title)) as title, 
ifnull(user1.is_paid, ifnull(user2.is_paid, user3.is_paid)) as paid,
ifnull(user1.price, ifnull(user2.price, user3.price)) as price,
ifnull(user1.rating, ifnull(user2.rating, user3.rating)) as rating,
ifnull(user1.num_reviews, ifnull(user2.num_reviews, user3.num_reviews)) as num_reviews from course_time ct
left join priyaprem08 user1 on ct.id = user1.id
left join priyadharshini170898 user2 on ct.id = user2.id
left join priyadharshini221099 user3 on ct.id = user3.id;


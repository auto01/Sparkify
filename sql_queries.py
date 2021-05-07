
# Drop tables ----------------------------------

songplays_table_drop="DROP TABLE IF EXISTS songplays"
users_table_drop="DROP TABLE IF EXISTS users"
songs_table_drop="DROP TABLE IF EXISTS songs"
artists_table_drop="DROP TABLE IF EXISTS artists"
time_table_drop="DROP TABLE IF EXISTS time"

# Create tables ---------------------------------

####### Dimension tables
users_table_create=("""
CREATE TABLE IF NOT EXISTS users 
(
user_id varchar(255),
first_name varchar(255) not null,
last_name varchar(255) not null, 
gender char(1) not null,
level varchar(30) not null,
primary key(user_id)
);
""")

songs_table_create=("""
CREATE TABLE IF NOT EXISTS songs
(
song_id varchar(255),
title text not null,
artist_id varchar(255) not null,
year int not null,
duration float not null,
primary key(song_id)
);
""")
artists_table_create=("""
CREATE TABLE IF NOT EXISTS artists
(
artist_id varchar(255),
name varchar(255) not null,
location text not null,
latitude text,
longitude text,
primary key(artist_id)
);
""")

time_table_create=("""
CREATE TABLE IF NOT EXISTS time
(
start_time timestamp,
hour int not null,
day int not null,
week int not null,
month int not null,
year int not null,
weekday int not null,
primary key(start_time)
);
""")

####### Fact tables


songplays_table_create=("""
CREATE TABLE IF NOT EXISTS songplays
(
songplay_id serial,
start_time timestamp,
user_id varchar(255) references users(user_id), 
level varchar(30),
song_id varchar(255) references songs(song_id),
artist_id varchar(255) references artists(artist_id), 
session_id int, 
location text,
user_agent text,
primary key(songplay_id)
);
""")

# song_select to extract song_id and artist_id
song_select=("""select s.song_id,a.artist_id from songs s join artists a 
on s.artist_id=a.artist_id 
where s.title=%s and a.name=%s and s.duration=%s""")


# select head records ---------------------------
songplays_head="select *from songplays limit 5"
users_head="select *from users limit 5"
songs_head="select *from songs limit 5"
artists_head="select *from artists limit 5"
time_head="select * from time limit 5"

# insert into tables ----------------------------
songplay_table_insert=("""
insert into songplays
(
start_time,
user_id, 
level,
song_id, 
artist_id,
session_id,
location,
user_agent
)
values(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert=("""
insert into users
(
user_id,
first_name, 
last_name,
gender, 
level
) 
values(%s,%s,%s,%s,%s) on conflict(user_id) do 
update set level=excluded.level
""")

song_table_insert=("""
insert into songs
(
song_id,
title,
artist_id,
year,
duration
)
values(%s,%s,%s,%s,%s) on conflict do nothing
""")

artist_table_insert=("""
insert into artists
(
artist_id,
name, 
location,
latitude,
longitude
) 
values(%s,%s,%s,%s,%s) on conflict do nothing
""")

time_table_insert=("""
insert into time
(
start_time,
hour,
day,
week,
month,
year,
weekday
)
values(%s,%s,%s,%s,%s,%s,%s) on conflict do nothing
""")


# query list ------------------------------------

drop_query_list=[songplays_table_drop,users_table_drop,songs_table_drop,artists_table_drop,time_table_drop]
create_query_list=[users_table_create,songs_table_create,artists_table_create,time_table_create,songplays_table_create]
select_tables_head=[songplays_head,users_head,songs_head,artists_head,time_head]

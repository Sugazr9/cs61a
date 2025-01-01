.read sp16data.sql
.read fa15data.sql

-- Q2
CREATE TABLE obedience AS
  select seven, hilfinger from students;

-- Q3
CREATE TABLE smallest_int AS
  select time, smallest from students where smallest > 12 order by smallest limit 20;

-- Q4
CREATE TABLE greatstudents AS
  select a.date, b.number, b.pet, a.color, b.color from students as a, fa15students as b where b.date = a.date and b.pet = a.pet and a.number = b.number;

-- Q5
CREATE TABLE matchmaker AS
  select a.pet, b.song, a.color, b.color from students as a, students as b where a.pet = b.pet and a.song = b.song and a.time < b.time;

-- Q6
CREATE TABLE fa15favnum AS
  SELECT number, count(*) as count from fa15students group by number order by count desc limit 1;

CREATE TABLE fa15favpets AS
  SELECT pet, count(*) as count from fa15students group by pet order by count desc limit 10;

CREATE TABLE sp16favpets AS
  SELECT pet, count(*) as count from students group by pet order by count desc limit 10;

CREATE TABLE sp16dragon AS
  SELECT pet, count(*) from students where pet = "dragon";

CREATE TABLE sp16alldragons AS
  SELECT pet, count(*) from students where pet like '%dragon%';

CREATE TABLE obedienceimage AS
  SELECT seven, hilfinger, count(*) from students where seven = '7' group by hilfinger;

-- Q7
CREATE TABLE pairs AS
    with
      naturals(n) as (
        select 0 union
        select n+1 from naturals where n < 42
        )
  select a.n as x, b.n  as y from naturals as a, naturals as b where a.n <= b.n;


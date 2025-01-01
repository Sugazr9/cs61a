create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select name, size from dogs, sizes where height > min and height <= max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select child from dogs, parents where name = parent order by height desc;

-- Sentences about siblings that are the same size
create table sentences as
  with siblings(n, m) as (
    select a.child, b.child from parents as a, parents as b where a.parent=b.parent and a.child < b.child)
  select n || " and " || m ||" are " || a.size || " siblings" from siblings, size_of_dogs as a, size_of_dogs as b
  where n = a.name and m = b.name and a.size = b.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with intermediate(stack_dogs, last_dog, count_dogs, total) as (
    select name, height, 1, height from dogs union
    select stack_dogs || ", " || name, height, count_dogs + 1, total + height from dogs, intermediate
    where height > last_dog and count_dogs < 4
    )
  select stack_dogs, total from intermediate where total >= 170 order by total;

-- Heights and names of dogs that are above average in height among
-- dogs whose height has the same first digit.
create table above_average as
  with numbers(height, average) as (
    select (height- (height %10)), avg(height) from dogs group by (height - (height % 10))
    )
  select a.height, name from dogs as a, numbers as b where (a.height - (a.height % 10)) = b.height and a.height> average;
-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

-- Question 1: Composites --
create table composites as
  select distinct d.n as c from ints as a, ints as b, ints as d where a.n*b.n = d.n and a.n != 1 and b.n != 1;

create table multiples as
  select c as m from composites union all select n from ints;

-- Question 2: Primes --
create table primes as
  select m as p from multiples where m > 1 group by m having count(*) = 1;


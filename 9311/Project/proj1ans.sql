-- comp9311 19s1 Project 1
--
-- MyMyUNSW Solutions


--z5193712

-- CHMOD


-- Q1:
create or replace view Findcourseid(courseid)
as
select id
from courses
where subject in (
-- find the id of COMP9311
select id 
from subjects
where code = 'COMP9311')
and semester = (
select id 
from semesters
where year = '2013' and term='S1');


create or replace view Q1(unswid, longname)
as
select unswid,longname 
from rooms 
where id in(select room
from classes
where course in (select courseid from Findcourseid))
and rtype in (select id
from room_types 
where description='Laboratory');


-- Q2:
create or replace view Findcourseheenroll(course)
as
select course 
from course_enrolments
where student = (
select id
from people
where name =  'Bich Rae'
);

create or replace view Q2(unswid,name)
as
select unswid,name
from people
where id in (select staff from course_staff
where  course in (select course from Findcourseheenroll));

-- Q3:
create or replace view Comp9311(sid,code,semester)
as
select distinct students.id,code,semester
from students,semesters,subjects,courses,course_enrolments
where stype='intl' 
and semesters.id =courses.semester
and courses.subject = subjects.id
and subjects.code = 'COMP9311'
and students.id = course_enrolments.student
and course_enrolments.course = courses.id;

create or replace view Comp9021(sid,code,semester)
as
select distinct students.id,code,semester
from students,semesters,subjects,courses,course_enrolments
where stype='intl' 
and semesters.id =courses.semester
and courses.subject = subjects.id
and subjects.code = 'COMP9021'
and students.id = course_enrolments.student
and course_enrolments.course = courses.id; 

create or replace view Q3_1(sid)
as
select distinct Comp9311.sid from Comp9021,Comp9311
where Comp9311.semester=Comp9021.semester
and Comp9311.sid = Comp9021.sid;

create or replace view Q3(unswid, name)
as 
select distinct unswid,name from people,Q3_1
where Q3_1.sid = people.id;



-- Q4:

create or replace view Countstudents(program, total_students)
as
select program,count(distinct student)
from Program_enrolments 
group by program;

create or replace view Countintelstudents(program, total_intelstudents)
as
select program,count(distinct student)
from Program_enrolments 
where student in (
select id from students
where stype='intl')
group by program;

create or replace view percentage(program, percent)
as
select Countintelstudents.program, (Countintelstudents.total_intelstudents/(1.0*Countstudents.total_students))*100
from Countintelstudents, Countstudents
where Countintelstudents.program=Countstudents.program;


create or replace view Q4(code,name)
as
select distinct code, name from programs
where id in (select program from percentage
where percent>=30 and percent<=70);


--Q5:

create or replace view Mincourse(course,minmark)
as
select course,min(mark)
from Course_enrolments
where mark is not null
group by course
having count(mark is not null)>=20;

create or replace view Maxofmincourse(course)
as
select course from Mincourse where
minmark = (select max(minmark) 
from Mincourse);

create or replace view Courseandse(subject,semester)
as
select subject, semester 
from courses
where id in (select course 
from Maxofmincourse);


create or replace view Q5(code,name,semester)
as
select code,subjects.name,semesters.name
from subjects,semesters
where subjects.id in (select subject 
from Courseandse)
and semesters.id in (
select semester from Courseandse);


-- Q6:

create or replace view Chemistry(student)
as
select student
from Program_enrolments
where id in(
select partOf from Stream_enrolments
	where stream in(
	select id from Streams
	where name = 'Chemistry'))
and semester in (
select id from semesters
where year = 2010 and term ='S1')
and student in(
select id from Students
where stype='local');

create or replace view Engineering(student)
as
select student
from Program_enrolments
where semester in (
select id from semesters
where year = 2010 and term ='S1')
and student in(
select id from Students
where stype='intl')
and program in(
select id from programs
where offeredby in (
select id from orgunits 
where name ='Faculty of Engineering'));


create or replace view Cs(student)
as
select student
from Program_enrolments
where semester in (
select id from semesters
where year = 2010 and term ='S1')
and program in(
select id from programs
where code='3978');

create or replace view Countone(num1)
as
select count(distinct student) as num1 from Chemistry;

create or replace view Counttwo(num2)
as
select count(distinct student) as num2 from Engineering;

create or replace view Countthree(num3)
as
select count(distinct student) as num3 from Cs;

create or replace view Q6(num1, num2, num3)
as
select num1,num2,num3 from Countone,Counttwo,Countthree;



-- Q7:


create or replace view Q7_1(staff,numberofcourse)
as
select distinct staff,count(distinct subjects.code) from course_staff,subjects,courses
where courses.id =course_staff.course
and 
subjects.id = courses.subject
group by staff
having count(distinct subjects.code)>=1;

create or replace view Q7_2(staff,starting,orgunit)
as
select distinct staff,starting,orgunit from affiliations
where role in(
select id from Staff_roles
where name = 'Dean')
and orgunit in(
select id from Orgunits
where utype in(
select id from Orgunit_types
where name='Faculty'))
and isprimary='t';

create or replace view Allstaff(staff)
as
select Q7_2.staff from Q7_2,Q7_1
where Q7_2.staff=Q7_1.staff;


create or replace view Q7(name, school, email, starting, num_subjects)
as
select people.name,longname,people.email,Q7_2.starting ,numberofcourse from Allstaff,people,Q7_2,orgunits,Q7_1
where people.id = Allstaff.staff
and Q7_2.staff = Allstaff.staff
and Q7_2.orgunit = orgunits.id
and Q7_1.staff = Allstaff.staff;


-- Q8: 

create or replace view Courseandnum(course,num)
as
select course,count(distinct student) as num from course_enrolments
group by course
having count(distinct student)>=20;

create or replace view Q8_1(subject)
as
select subject from courses,Courseandnum
where Courseandnum.course=courses.id
group by subject
having count(course)>=20;

create or replace view Q8(subject)
as
select code||' '||name as subject
from subjects,Q8_1
where Q8_1.subject = subjects.id;



-- Q9:




create or replace view Q9_2(num,year,unit)
as
select count(distinct student),year,orgunits.id
from program_enrolments,semesters,students,orgunits,programs
where program_enrolments.semester = semesters.id
and programs.offeredby = Orgunits.id
and programs.id = program_enrolments.program
and program_enrolments.student = students.id
and students.stype='intl'
group by orgunits.id,year
order by year,orgunits.id;




create or replace view Q9_3(sum,year,unit)
as
select * from
(select *,rank() over (partition by unit order by num desc) rank
from Q9_2) as a
where rank=1;


create or replace view Q9(year,num,unit)
as
select year,sum,longname
from Q9_3,Orgunits
where orgunits.id=Q9_3.unit;


-- Q10:

create or replace view studentandavg(student,avgmark)
as
select student,avg(mark)::numeric(4,2) from course_enrolments
where course in (
	select id from courses
	where semester =(
	select id from semesters
	where year = 2011 and term='S1'))
and course_enrolments.mark >= 0
group by student
having count(course)>=3
order by avg(mark) desc;

create or replace view studentandrank(student,avgmark,ra)
as
select student,avgmark,rank() over
(order by avgmark desc ) as ra
from studentandavg;


create or replace view Q10(unswid,name,avg_mark)
as
select unswid,name,avgmark from studentandrank,people
where people.id = studentandrank.student
and ra>=1 and ra <=10;

-- Q11:


create or replace view studentAndcourse(student,course,mark)
as
select student,course,mark from course_enrolments
where student in(
select id
from people
where (unswid /10000) =313)
and course in(
select id from courses
where semester =(
select id from semesters
where year = 2011 and term='S1'))
and mark>=0
order by student;


create or replace view passornot(student,course,passornot)
as
select student,course,
(case when mark>50 then 1 else 0 end) as passornot
from studentAndcourse
group by student,mark,course
order by student;


create or replace view numpass(student,numofpass)
as
select student,count(passornot) as numofpass
from passornot
where passornot=1
group by student;


create or replace view numnotpass(student,numofnotpass)
as
select student,count(passornot) as numofnotpass
from passornot
where passornot=0
group by student;

create or replace view Q11_1(student1,numofpass,student2,numofnotpass)
as
select * from
numpass full join numnotpass
on numpass.student = numnotpass.student;


create or replace view Q11_2(student,standing)
as
select case when student1 is not null then student1 else student2 end,
(case when student2 is null then 'Good' else (
case when student1 is null and numofnotpass<=1 then 'Referral' else (
case when student1 is null and numofnotpass>1 then 'Probation' else(
case when numofpass<=numofnotpass then 'Referral' else 'Good' end)end )end)end) as standing
from Q11_1;


select case when student1 is not null then student1 else student2 end,
(case when student2 is null then 'Good' else (
case when student1 is null then 'Probation' else (
case when numofpass<=numofnotpass then 'Referral' else 'Good' end)end )end) as standing
from Q11_1;




create or replace view Q11(unswid, name, academic_standing)
as
select unswid,name,standing
from people,Q11_2
where Q11_2.student=people.id;



-- Q12:

create or replace view subjectid(subject)
as
select id from subjects
where code like 'COMP90%';


create or replace view yearandterm(year,term)
as
select distinct year,term from semesters
where year between 2003 and 2012
and (term='S1' or term ='S2')
order by year;

create or replace view Subdivide(subject)
as
select distinct subject from courses Sub1
where not exists(
select * from yearandterm 
	where not exists(
	select * from courses,semesters 
	where courses.semester = semesters.id
	and semesters.year = yearandterm.year
	and semesters.term = yearandterm.term
	and courses.subject = Sub1.subject));


create or replace view Finalsub(subject)
as
select subject from Subdivide
intersect
select subject from subjectid;


create or replace view pass(code,name,numberofpass,year,term)
as
select subjects.code,subjects.name,count(mark),year,term
from subjects,Finalsub,course_enrolments,courses,semesters
where subjects.id = Finalsub.subject
and course_enrolments.course=courses.id
and courses.subject=subjects.id
and courses.semester=semesters.id
and mark>=50
group by course_enrolments.course,subjects.code,subjects.name,year,term
order by code,year,term;



create or replace view recievemark(code,name,numofrecievemark,year,term)
as
select subjects.code,subjects.name,count(mark),year,term
from subjects,Finalsub,course_enrolments,courses,semesters
where subjects.id = Finalsub.subject
and course_enrolments.course=courses.id
and courses.subject=subjects.id
and courses.semester=semesters.id
and mark>=0
group by course_enrolments.course,subjects.code,subjects.name,year,term
order by code,year,term;



create or replace view Q12_1(code,name,rate,year,term)
as
select recievemark.code,recievemark.name, 
case when pass.numberofpass>=0 then pass.numberofpass/(recievemark.numofrecievemark*1.0) 
else 0/(recievemark.numofrecievemark*1.0)end,
recievemark.year,recievemark.term
from recievemark left join
pass on recievemark.code=pass.code
and recievemark.year=pass.year
and recievemark.term=pass.term;


create or replace view Q12_2(code,name,rate,year,term)
as
select recievemark.code,recievemark.name, 
case when pass.numberofpass>=0 then pass.numberofpass/(recievemark.numofrecievemark*1.0) 
else 0/(recievemark.numofrecievemark*1.0)end,
recievemark.year,recievemark.term
from recievemark left join
pass on recievemark.code=pass.code
and recievemark.year=pass.year
and recievemark.term=pass.term;



create or replace view Q12s1(code,name,rate,year,term)
as
select code,name,rate::numeric(4,2),year,term
from Q12_1
where term = 'S1';

create or replace view Q12s2(code,name,rate,year,term)
as
select code,name,rate::numeric(4,2),year,term
from Q12_1
where term = 'S2';

create or replace view Q12_11(code, name, year, s1_ps_rate, s2_ps_rate)
as
select Q12s2.code,Q12s2.name,Q12s2.year,Q12s1.rate,Q12s2.rate
from Q12s2
left join 
Q12s1
on Q12s1.code = Q12s2.code
and  Q12s1.year=Q12s2.year
order by code,year;

create or replace view Q12_12(code, name, year, s1_ps_rate, s2_ps_rate)
as
select Q12s1.code,Q12s1.name,Q12s1.year,Q12s1.rate,Q12s2.rate
from Q12s1
left join 
Q12s2
on Q12s1.code = Q12s2.code
and  Q12s1.year=Q12s2.year
order by code,year;

create or replace view Q12_3(c1,n1,y1,s11,s21,c2,n2,y2,s12,s22)
as
select * from Q12_11 
full join Q12_12
on Q12_11.code = Q12_12.code
and Q12_11.year = Q12_12.year;

create or replace view Q12_final(code,name,year,s1rate,s2rate)
as
select case when c1 is null then c2
else c1 end,
case when n1 is null then n2
else n1 end,
case when y1 is null then y2
else y1 end, 
case when c1 is null then s12
else s11 end,
case when c1 is null then s22
else s21 end
from Q12_3;


--to_char(y2%100,'00') 
--substr(cast(semesters.year as varchar(5)),3,2)

create or replace view Q12(code, name, year, s1_ps_rate, s2_ps_rate)
as
select code,name, substr(cast(year as varchar(5)),3,2),
case when s1rate is null then null
else s1rate end,
case when s2rate is null then null
else s2rate end
from Q12_final;


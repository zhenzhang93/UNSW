-- comp9311 19s1 Project 1
--
-- MyMyUNSW Solutions


-- Q1:
CREATE OR REPLACE VIEW Q1(unswid, longname) 
AS
SELECT distinct r.unswid, r.longname
FROM Rooms r
JOIN Room_types rt ON r.rtype=rt.id
JOIN Classes cl ON cl.room=r.id
JOIN Courses c ON cl.course =c.id
JOIN Semesters s ON s.id = c.semester
JOIN Subjects sb ON c.subject=sb.id
WHERE rt.description='Laboratory'
  AND s.term='S1'
  AND s.year='2013'
  AND sb.code='COMP9311';


-- Q2:
CREATE OR REPLACE VIEW Q2(unswid,name) 
AS
SELECT DISTINCT p.unswid,
                p.name
FROM People p
JOIN Staff ON (Staff.id = p.id)
JOIN Course_staff ON (Course_staff.staff=Staff.id)
JOIN Courses ON (Courses.id=Course_staff.course)
JOIN Course_enrolments ON (Course_enrolments.course=Courses.id)
JOIN Students ON (Students.id=Course_enrolments.student)
WHERE Students.id =
    (SELECT id
     FROM People
     WHERE name='Bich Rae');


-- Q3:
-- INTERSECT CAN BE REPLACED BY JOIN
CREATE OR REPLACE VIEW Q3_sub(student, semester) 
AS
SELECT ce.student,
       c.semester
FROM course_enrolments AS ce,
     courses AS c,
     subjects AS s
WHERE ce.course = c.id
  AND c.subject = s.id
  AND s.code = 'COMP9311' 
INTERSECT
SELECT ce.student,
       c.semester
FROM course_enrolments AS ce,
     courses AS c,
     subjects AS s 
WHERE ce.course = c.id
  AND c.subject = s.id
  AND s.code = 'COMP9021';

CREATE OR REPLACE VIEW Q3(unswid, name) 
AS
SELECT DISTINCT p.unswid,
                p.name
FROM people AS p,
     Q3_sub AS q,
     students AS s
WHERE p.id = q.student
  AND q.student = s.id
  AND s.stype = 'intl';


-- Q4:
CREATE OR REPLACE VIEW program_all(id, alls) 
AS
SELECT pe.program,
       count(DISTINCT pe.student)
FROM program_enrolments pe
GROUP BY pe.program;

CREATE OR REPLACE VIEW program_intl(id, intl) 
AS
SELECT pe.program,
       count(DISTINCT s.id)
FROM program_enrolments pe
JOIN students s ON pe.student = s.id
WHERE s.stype = 'intl'
GROUP BY pe.program;

CREATE OR REPLACE VIEW Q4(code,name) 
AS
SELECT p.code,
       p.name
FROM programs p
JOIN program_all pa ON p.id = pa.id
JOIN program_intl pi ON p.id = pi.id
WHERE pi.intl::float / pa.alls::float >= 0.3
  AND pi.intl::float / pa.alls::float <= 0.7
GROUP BY p.id;


--Q5:
CREATE OR REPLACE VIEW valid_courses(course, min_mark) 
AS
SELECT course,
       min(mark) AS min_mark
FROM Course_enrolments enr
GROUP BY course 
HAVING sum(CASE WHEN mark IS NOT NULL THEN 1 ELSE 0 END)>= 20;

CREATE OR REPLACE VIEW Q5(code,name,semester) 
AS
SELECT sub.code,
       sub.name,
       sem.name AS semester
FROM valid_courses enr,
     Courses cour,
     Subjects sub,
     Semesters sem
WHERE min_mark =
    (SELECT max(min_mark)
     FROM valid_courses)
  AND enr.course = cour.id
  AND cour.subject = sub.id
  AND cour.semester = sem.id;


-- Q6:
CREATE OR REPLACE VIEW enrolInChemistry(studentId,semester) 
AS
SELECT program_enrolments.student AS studentId,
       program_enrolments.semester AS semester
FROM (program_enrolments
      INNER JOIN stream_enrolments ON program_enrolments.id = stream_enrolments.partof)
INNER JOIN streams ON stream_enrolments.stream = streams.id
INNER JOIN semesters ON semesters.id = program_enrolments.semester
WHERE streams.name = 'Chemistry'
  AND semesters.year = '2010'
  AND semesters.term = 'S1';


CREATE OR REPLACE VIEW Num1(num1) 
AS
SELECT count(DISTINCT(students.id))
FROM enrolInChemistry
INNER JOIN students ON enrolInChemistry.studentId = students.id
WHERE students.stype = 'local';


CREATE OR REPLACE VIEW enrolInEngineering(studentId,semester) 
AS
SELECT program_enrolments.student AS studentId,
       program_enrolments.semester AS semester
FROM orgunits
INNER JOIN programs ON programs.offeredby = orgunits.id
INNER JOIN program_enrolments ON programs.id = program_enrolments.program
INNER JOIN semesters ON semesters.id = program_enrolments.semester
WHERE orgunits.longname = 'Faculty of Engineering'
  AND semesters.year = '2010'
  AND semesters.term = 'S1';


CREATE OR REPLACE VIEW Num2(num2) 
AS
SELECT count(DISTINCT(students.id))
FROM enrolInEngineering
INNER JOIN students ON enrolInEngineering.studentId = students.id
WHERE students.stype = 'intl';


CREATE OR REPLACE VIEW Num3(num3) 
AS
SELECT count(DISTINCT(program_enrolments.student))
FROM (programs
      INNER JOIN program_enrolments ON programs.id = program_enrolments.program)
INNER JOIN semesters ON semesters.id = program_enrolments.semester
WHERE programs.code = '3978'
  AND semesters.year = '2010'
  AND semesters.term = 'S1';


CREATE OR REPLACE VIEW q6(num1, num2, num3) AS
SELECT n1.num1,
       n2.num2,
       n3.num3
FROM Num1 n1,
     Num2 n2,
     Num3 n3
WHERE 1=1;


-- Q7:
CREATE OR REPLACE VIEW Q7(name, school, email, starting, num_subjects) 
AS
SELECT p.name,
       o.longname,
       p.email,
       a.starting,
       count(DISTINCT (sb.code))
FROM People p
JOIN Staff s ON p.id= s.id
JOIN Affiliations a ON a.staff=s.id
JOIN OrgUnits o ON o.id=a.orgUnit
JOIN OrgUnit_types ot ON o.utype=ot.id
JOIN Staff_roles sr ON a.role=sr.id
JOIN Course_staff cs ON cs.staff=s.id
JOIN Courses c ON cs.course=c.id
JOIN Subjects sb ON c.subject=sb.id
WHERE sr.name='Dean'
  AND a.isPrimary
  AND ot.name='Faculty'
GROUP BY p.name,
         o.longname,
         p.email,
         a.starting;


-- Q8: 
CREATE OR REPLACE VIEW valid_course_enrol_sub(course_id,subject) 
AS
SELECT Cour_enr.course AS course_id,
       concat(sub.code, ' ', sub.name) AS subject
FROM Course_enrolments Cour_enr,
     Courses cour,
     Subjects sub
WHERE Cour_enr.course = cour.id
  AND cour.subject = sub.id
GROUP BY Cour_enr.course,
         concat(sub.code, ' ', sub.name) 
HAVING count(DISTINCT Cour_enr.student)>= 20;


CREATE OR REPLACE VIEW Q8(subject) 
AS
SELECT subject
FROM valid_course_enrol_sub sub
GROUP BY subject HAVING count(DISTINCT course_id) >=20;


-- Q9:
CREATE OR REPLACE VIEW Q9_sub1(student, TYPE, unit_id, YEAR) 
AS
SELECT st.id,
       st.stype,
       o.id,
       se.YEAR
FROM students st
JOIN program_enrolments pe ON st.id = pe.student
JOIN semesters se ON pe.semester = se.id
JOIN programs p ON pe.program = p.id
JOIN orgunits o ON p.offeredby = o.id;

CREATE OR REPLACE VIEW unit_intl(unit_id, YEAR, num_intl) 
AS
SELECT qs1.unit_id,
       qs1.YEAR,
           COUNT (DISTINCT qs1.student)
FROM Q9_sub1 qs1
WHERE qs1.TYPE = 'intl'
GROUP BY qs1.unit_id,
         qs1.YEAR;

CREATE OR REPLACE VIEW maxInl(unit_id, max_intl) 
AS
SELECT ui.unit_id,
       max(ui.num_intl)
FROM unit_intl ui
GROUP BY ui.unit_id;

CREATE OR REPLACE VIEW Q9(YEAR, num, unit) 
AS
SELECT ui.YEAR,
       ui.num_intl,
       o.longname
FROM orgunits o
JOIN unit_intl ui ON o.id = ui.unit_id
JOIN maxInl mi ON o.id = mi.unit_id
WHERE ui.num_intl = mi.max_intl;


-- Q10:
CREATE OR REPLACE VIEW valid_students(student) 
AS
SELECT ce.student
FROM course_enrolments ce
JOIN courses c ON ce.course = c.id
JOIN semesters s ON c.semester = s.id
WHERE s.term = 'S1'
  AND ce.mark >= 0
  AND s.YEAR = 2011
GROUP BY ce.student 
HAVING COUNT(ce.student) >= 3;

CREATE OR REPLACE VIEW stu_mark(student, mark) AS
SELECT ce.student,
       avg(ce.mark)
FROM course_enrolments ce
JOIN courses c ON ce.course = c.id
JOIN semesters s ON c.semester = s.id
WHERE ce.mark >= 0
  AND s.YEAR = 2011
  AND s.term = 'S1'
  AND ce.student IN
    (SELECT *
     FROM valid_students)
GROUP BY ce.student;

CREATE OR REPLACE VIEW cal_wam(student, avg_mark, rank) 
AS
SELECT sm.student,
       cast(sm.mark AS numeric(4, 2)),
       rank() over(
                   ORDER BY sm.mark DESC) AS rank
FROM stu_mark sm;

CREATE OR REPLACE VIEW Q10(unswid, name, avg_mark) 
AS
SELECT p.unswid,
       p.name,
       w.avg_mark
FROM people p
JOIN cal_wam w ON p.id = w.student
WHERE w.rank <= 10;


-- Q11:
CREATE OR REPLACE VIEW students_marks(student, sem, mark) 
AS
SELECT ce.student,
       s.term,
       ce.mark
FROM Course_enrolments ce
JOIN Courses c ON ce.course = c.id
JOIN Semesters s ON c.semester = s.id
WHERE s.YEAR = 2011
  AND s.term = 'S1'
  AND ce.mark >= 0;

CREATE OR REPLACE VIEW stat(student,s1_pass,s1_total) 
AS
SELECT student,
       sum(CASE WHEN sem='S1'
           AND mark >= 50 THEN 1 ELSE 0 END) AS s1_pass,
       sum(CASE WHEN sem='S1' THEN 1 ELSE 0 END) AS s1_total
FROM students_marks
GROUP BY student;

CREATE OR REPLACE VIEW s1_ac(student, as_s1) 
AS
SELECT student,
       CASE
           WHEN s1_total > 1
                AND s1_pass = 0 THEN 'Probation'
           WHEN s1_total > 1
                AND (s1_pass::float / s1_total::float) <= 0.5 THEN 'Referral'
           WHEN s1_total > 1
                AND (s1_pass::float / s1_total::float) > 0.5 THEN 'Good'
           WHEN s1_total = 1
                AND s1_pass = 1 THEN 'Good'
           WHEN s1_total = 1
                AND s1_pass = 0 THEN 'Referral'
           ELSE 'OTHER'
       END AS as_s1
FROM stat;

CREATE OR REPLACE VIEW Q11(unswid,name,academic_standing) 
AS
SELECT p.unswid,
       p.name,
       a.as_s1
FROM s1_ac a
JOIN People p ON a.student = p.id
WHERE CAST(p.unswid AS TEXT) LIKE '313%'
  AND NOT a.as_s1 = 'OTHER';


-- Q12:
CREATE OR REPLACE VIEW CourseInfo(id, code, name, YEAR, term, courseId) AS
SELECT sub.id,
       sub.code,
       sub.name,
       sem.YEAR,
       sem.term,
       c.id
FROM subjects sub,
     courses c,
     semesters sem
WHERE sub.id = c.subject
  AND c.semester = sem.id;


CREATE OR REPLACE VIEW MajorSemesters(YEAR, term) AS
SELECT DISTINCT semesters.YEAR,
                semesters.term
FROM courses,
     semesters
WHERE courses.semester = semesters.id
  AND (semesters.YEAR BETWEEN 2003 AND 2012)
  AND semesters.term LIKE 'S%';


CREATE OR REPLACE VIEW GoodSubjects(id, code, name, YEAR, term, courseId) AS
SELECT *
FROM CourseInfo c
WHERE c.code LIKE 'COMP90%'
  AND NOT exists(
                   (SELECT YEAR,term
                    FROM MajorSemesters) EXCEPT
                   (SELECT YEAR,term
                    FROM CourseInfo
                    WHERE code = c.code) );


CREATE OR REPLACE VIEW Q12(code, name, YEAR, s1_ps_rate, s2_ps_rate) AS
SELECT code,
       name,
       YEAR,
       CASE
           WHEN s1n=0 THEN NULL
           ELSE (s1npass::float / s1n::float)::numeric(4,2)
       END,
       CASE
           WHEN s2n=0 THEN NULL
           ELSE (s2npass::float / s2n::float)::numeric(4,2)
       END
FROM
  (SELECT code,
          name,
          substr(YEAR::text,3,2) AS YEAR,
          sum(CASE WHEN term='S1'
              AND mark >= 50 THEN 1 ELSE 0 END) AS s1npass,
          sum(CASE WHEN term='S1' THEN 1 ELSE 0 END) AS s1n,
          sum(CASE WHEN term='S2'
              AND mark >= 50 THEN 1 ELSE 0 END) AS s2npass,
          sum(CASE WHEN term='S2' THEN 1 ELSE 0 END) AS s2n
   FROM
     (SELECT s.code,
             s.name,
             ce.mark,
             s.YEAR,
               s.term
      FROM GoodSubjects s
      JOIN course_enrolments ce ON (s.courseId=ce.course)
      WHERE ce.mark >= 0 ) AS A
   GROUP BY code,
            name,
            YEAR ) AS B
ORDER BY code,
         YEAR;

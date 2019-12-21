-- Create view student_class_stream_view as
-- Select *
-- from students_student s
-- left join academics_classes w
-- on w.id = s.class_stream_id
CREATE VIEW exam_performance_view as
SELECT
   stud_id, sir_name,first_name, name, marks, subject_id, grade, term, year, class_numeral_id, stream_id
  FROM students_student
Left JOIN academics_examperformance ON academics_examperformance.stud_id = students_student.student_id
INNER JOIN academics_exam ON academics_exam.id = academics_examperformance.name_id
INNER JOIN academics_classes ON academics_classes.id = students_student.class_ns_id
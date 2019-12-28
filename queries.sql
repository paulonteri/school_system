-- Create view student_class_stream_view as
-- Select *
-- from students_student s
-- left join academics_classes w
-- on w.id = s.class_stream_id
CREATE VIEW exam_performance_view as
SELECT
   academics_examperformance.student_id, sir_name,first_name, exam_name_id, english, kiswahili, mathematics, religious_education, science, social_studies, total, term, year, class_numeral_id, stream_id, academics_examperformance.id
  FROM students_student
Left JOIN academics_examperformance ON academics_examperformance.student_id = students_student.student_id
INNER JOIN academics_exam ON academics_exam.id = academics_examperformance.exam_name_id
INNER JOIN academics_classes ON academics_classes.id = students_student.class_ns_id
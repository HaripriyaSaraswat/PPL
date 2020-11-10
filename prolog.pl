subject_teacher(t1,ppl).

subject_teacher(t2,dsa).

subject_teacher(t3,dsa).

subject_teacher(t4,ode).

subject_teacher(t5,dld).

subject_teacher(t6,dtl).

 

dept_subject(maths_dept,ode).

dept_subject(comp_dept,dsa).

dept_subject(comp_dept,ppl).

dept_subject(comp_dept,dtl).

dept_subject(comp_dept,dld).



 

dept_student(comp_dept,s1).

dept_student(comp_dept,s2).

dept_student(maths_dept,s2).

dept_student(comp_dept,s3).
 

 

has_faculty(D,F) :- subject_teacher(F,S) , subject_teacher(D,S).

studies_subject(ST,SB) :- dept_student(D,ST) , dept_subject(D,SB).

studies_under(S,F) :- dept_subject(D,SB) , dept_student(D,S) , subject_teacher(F,SB).
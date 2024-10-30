#1. LABS

completed_labs = int(input("Enter the number of labs completed: "))
 
if completed_labs  <  6 :
 grade_contribution_l = (completed_labs /6) * 20  
else : 
  grade_contribution_l = 20

#2. QUIZZ

completed_quizzes =int(input("Enter the number of quizzes completed: "))

if completed_quizzes < 6 :
 grade_contribution_q = (completed_quizzes /6) * 15
else : 
 grade_contribution_q = 15

#3. ASSIGNMENT 1

grade_a1 =int(input("Enter grade for Assignment 1: "))

a1_weight = 0.04
grade_contribution_1 = (a1_weight* grade_a1)  

#4. ASSIGNMENT 2

grade_a2 =int( input("Enter grade for Assignment 2: "))

a2_weight = 0.04
grade_contribution_2 = (a2_weight* grade_a2) 

#5. ASSIGNMENT 3

grade_a3 = int(input("Enter grade for Assignment 3: "))

a3_weight = 0.04 
grade_contribution_3 = (a3_weight* grade_a3)  

#6. ASSIGNMENT 4

grade_a4 = int(input("Enter grade for Assignment 4: "))

a4_weight = 0.04
grade_contribution_4 = (a4_weight* grade_a4)  

#7. MIDTERM 1

grade_mid1 = int(input("Enter grade for Midterm 1: "))

m1_weight = 0.125
grade_contribution_m1 = (m1_weight * grade_mid1)

#8. MIDTERM 2

grade_mid2 = int(input("Enter grade for Midterm 2: "))

m2_weight = 0.125
grade_contribution_m2 = (m2_weight * grade_mid2) 

#9 FINAL 

grade_final = int(input("Enter grade for Final Exam: "))

f_weight = 0.18
grade_contribution_f = (f_weight*grade_final)  

#10 PREP

grade_prep = int(input("Enter grade for Midterms and Final Preparation: "))

prep_weight = 0.06
grade_contribution_p = (prep_weight * grade_prep)

# FINAL GRADE

print("Your final grade is: ", round(grade_contribution_l + grade_contribution_q + grade_contribution_1 + grade_contribution_2 + grade_contribution_3 + grade_contribution_4 + grade_contribution_m1 + grade_contribution_m2 + grade_contribution_p + grade_contribution_f, 1))

if  (grade_contribution_l + grade_contribution_q + grade_contribution_1 + grade_contribution_2 + grade_contribution_3 + grade_contribution_4 + grade_contribution_m1 + grade_contribution_m2 + grade_contribution_p + grade_contribution_f) < 60 :
 print( "YOU FAILED... :( " )
else :
 print( " CONGRATS ! " )



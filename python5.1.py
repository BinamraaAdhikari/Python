#Enter marks of 3 subj from user and store in dictionary

dict1={}
name=input("Enter your name:")
marks1=input("Enter Physics marks:")
marks2=input("Enter Maths marks:")
marks3=input("Enter Chemistry marks:")
dict1.update({"Name":name})
dict1.update({"Subjects":{"Physics":marks1,"Maths":marks2,"Chemistry":marks3}})
print(dict1)

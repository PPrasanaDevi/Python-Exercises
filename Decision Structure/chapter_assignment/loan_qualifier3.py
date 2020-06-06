#This program determine whether a bank customer qualifies for a loan.
MIN_SALARY = 30000.0 #MINIMUM SALARY
MIN_YEARS = 2 #MINIMUM YEARS ON THE JOB

#Get the customer's annual salary
salary = float(input('Enter your annual salary: '))
#Get number of years on the job
years_on_job = int(input('Enter number of years on the job: '))

#Determine whether the customer qualifies.
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print('You qualify for the loan')
else:
    print('You do not qualify for the loan')

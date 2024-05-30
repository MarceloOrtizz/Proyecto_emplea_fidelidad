### Data Dictionary of Variables


Fuente de datos: [IBM-HR-Analytics](https://github.com/denistanjingyu/IBM-HR-Analytics/blob/master/Data/ibm.clean.csv)

| Variable Name            | Description                                                                                          | Metric                                                           |
|--------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Age                      | Total years lived by the employee.                                                                   |                                                                  |
| AgeStartedWorking        | Age that the individual started working. (Derived variable: Age - TotalWorkingYears)                 |                                                                  |
| Application ID           | Unique identifier of the employee when applying for a job in the company.                            |                                                                  |
| Attrition                | Outcome variable of employee status                                                                  | Current Employee / Voluntary Resignation / Termination           |
| AverageTenure            | Average length of time at the job. (Derived variable: PriorYearsOfExperience / NumCompaniesWorked)   |                                                                  |
| BusinessTravel           | Indication of whether the employee travels abroad for work-related purposes.                         | Travel Frequently / Travel_Rarely / Non_Travel                   |
| Department               | The department that the employee currently works for or has previously worked for.                   | Human Resources / Research & Development / Sales                 |
| DistanceFromHome         | Distance between the employee’s home and the company, measured in KM.                                |                                                                  |
| Education                | Highest level of education attained by the employee.                                                 | 1: Below college / 2: College / 3: Bachelor / 4: Master / 5: Doctor |
| EducationField           | The employee’s main field of study.                                                                  | Human Resources / Life Sciences / Marketing / Medical / Technical Degree / Other |
| EmployeeCount            | Number of employees in the company.                                                                  |                                                                  |
| EmployeeNumber           | Unique identifier of the employee.                                                                   |                                                                  |
| Gender                   | Biological characteristics of the individual.                                                        | Female / Male                                                    |
| JobRole                  | Role of the individual in the company.                                                               | Healthcare Representative / Human Resources / Laboratory Technician / Manager / Manufacturing Director / Research Director / Research Scientist / Sales Executive / Sales Representative |
| MaritalStatus            | Relationship status of an employee.                                                                  | Divorced / Married / Single                                      |
| NumCompaniesWorked       | Total number of companies the employee has worked for prior to his/her current job.                  |                                                                  |
| Over18                   | Indication of whether the employee is more than 18 years old.                                        | Y / N                                                            |
| PriorYearsOfExperience   | Number of working years experience before the current job. (Derived variable: TotalWorkingYears - YearsAtCompany) |                                                                  |
| TotalWorkingYears        | Total years the employee has worked.                                                                 |                                                                  |
| TrainingTimesLastYear    | Number of work-related trainings attended by the employee last year.                                 |                                                                  |
| YearsAtCompany           | Total years the employee has worked for the company.                                                 |                                                                  |
| YearsInCurrentRole       | Total years the employee has stayed in his/her current role in the company.                          |                                                                  |
| YearsSinceLastPromotion  | Total years since the employee was last promoted.                                                    |                                                                  |
| YearsWithCurrManager     | Total years working under the same manager.                                                          |                                                                  |
| Employee Source          | Source of employee recruitment.                                                                      | Referral / Company Website / Seek / LinkedIn / Adzuna / Indeed / Glassdoor / Jora / Recruit.net |
| DailyRate                | Gross rate of pay per day.                                                                           |                                                                  |
| HourlyRate               | Gross rate of pay per hour.                                                                          |                                                                  |
| MonthlyIncome            | Monthly salary of the employee.                                                                      |                                                                  |
| MonthlyRate              | Gross rate of pay per month.                                                                         |                                                                  |
| OverTime                 | Indication of whether the employee has worked after his/her standard working hours.                  | Yes / No                                                         |
| PercentSalaryHike        | Percentage increase in the employee’s salary compared to the prior year.                            |                                                                  |
| StandardHours            | Number of hours stipulated in the employee contract.                                                 |                                                                  |
| StockOptionLevel         | Proportion of the employee’s income spent on purchasing the company’s stocks.                        | 0-3 (0 indicates no stock purchase; higher numbers indicate higher proportion) |
| EnvironmentSatisfaction  | Degree to which the employee is satisfied with the work environment.                                 | 1-4 (higher number indicates higher satisfaction)                |
| JobInvolvement           | Degree to which the employee identifies with his/her job.                                            | 1-4 (higher number indicates higher involvement)                 |
| JobLevel                 | The employee’s assessment of his/her job difficulty.                                                 | 1-4 (higher number indicates higher difficulty)                  |
| JobSatisfaction          | Degree to which the employee is satisfied with his/her job.                                          | 1-4 (higher number indicates higher satisfaction)                |
| PerformanceRating        | Grade given to the employee by his/her superior based on his/her performance at work.                | 1-4 (higher number indicates higher rating)                      |
| RelationshipSatisfaction | Degree to which the employee is satisfied with his/her relationships at work.                        | 1-4 (higher number indicates higher satisfaction)                |
| WorkLifeBalance          | Degree to which the employee agrees that there is work-life balance.                                 | 1-4 (higher number indicates higher balance)                     |

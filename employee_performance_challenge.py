import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

def load_employee_data ():
    df = pd.read_csv("data/employee_performance.csv")
    df.columns = df.columns.str.lower()
    return df
def explore_employee_dataframe(df):
  
    return(f"""EMPLOYEE INFO {df.head(10)}
                {df.info()}
                {df.describe()}""")


def select_and_filter_employee_data(df):
    return df.loc[df.performance_score > 80,["employee_id", "first_name", "last_name", "performance_score"]]

#i stupidly did the slogging work of calculating the years of the employee at the company and then realized there was a variable just for that. LESSON : Always check the shape fully of your data before starting!!! But it was a good lesson also in working with datetimes which is a weak point for me so it wasn't really a waste. really used AI to great effect on this one...

def employee_data_operations(df):
    current_date = pd.to_datetime('today').normalize()
    dates = df["hire_date"]
    dates = pd.to_datetime(dates)
    difference = current_date - dates
    years_since_hire = (difference.dt.days / 365.25).round()  # Using 365.25 to account for 
    salary_per_year = df["salary"] / years_since_hire
    salary_per_year = salary_per_year.round(2)
    sorted_df_based_on_performance_scores = df.sort_values(by='performance_score', ascending=False)
    return sorted_df_based_on_performance_scores


def top_3_employees_with_highest_salary(df):
        sorted_df_based_on_salary = df.sort_values(by='salary', ascending=False)
        top_3_highest_paid_employees = sorted_df_based_on_salary[["first_name", "last_name", "email", "salary"]].head(3)
        top_3_highest_paid_employees['salary'] = top_3_highest_paid_employees['salary'].round(2)
        return top_3_highest_paid_employees



def avg_performance_score_by_department(df):
    # Group by department_id and calculate the average performance_score
    avg_performance = df.groupby("department_id")["performance_score"].mean()
    return avg_performance


def plot_salary_vs_years_of_experience(df):
    total_employees = len(df)
    x_axis = df["salary"]
    y_axis = df["years_at_company"]
    plt.scatter(x_axis, y_axis)
    plt.title('Distribution of Salary to Years at Company')
    plt.xlabel('Salary Amount')
    plt.ylabel('Years at Company')
    plt.show()
    



   

    
def main():
    df = load_employee_data()
    # Uncomment each function one by one to see the output


    # print(f'2. Explore the DataFrame \n')
    # print(explore_employee_dataframe(df)) DONE

    #print(f'3. Select and filter employee data \n')
    # print(select_and_filter_employee_data(df)) DONE

    # print(f'4. Perform Data Operations: \n')
    # print(employee_data_operations(df)) DONE 

    #print(f'5. Find the top 3 employees with the highest salary \n')
    # print(top_3_employees_with_highest_salary(df)) DONE


    #print(f'6. Average performance score by department \n')
    # print(avg_performance_score_by_department(df)) DONE

    #print(f'7. Plot a scatter plot of salary vs years_at_company \n')
    # print(plot_salary_vs_years_of_experience(df)) DONE

if __name__ == "__main__":
    main()


#%%
import matplotlib.pyplot as plt
from calculate_wrapper import get_total
from data_to_file import display_categories

@get_total
def visualise(sums):
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,5))
    # Calculation
    expenses = [sums[f"sums_{i}"] for i in range(1,9)]
    
    #get the reference_categories_value
    ref_cat_value = display_categories(out=False)
    categories = [i[1] for i in ref_cat_value[1:]]
    incomes = round(sums['sums_0'] + sums['sums_9'], 2)

    # Joint var
    remain = round(incomes + sum(expenses), 2)
    expenses.append(remain)
    categories.append("Remain")
    
     # Pie chart
    pie_expenses, pie_categories = list(), list()
    for i, _ in enumerate(expenses):
        if expenses[i] != 0:
            pie_expenses.append(abs(expenses[i]))
            pie_categories.append(categories[i])
    
    ax1.pie(pie_expenses, labels = categories, autopct='%1.2f%%',startangle=90)
    ax1.axis('equal')

    # Bar chart
    labels = ["Incomes", "Expenses", "Remain"]
    values = [incomes, abs(round(sum(expenses[:-1]), 2)), remain]
    ax2.bar(labels, values, width=0.5, color=["blue", "red", "green"])

    for index,data in enumerate(values):
        plt.text(x=index , y=data+20 , s=f"{data}", fontdict=dict(fontsize=13), ha="center")
    plt.show()
from . import Expense
import collections
import matplotlib.pyplot as plt

expenses=Expense.Expenses()
expenses.read_expenses('data/spending_dat.csv')
spending_categories = []
for expense in expense.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending.category)
top5 = spending_counter.most_common(5)
categories, count = zip(*top5)

fix, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show ()

### Data Analyst Python Interview Answers

# 1. Basic Python
# A1: Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# A2: Filter even numbers from a list
def filter_evens(lst):
    return [x for x in lst if x % 2 == 0]

# A3: Swap two variables without a third variable
a, b = 5, 10
a, b = b, a

# 2. Data Structures
# A4: Find two numbers in a list that sum to a target
def two_sum(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen[num] = True
    return None

# A5: Count occurrences of characters in a string
def char_count(s):
    from collections import Counter
    return dict(Counter(s))

# A6: Remove duplicates while maintaining order
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# 3. Pandas & NumPy
import pandas as pd
import numpy as np

# A7: Load a CSV into Pandas
df = pd.read_csv("data.csv")
print(df.head())

# A8: Fill missing values with column mean
df.fillna(df.mean(), inplace=True)

# A9: Normalize a NumPy array
def normalize_array(arr):
    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

# 4. SQL-like operations with Pandas
# A10: Select rows where sales > 1000
df_filtered = df[df["sales"] > 1000]

# A11: Inner join between two DataFrames
df1.merge(df2, on="common_column", how="inner")

# A12: Group by column and sum another column
df.groupby("category")["sales"].sum()

# 5. Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# A13: Histogram of a column
df["column_name"].hist()
plt.show()

# A14: Scatter plot with Seaborn
sns.scatterplot(x=df["col1"], y=df["col2"])
plt.show()

# A15: Box plot
sns.boxplot(y=df["column_name"])
plt.show()

# 6. Algorithms & Problem-Solving
# A16: Factorial using recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# A17: Reverse a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

# A18: Quicksort algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 7. Bonus Questions
import requests
from bs4 import BeautifulSoup

# A19: Web scraping example
def scrape_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    products = [(p.text, p.find_next_sibling("span").text) for p in soup.find_all("h2")]
    return products

# A20: Simple Flask API
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Hello, World!"})

if __name__ == "__main__":
    app.run(debug=True)

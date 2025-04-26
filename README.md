# Babak-Yousefian-BD-T1

# Big Data Homework 1 - MRJob Solutions
_By ```Babak Yousefian```_

---

## 📚 Introduction

This project solves two problems using **Python** and the **MRJob** library (MapReduce in Python).  
The two problems are related to **text processing** and **matrix manipulation**.

The goal is to simulate simple distributed computing using **MRJob** framework.

---

## 🧩 Problem 1: Find Top 3 Frequent Words (Ignoring Stopwords)

### 📄 Problem Description
Given a text file (`File1.txt`), we must:
- Find and count the occurrences of **each real word**.
- Ignore **common prepositions**, conjunctions, and other stopwords.
- Output the **Top 3 most frequent words** with their counts.

---

### 🛠️ Code Explanation

```python
from mrjob.job import MRJob
from mrjob.step import MRStep


```

Import the MRJob base class and MRStep for multi-step MapReduce jobs.

```
class MRTop3WordsFiltered(MRJob):
```
Define a new class inheriting from MRJob.

STOPWORDS = {...}
A set of common English stopwords like 'the', 'and', 'of', etc.

Words inside this list will not be counted.

```python
def steps(self):
    return [
        MRStep(mapper=self.mapper_get_words,
               reducer=self.reducer_count_words),
        MRStep(mapper=self.mapper_prepare_for_sort,
               reducer=self.reducer_output_top3)
    ]
```
Define two steps:

Step 1: Word counting.

Step 2: Sorting and selecting Top 3.

Step 1: Counting Words

```python
def mapper_get_words(self, _, line):
    pass
```
For each line, split into words, normalize (lowercase, remove punctuation).

Ignore any word found in STOPWORDS.

Emit each word as key, 1 as value.

```python
def reducer_count_words(self, word, counts):
    pass
```
Sum all counts for each word.

Step 2: Selecting Top 3

```python
def mapper_prepare_for_sort(self, word, count):
    pass
```

Emit (None, (count, word)) to prepare for sorting.


```python
def reducer_output_top3(self, _, count_word_pairs):
    pass
```
Sort all word-count pairs in descending order.

Output only the Top 3.

---

## 🧩 Problem 2: Matrix Transpose
📄 Problem Description
Given a file (File2.txt) representing a matrix:

Each line describes a matrix element: (MatrixID, Row, Column, Value).

Output the transposed matrix:

Row and Column are swapped.

🛠️ Code Explanation
```python
from mrjob.job import MRJob
```
Import MRJob base class.

```python
class MRMatrixTranspose(MRJob):
      pass
```
Define a new MRJob class for transposing the matrix.

Mapper: Swapping Row and Column

```python
def mapper(self, _, line):
    pass
```
Read each line.

Split the line into matrix ID, row, column, value.

Emit key (MatrixID, Column, Row) and value.

Row and Column are swapped here.

Reducer: Emitting Transposed Matrix

```python
def reducer(self, key, values):
    pass
```
For each key (which is (MatrixID, Column, Row)), emit the value.

## ⚡ How to Run the Programs
Make sure you are in your virtual environment, then:

- ### 1. To find Top 3 frequent words:


python top3words_filtered.py File1.txt
✅ Outputs top 3 real words and their counts.

- ### 2. To transpose the matrix:


python transpose_matrix.py File2.txt
✅ Outputs the transposed matrix entries.

## 📌 Important Notes
MRJob reads input files line-by-line automatically. No need to open the file manually.

Stopwords are filtered using a set to make counting meaningful words more accurate.

Sorting is done in the second MapReduce step to find the top 3 words.

## 🚀 Final Tips
This project is tested on Python 3.10.x and MRJob 0.7.x.

On Python 3.12+, some manual fixes might be needed because of pipes module removal.

Always activate your .venv virtual environment before running.

---

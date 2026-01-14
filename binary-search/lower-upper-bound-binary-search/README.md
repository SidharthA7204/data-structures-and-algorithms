# Lower Bound & Upper Bound using Binary Search (Python)

## 📌 Problem Statement
Given a sorted array and a value `x`, find:

- **Lower Bound** → first index `i` where `arr[i] >= x`
- **Upper Bound** → first index `i` where `arr[i] > x`

If such index does not exist, return `n` (length of array).

---

## 🧠 Why Binary Search?
- Array is sorted
- Time complexity improves from `O(n)` to `O(log n)`

---

## 📘 Example

Array:[1, 4, 6, 10, 13]

| x | Lower Bound | Upper Bound |
|---|---|---|
| 6 | 2 | 3 |
| 8 | 3 | 3 |
| 15 | 5 | 5 |

---

## 🚀 Python Implementation

### Lower Bound → `lower_bound.py`
### Upper Bound → `upper_bound.py`

---

## ⚡ Built-in Python Method
import bisect
bisect.bisect_left(arr, x)   # lower bound
bisect.bisect_right(arr, x)  # upper bound

⏱ Complexity
Time: O(log n)
Space: O(1)




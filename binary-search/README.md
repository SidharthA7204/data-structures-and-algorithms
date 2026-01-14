# 🔍 Binary Search

This folder contains implementations related to the **Binary Search algorithm**.

Binary search is an efficient searching technique that works on **sorted arrays** and reduces time complexity from **O(n)** to **O(log n)**.

---

## 🧠 Concepts Covered
- Basic binary search
- Mid-point calculation
- Boundary conditions
- Handling edge cases

---

## 📂 Files
- `binary_search_basic.py` – Standard binary search implementation

---

## ⏱️ Complexity
- Time Complexity: **O(log n)**
- Space Complexity: **O(1)**


 **Lower Bound – Pseudocode**
 
 function lower_bound(arr, x):
    low = 0
    high = length(arr) - 1
    ans = length(arr)
        while low <= high:
          mid = (low + high) // 2
          if arr[mid] >= x:
            ans = mid
            high = mid - 1
          else:
            low = mid + 1
      return ans
      
** Upper Bound – Pseudocode**
function upper_bound(arr, x):
    low = 0
    high = length(arr) - 1
    ans = length(arr)
    while low <= high:
        mid = (low + high) // 2
       if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
      return ans



### Time Complexity Analysis:

1. **Naive Approach:**
   - **Big O (Worst Case):** \(O(n)\) - The loop iterates through each element in the list exactly once.
   - **Big Omega (Best Case):** \(O(n)\) - The best case is the same as the worst case because the loop always iterates through all elements.
   - **Theta (Average Case):** \(O(n)\) - Every case runs in linear time, making it \(\Theta(n)\).

2. **Recursive Approach:**
   - **Big O (Worst Case):** \(O(n)\) - Each recursive call processes one element, and there are \(n\) recursive calls for a list of size \(n\).
   - **Big Omega (Best Case):** \(O(n)\) - Similar to the worst case because all elements must be summed.
   - **Theta (Average Case):** \(O(n)\) - All cases involve \(n\) recursive calls.

   **Note:** The recursive approach also has a space complexity of \(O(n)\) due to the function call stack.

3. **Using Built-in Functions:**
   - **Big O (Worst Case):** \(O(n)\) - The `sum()` function internally iterates over the list once.
   - **Big Omega (Best Case):** \(O(n)\) - Even in the best case, the function processes all elements.
   - **Theta (Average Case):** \(O(n)\) - Similar to the other cases, making it \(\Theta(n)\).

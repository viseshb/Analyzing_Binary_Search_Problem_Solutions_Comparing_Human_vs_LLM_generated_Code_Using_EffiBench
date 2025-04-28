# 📌 ANALYZING BINARY SEARCH SOLUTIONS: HUMAN VS LLM BENCHMARKING USING EFFIBENCH

This project analyzes solutions to binary search problems by benchmarking and comparing the performance of human-written code against LLM-generated code (ChatGPT, Gemini, Claude). Using the EffiBench framework, it provides a precise evaluation of execution time and memory usage to highlight efficiency differences across solution sources.

---

🔹 **Project Structure**
We benchmarked and analyzed three types of solutions:
- **Human-written code:** Canonical efficient binary search solutions.
- **LLM-generated code:** Solutions created by ChatGPT, Gemini, and Claude models.
- **Benchmarking Framework:** Used EffiBench to ensure standardized measurement of execution time and memory usage.

---

🔹 **Techniques Used**
We focused on performance and memory profiling:
- **Execution Time Measurement:** Capturing precise run times for each solution.
- **Memory Usage Analysis:** Measuring maximum and average memory consumption.
- **Benchmarking Framework:** Used EffiBench to automate and standardize evaluations.

---

🔹 **Highlights**
The project highlights key observations:
- Human code generally shows consistent efficiency.
- LLM code varies: some generate highly optimized solutions, others have unnecessary overhead.
- Benchmarks reveal subtle differences not visible from code inspection alone — especially in memory handling and runtime complexity.

---


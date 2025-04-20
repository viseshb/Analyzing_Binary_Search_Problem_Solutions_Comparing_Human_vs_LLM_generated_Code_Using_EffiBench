import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# STEP 1: Load Excel file
file_path = r'C:\Users\vises\OneDrive\Desktop\Masters_TAMUSA\Sem1\Algorithms\Algorithm_Project\LeetCode_Problems.xlsx'
excel_data = pd.ExcelFile(file_path)
df = excel_data.parse('MAIN- SHEET')

# STEP 2: Clean headers and rows
df_clean = df[1:].copy()
df_clean.columns = [
    'Problem No',
    'Human Time', 'Human MemTime', 'Human AvgMem', 'Human MaxMem',
    'ChatGPT Time', 'ChatGPT MemTime', 'ChatGPT AvgMem', 'ChatGPT MaxMem',
    'Gemini Time', 'Gemini MemTime', 'Gemini AvgMem', 'Gemini MaxMem',
    'Claude Time', 'Claude MemTime', 'Claude AvgMem', 'Claude MaxMem'
]

# STEP 3: Convert time and memory values to numeric
for col in ['Human Time', 'ChatGPT Time', 'Gemini Time', 'Claude Time']:
    df_clean[col] = df_clean[col].str.extract(r'([\d.]+)').astype(float)
for col in df_clean.columns[2:]:
    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

# STEP 4: Assign difficulty
df_clean = df_clean[pd.to_numeric(df_clean['Problem No'], errors='coerce').notna()]
df_clean['Problem No'] = df_clean['Problem No'].astype(int)
difficulty_labels = ['Easy'] * 10 + ['Medium'] * 10 + ['Hard'] * 10
df_clean = df_clean.iloc[:len(difficulty_labels)].copy()
df_clean['Difficulty'] = difficulty_labels

# Assign group order
difficulty_order = {'Easy': 0, 'Medium': 1, 'Hard': 2}
df_clean['GroupOrder'] = df_clean['Difficulty'].map(difficulty_order)

# STEP 5: Calculate efficiency scores
df_clean['ChatGPT Score'] = df_clean['ChatGPT Time'] * df_clean['ChatGPT MaxMem']
df_clean['Gemini Score'] = df_clean['Gemini Time'] * df_clean['Gemini MaxMem']
df_clean['Claude Score'] = df_clean['Claude Time'] * df_clean['Claude MaxMem']
df_clean['Human Score'] = df_clean['Human Time'] * df_clean['Human MaxMem']

# STEP 6: Sort and set up groups
df_ordered = df_clean.sort_values(by=['GroupOrder', 'Problem No']).reset_index(drop=True)
x = np.arange(len(df_ordered))
width = 0.2
problem_labels = df_ordered['Problem No'].tolist()

groups = {"Easy": (0, 9), "Medium": (10, 19), "Hard": (20, 29)}
colors_darker = {'Easy': '#218838', 'Medium': '#e0a800', 'Hard': '#c82333'}

# === Helper Functions ===

def add_labels(ax, bars, use_scientific=True):
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            label = f'{height:.2e}' if use_scientific else f'{height:.2f}'
            ax.text(bar.get_x() + bar.get_width()/2., height * 1.01,
                    label, ha='center', va='bottom', fontsize=8, rotation=90)

def draw_darker_background(ax, group_dict, colors):
    for label, (start, end) in group_dict.items():
        ax.axvspan(start - 0.5, end + 0.5, facecolor=colors[label], alpha=0.3)

# === EXECUTION TIME ===
plt.figure(figsize=(16, 6))
ax = plt.gca()
draw_darker_background(ax, groups, colors_darker)
b1 = ax.bar(x - 1.5*width, df_ordered['ChatGPT Time'], width, label='ChatGPT')
b2 = ax.bar(x - 0.5*width, df_ordered['Gemini Time'], width, label='Gemini')
b3 = ax.bar(x + 0.5*width, df_ordered['Claude Time'], width, label='Claude')
b4 = ax.bar(x + 1.5*width, df_ordered['Human Time'], width, label='Human')
plt.yscale('log')
add_labels(ax, b1 + b2 + b3 + b4)
plt.xticks(x, problem_labels, rotation=45)
plt.xlabel("Problem No's by Difficulty Level")
plt.ylabel('Execution Time (s) [Log Scale]')
plt.title('Execution Time by LLMs (Grouped by Difficulty)')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.4)
ax.set_ylim(bottom=1e-7, top=1e-1)
plt.tight_layout()
plt.savefig('execution_time_darker_background.png')
plt.show()

# === MAX MEMORY ===
plt.figure(figsize=(16, 6))
ax = plt.gca()
draw_darker_background(ax, groups, colors_darker)
b1 = ax.bar(x - 1.5*width, df_ordered['ChatGPT MaxMem'], width, label='ChatGPT')
b2 = ax.bar(x - 0.5*width, df_ordered['Gemini MaxMem'], width, label='Gemini')
b3 = ax.bar(x + 0.5*width, df_ordered['Claude MaxMem'], width, label='Claude')
b4 = ax.bar(x + 1.5*width, df_ordered['Human MaxMem'], width, label='Human')
add_labels(ax, b1 + b2 + b3 + b4, use_scientific=False)
plt.xticks(x, problem_labels, rotation=45)
plt.xlabel("Problem No's by Difficulty Level")
plt.ylabel('Max Memory (MB)')
plt.title('Max Memory Usage by LLMs (Grouped by Difficulty)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
ax.set_ylim(bottom=0, top=16)
plt.tight_layout()
plt.savefig('max_memory_darker_background.png')
plt.show()

# === EFFICIENCY SCORE ===
plt.figure(figsize=(16, 6))
ax = plt.gca()
draw_darker_background(ax, groups, colors_darker)
b1 = ax.bar(x - 1.5*width, df_ordered['ChatGPT Score'], width, label='ChatGPT')
b2 = ax.bar(x - 0.5*width, df_ordered['Gemini Score'], width, label='Gemini')
b3 = ax.bar(x + 0.5*width, df_ordered['Claude Score'], width, label='Claude')
b4 = ax.bar(x + 1.5*width, df_ordered['Human Score'], width, label='Human')
plt.yscale('log')
add_labels(ax, b1 + b2 + b3 + b4)
plt.xticks(x, problem_labels, rotation=45)
plt.xlabel("Problem No's by Difficulty Level")
plt.ylabel('Efficiency Score (Time × Max Mem) [Log Scale]')
plt.title('Efficiency Score by LLMs (Grouped by Difficulty)')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)
ax.set_ylim(bottom=1e-8, top=1)
plt.tight_layout()
plt.savefig('efficiency_score_darker_background.png')
plt.show()

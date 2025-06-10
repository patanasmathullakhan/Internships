<h1 align="center">🎬 Netflix Dataset Cleaning & Preprocessing</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Project-Type%3A%20Assignment-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tools-Pandas%2C%20NumPy%2C%20Seaborn%2C%20Sklearn-ff69b4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.icons8.com/color/480/netflix-desktop-app.png" width="120px" />
</p>


---

## 📂 Dataset Used

- **Source:** [Kaggle Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **File Name:** `netflix_titles.csv`
- **Content:** Contains metadata for Netflix Movies and TV Shows including:
  - `title`, `type`, `country`, `cast`, `date_added`, `duration`, and more.

---

## 🧠 Objective

Use Python libraries **Pandas** and **NumPy** to:

- 🧹 Detect and clean missing, duplicate, and invalid data  
- 🔁 Convert data types appropriately  
- 🔢 Use NumPy for transformations  
- 🔍 Use Pandas for filtering, sorting, and grouping  
- 📊 Bonus: Visualize missing values and correlations  


---

## 🛠 Technologies Used

| Tool            | Purpose                         |
|-----------------|----------------------------------|
| Python 🐍        | Core programming language        |
| Pandas 📊        | Data cleaning & manipulation     |
| NumPy 🔢         | Numerical calculations           |
| Seaborn 📈       | Visualization (heatmaps)         |
| Matplotlib 📉    | Basic plotting                   |


---

## 🧼 Data Cleaning Steps

| Step               | Description                                                 |
|--------------------|-------------------------------------------------------------|
| ✅ Load Data        | Used `pd.read_csv()` to load the dataset                   |
| ✅ Inspect          | Used `.info()`, `.isnull()`, `.duplicated()`, `.describe()` |
| ✅ Handle Missing   | Filled or forward-filled nulls for `director`, `cast`, etc. |
| ✅ Drop Duplicates  | Used `.drop_duplicates()`                                   |
| ✅ Convert Types    | Converted `date_added` to `datetime`                        |
| ✅ Extract Duration | Split `duration` into `duration_int` and `duration_type`    |


---


## 🔢 NumPy Usage

- Used **min-max normalization** on `duration_int`
- Extracted numeric data from string columns (e.g., from `duration`)

---

## 🔁 Pandas Usage

- **Filtering:** Extracted only TV Shows
- **Grouping:** Counted titles by country
- **Sorting:** Sorted by `date_added`, `release_year`, and more

---

> 📌 Summary
> 
✅ Cleaned and structured over 6 columns

✅ Converted types and filled missing values

✅ Added feature columns like duration_int

✅ Visualized key insights



---


Made with 💻 and ☕ by ASMATHULLA KHAN

# 🌌 UFO Sightings Dashboard (Power BI)

## 🔭 Project Overview
This report visualizes UFO sightings from multiple perspectives—temporal, geographical, and by duration. Emphasizing both visuals and storytelling, the dashboard conveys the mysterious atmosphere behind the data.

## 🧠 Concept & Design Philosophy
While incorporating non-ordinary themes such as UFOs and aliens, the dashboard maintains a data representation suitable for business use. With intuitive usability and a unique visual style, it aims to provide an experience that goes beyond simple information delivery.

## 📊 Data Source
The report is based on the *NUFORC UFO Sightings Dataset* (available on Kaggle), originally provided as `scrubbed.csv`.
Prior to visualization, the dataset was filtered, cleaned, and reshaped. The final version used for analysis is saved as `cleaned_data.csv`.

## 🎨 Visual Structure & UI
1. **Background image**: A thematic custom design sets the tone for the entire layout.
2. **Color & fonts**: Dark mode + metallic silver tone (#C0C0C0) ensure futuristic yet high-contrast readability.
   - Font color: #C0C0C0 (silver gray)
   - Minimal visual noise: Axes, borders, and titles are removed to emphasize clean data forms.
3. **Page structure**: Concise page names and clearly guided navigation enhance usability.

## 🧪 Technical Highlights
1. Created under a Power BI environment with account-free limitations, where visual options were restricted.
2. Custom visuals were generated using Python Visuals, building a coherent and immersive design theme.
3. Visuals are saved as transparent PNG images from Python and layered over Power BI’s background for seamless integration.

## 👤 Intended Audience & Use
This dashboard was designed for:
- Power BI users in business or analytics roles
- Hiring teams evaluating technical capabilities in M language, Python integration, and data-driven design

> 🔍 This dashboard also serves as a portfolio project showcasing the creator Sachiko’s Power BI skill set.

## ⚠️ Important Notes
The visuals for “UFO Duration” and “Witness Remarks” in the Statistics page are powered by Python Visuals and will only display correctly in Power BI environments where Python is enabled.

## 🐍 Python Visuals & Required Libraries
To display the custom Python-based visuals, follow these steps:

1. In Power BI Desktop, go to  
   `File → Options and settings → Options → Python scripting`  
   and specify the path to your `python.exe`
2. Install the following libraries in your Python environment:

```bash
pip install matplotlib pandas numpy wordcloud
```

## ⚠️ Data Refresh

This report references two external CSV files:

- `cleaned_data.csv`  
- `latitude_longitude_grouping_table_world.csv`

These files are already loaded into the `.pbix` file, so in most cases **no refresh is needed**.  
However, if the **[Refresh]** button is pressed, Power BI may attempt to access the original absolute file paths used during development, which can lead to errors.

### ✅ If refresh is needed:

- Make sure both CSV files exist locally on your machine  
- In Power BI, go to **Transform Data**  
- Open each query (`cleaned_data`, `latitude_longitude_grouping_table_world`)  
- Update the following step to match your local path:  
  `Source = File.Contents("your/local/path/to/file.csv")`

---

## 📁 File Structure

- PBI_UFO-Study.zip`: Archive containing the report and required resources  
  ├─ `UFO Project.pbix`: Main Power BI report file  
  ├─ `cleaned_data.csv`: Cleaned UFO sightings data  
  ├─ `latitude_longitude_grouping_table_world.csv`: Grid-based location mapping  
  ├─ `images/`: Backgrounds and visual assets  
  └─ `PythonScripts/`: Python scripts for visual generation  

- `DataCleansing.py` (optional): Data preprocessing script  
- `scrubbed.csv` (optional): Original raw dataset  
- `README.md`: This document

## 📥 How to Use

### ✅ Required:

Download the following file:

- `PBI_UFO-Study.zip`  
  → Contains everything needed to open and explore the dashboard (PBIX file, CSVs, visuals, and scripts)

### 🔍 Optional (if you want to explore further):

- `DataCleansing.py`: Review the data cleaning logic  
- `scrubbed.csv`: Raw UFO sightings data before cleaning

---

## 🛠 Recommended Environment

| Software           | Version             |
|--------------------|----------------------|
| Power BI Desktop   | Version 2.144 or later |
| Python             | 3.9 or 3.10 (64-bit)  |

---

## 🔭 Future Plans

- Rebuild the themed dashboard in Tableau  
- Add interactivity, animations, and external data integrations in future updates

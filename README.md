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
pip install matplotlib pandas numpy wordcloud Pillow

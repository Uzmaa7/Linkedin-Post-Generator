# Linkedin-Post-Generator

A simple AI-powered tool to generate engaging LinkedIn posts with customizable options for **title**, **length**, and **language**.  
Built with **Streamlit** for the UI and an LLM backend for content generation.  

---

## 🚀 Features
- Select post **title/topic** from predefined tags.  
- Choose **length**: Short, Medium, or Long.  
- Select **language**: English or Hinglish.  
- Generates clean LinkedIn posts by removing unnecessary `<think>...</think>` tags from LLM responses.  

---

## 🛠️ Tech Stack
- [Python 3.10+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – Interactive UI  
- LLM (via `llm.invoke`) – Text generation backend  
- Regex (Python `re`) – For cleaning unwanted tags  

---

## 📂 Project Structure
.

├── app.py - Streamlit UI

├── few_shot.py # Few-shot examples for post generation

├── generator.py # generate_post function (LLM + regex cleaning)

├── requirements.txt # Dependencies

└── README.md


---

## ⚡ Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Linkedin-Post-Generator.git
   cd Linkedin-Post-Generator
   ```
2. Create and activate a virtual environment:
    ``` bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux 
    venv\Scripts\activate      # Windows
   ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
   ```
4. Run the app:
     ```bash
        streamlit run app.py
    
    ```
   

# 🎯 Example

Input: Title = "AI in Hiring", Length = "Medium", Language = "English"

Output: A professional LinkedIn-style post ready to share.

# 🔮 Future Improvements

Add support for multiple tones (professional, witty, motivational).

Allow direct posting to LinkedIn via API.

Store generated posts history.

# 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your idea.

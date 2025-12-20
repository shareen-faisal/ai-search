# 🗺️ Romania Route Planner (AI Search Visualizer)

A web-based interactive visualizer for Artificial Intelligence search algorithms (BFS, DFS, UCS). This project demonstrates how different pathfinding strategies navigate the classic "Romania Map" problem to find a route between two cities.

## 🚀 Live Demo
**Click here to view the live project:** 👉 **[https://ai-search-git-main-eman-faisals-projects-9ae5e7e9.vercel.app?_vercel_share=xQcApgvugb5LD0oGS9659rzTjdkHRahb]**

---

## 🌟 Features
* **Graph Visualization:** Interactive map rendered using **Vis.js**.
* **3 Search Algorithms:** Compare the performance of:
    * **BFS** (Breadth-First Search)
    * **DFS** (Depth-First Search)
    * **UCS** (Uniform Cost Search)
* **Animated Pathfinding:** Watch the algorithm trace the path step-by-step with a 1-second delay.
* **Dynamic Graph Editing:** Add new cities and road connections dynamically via the sidebar.
* **Performance Metrics:** View the **Total Cost** and **Time Complexity (Steps)** for each search.

---

## 🛠️ Technologies Used
* **Backend:** Python, Flask
* **Frontend:** HTML5, JavaScript (Fetch API)
* **Visualization:** Vis.js Library
* **Styling:** CSS3 (Custom Purple Theme)
* **Deployment:** Vercel

---

## 📂 Project Structure
```bash
├── static/
│   └── style.css       
├── templates/
│   └── index.html      
├── app.py              
├── requirements.txt   
├── vercel.json        
└── README.md          
```
💻 How to Run Locally
Follow these steps to set up and run the project on your own computer.

1. Prerequisites
Make sure you have Python 3.x installed. You can check by running:

```bash

python --version
```
2. Download the Project
Clone the repository or download the ZIP file and extract it.

```bash

git clone <your-repository-link>
cd <your-project-folder>
```
3. Install Dependencies
Open your terminal/command prompt in the project folder and install the required Python packages (Flask):

```bash

pip install -r requirements.txt
```
4. Run the Application
Start the Flask server by running the app.py file:

```bash
python app.py
```
You should see output indicating the server is running (usually on http://127.0.0.1:5000).

5. Open in Browser
Open your web browser (Chrome, Edge, etc.) and navigate to:
```bash
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
```

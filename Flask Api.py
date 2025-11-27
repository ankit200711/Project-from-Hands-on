from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Resume - Ankit</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      background: #f4f4f9;
      color: #333;
    }
    .resume {
      display: grid;
      grid-template-columns: 1fr 2fr;
      max-width: 1000px;
      margin: 30px auto;
      background: #fff;
      box-shadow: 0 0 15px rgba(0,0,0,0.1);
    }
    .sidebar {
      background: #2c3e50;
      color: #fff;
      padding: 20px;
    }
    .sidebar h2 {
      border-bottom: 2px solid #fff;
      padding-bottom: 5px;
    }
    .sidebar ul {
      list-style: none;
      padding: 0;
    }
    .sidebar ul li {
      margin: 10px 0;
    }
    .main {
      padding: 20px;
    }
    .main header {
      border-bottom: 2px solid #333;
      margin-bottom: 20px;
    }
    .main header h1 {
      margin: 0;
    }
    section {
      margin-bottom: 20px;
    }
    h2 {
      color: #2c3e50;
      border-bottom: 1px solid #ccc;
      padding-bottom: 5px;
    }
    ul {
      list-style: none;
      padding: 0;
    }
    ul li {
      margin-bottom: 8px;
    }
  </style>
</head>
<body>
  <div class="resume">
    <!-- Sidebar -->
    <div class="sidebar">
      <h2>Contact</h2>
      <p>Email: fiuhfed.gmail.com</p>
      <p>Phone: +91-79790*****</p>
      <p>Location: Jaipur, India</p>

      <h2>Skills</h2>
      <ul>
        <li>HTML, CSS, JavaScript, Python</li>
        <li>React, Node.js</li>
        <li>Responsive Design</li>
        <li>Git & GitHub</li>
      </ul>
    </div>

    <!-- Main Content -->
    <div class="main">
      <header>
        <h1>Ankit</h1>
        <p>Web Developer</p>
      </header>

      <section>
        <h2>Summary</h2>
        <p>Motivated web developer with experience building responsive websites and applications. Passionate about clean design and efficient code.</p>
      </section>

      <section>
        <h2>Experience</h2>
        <ul>
          <li><strong>Web Developer</strong> – Vivekananda Company (2025–Present)</li>
          <li><strong>Intern</strong> – Linux World Solutions (2025)</li>
        </ul>
      </section>

      <section>
        <h2>Education</h2>
        <ul>
          <li>B.Tech –University, Jaipur (2024–2028)</li>
        </ul>
      </section>
    </div>
  </div>
</body>
</html>
    """
@app.route("/about")
def about():
    return """
    <h1>I am about page </h1>
    <h2>Iam running in flask</h2>
    """
if __name__=='__main__':
     app.run()
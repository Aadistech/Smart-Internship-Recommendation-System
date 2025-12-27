from flask import Flask, render_template, request
from model import recommend_internship

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    skills = request.form["skills"]
    results = recommend_internship(skills)
    return render_template("result.html", internships=results)

# Internship details dictionary
internship_info = {
    "Data Analyst": {
        "description": "Data Analysts analyze data to help companies make better decisions.",
        "skills": "Python, SQL, Excel, Statistics",
        "tools": "Pandas, Power BI, Excel",
        "scope": "High demand in IT, finance, healthcare"
    },
    "Web Development": {
        "description": "Web Developers build websites and web applications.",
        "skills": "HTML, CSS, JavaScript",
        "tools": "VS Code, React, Browser",
        "scope": "Strong demand in startups and IT companies"
    },
    "Machine Learning": {
        "description": "ML Engineers build intelligent systems using data.",
        "skills": "Python, Pandas, Scikit-learn",
        "tools": "Jupyter, ML Libraries",
        "scope": "Growing field in AI-based companies"
    },
    "Cloud Computing": {
        "description": "Cloud computing is the delivery ofComputer fundamentals computing services—such as servers, storage, databases, networking, software, and analytics—over the internet instead of using local computers or physical servers.",
        "skills": "Computer fundamentals, Networking basics (IP, DNS, TCP/IP), Operating systems (Linux & Windows), Basic programming (Python, Java, or JavaScript)",
        "tools": "Docker,Kubernetes,Terraform,Ansible,Git & GitHub,Jenkins / GitHub Actions",
        "scope": "Cloud computing has huge demand and long-term scope because most companies are moving to the cloud"
    },
    "Cyber Security": {
        "description": "Cyber Security is the practice of protecting computers, networks, servers, applications, and data from cyber attacks, unauthorized access, data breaches, and malware.",
        "skills": "Computer Fundamentals, Networking Basics(TCP/IP, DNS, HTTP/HTTPS),Operating systems (Linux is very important),Basics of programming (Python, C, JavaScript),Ethical hacking concepts,Cryptography basics,Network security,Web application security,Security policies & risk management",
        "tools": "<b>Ethical Hacking Tools</b>:Kali Linux,Metasploit,Nmap,Burp Suite<br>"
                 "<b>Security Tools</b>:Snort,Splunk,Firewall,OpenVAS / Nessus,OWASP ZAP<br>"
                 "<b> Cryptography & Password Tools</b>:Hashcat,John the Ripper<br>",
        "scope": "Cyber security has very high demand because cyber attacks are increasing every year."
    },
    "Android Development": {
        "description": "Android Development is the process of creating applications for Android devices such as smartphones, tablets, smart TVs, and wearables using Android OS.",
        "skills": "Java or Kotlin (Kotlin is preferred),Android SDK & app lifecycle,Activities & Fragments,Layouts (XML),Intents & Services,Permissions & background tasks",
        "tools": "<b>Development Tools</b>:Android Studio (official IDE),Android SDK,Emulator & real device testing,Gradle (build system)<br>"
                 "<b>Libraries & Frameworks</b>:Jetpack (ViewModel, LiveData, Room),Retrofit / Volley (API calls),Firebase (Auth, Firestore, FCM),Glide / Picasso (image loading)<br>"
                 "<b>Databases</b>:SQLite,Room Database,Firebase Firestore<br>",
        "scope": "Android Development has excellent scope because Android is the most used mobile OS globally.",
        "Job Roles":"Android App Developer,Mobile Application Developer,Software Engineer (Android),Freelance App Developer,Startup App Developer.",
        "Average Salary (India – Approx.)":"Fresher: ₹3–6 LPA<br>"
                                           "2–5 years: ₹7–15 LPA<br>"
                                           "Experienced: ₹20+ LPA<br>", 
    },
    "Digital Marketing": {
    "description": "Digital Marketing is the process of promoting products, services, or brands using digital platforms.",
    
    "skills": "SEO, SEM / Google Ads, Marketing fundamentals, Communication skills, Content creation",
    
    "tools": "<b>SEO & Analytics Tools:</b> Google Analytics, Google Search Console, Ahrefs, SEMrush<br>"
             "<b>Advertising Tools:</b> Google Ads, Facebook Ads Manager, Instagram Ads, LinkedIn Ads<br>"
             "<b>Email & Automation Tools:</b> Mailchimp, HubSpot, Zoho Campaigns",
    
    "scope": "Digital marketing has huge scope due to online business growth and e-commerce.",
    
    "Job Roles": "Digital Marketing Executive, SEO Specialist, Social Media Manager, Content Marketer, PPC Specialist, Marketing Analyst",
    
    "Average Salary (India – Approx.)": """
    Fresher: ₹3–5 LPA<br>
    2–5 years: ₹6–12 LPA<br>
    Experienced: ₹15+ LPA
    """
},
"UI UX Design": {
    "description": "Digital Marketing is the process of promoting products, services, or brands using digital platforms.",
    
    "skills": "SEO, SEM / Google Ads, Marketing fundamentals, Communication skills, Content creation",
    
    "tools": "<b>SEO & Analytics Tools:</b> Google Analytics, Google Search Console, Ahrefs, SEMrush<br>"
             "<b>Advertising Tools:</b> Google Ads, Facebook Ads Manager, Instagram Ads, LinkedIn Ads<br>"
             "<b>Email & Automation Tools:</b> Mailchimp, HubSpot, Zoho Campaigns",
    
    "scope": "Digital marketing has huge scope due to online business growth and e-commerce.",
    
    "Job Roles": "Digital Marketing Executive, SEO Specialist, Social Media Manager, Content Marketer, PPC Specialist, Marketing Analyst",
    
    "Average Salary (India – Approx.)": """
    Fresher: ₹3–5 LPA<br>
    2–5 years: ₹6–12 LPA<br>
    Experienced: ₹15+ LPA
    """

},

}



@app.route("/details/<internship>")
def details(internship):
    info = internship_info.get(internship, None)
    return render_template("details.html", internship=internship, info=info)


if __name__ == "__main__":
    app.run(debug=True)

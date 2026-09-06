from flask import Flask, render_template_string
import requests

app=Flask(__name__)
SERVICES={"Google":"https://www.google.com","GitHub":"https://github.com","Python":"https://www.python.org"}
HTML="""<html><head><title>Service Dashboard</title><style>body{font-family:Arial;max-width:850px;margin:40px auto}.card{border:1px solid #ddd;padding:15px;margin:10px 0;border-radius:8px}</style></head>
<body><h1>Service Availability Dashboard</h1>{%for name,url,status in rows%}<div class=card><b>{{name}}</b> — {{status}}<br><small>{{url}}</small></div>{%endfor%}</body></html>"""
@app.route("/")
def home():
    rows=[]
    for name,url in SERVICES.items():
        try:
            r=requests.get(url,timeout=5); status=f"Online ({r.status_code})"
        except requests.RequestException: status="Unavailable"
        rows.append((name,url,status))
    return render_template_string(HTML,rows=rows)
if __name__=="__main__": app.run(debug=True)

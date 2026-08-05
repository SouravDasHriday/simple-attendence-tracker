import csv
import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
DATA_FILE = "attendance.csv"

def init_csv():
    """Creates the CSV file with headers if it does not exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Time", "Status"])

def get_attendance():
    """Reads all attendance records from the CSV file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header row
        return list(reader)

@app.route("/")
def index():
    records = get_attendance()
    return render_template("index.html", records=records)

@app.route("/check-in", methods=["POST"])
def check_in():
    name = request.form.get("name", "").strip()
    status = request.form.get("status", "Present")
    
    if name:
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, date_str, time_str, status])
            
    return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

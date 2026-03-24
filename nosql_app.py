from flask import Flask, render_template_string, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Compass
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["analytical_minds"]
collection = db["fraud_alerts"]

@app.route('/')
def dashboard():
    # --- INTERACTIVE LOGIC ---
    # status: 1 (Fraud), 0 (Safe)
    # limit: number of records to show
    status_filter = int(request.args.get('status', 1))
    record_limit = int(request.args.get('limit', 15))
    
    # Query MongoDB based on user interaction
    query = {"isFraud": status_filter}
    data_list = list(collection.find(query).limit(record_limit))
    
    # --- DYNAMIC UI DESIGN ---
    html_template = """
    <html>
        <head>
            <title>Analytical-Minds | Interactive NoSQL Portal</title>
            <style>
                body { font-family: 'Segoe UI', sans-serif; background-color: #f0f2f5; padding: 30px; }
                .container { max-width: 1100px; margin: auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
                h1 { color: #1a237e; border-bottom: 4px solid #3949ab; padding-bottom: 10px; }
                .nav-buttons { margin-bottom: 25px; display: flex; gap: 12px; flex-wrap: wrap; }
                button { padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; transition: 0.2s; color: white; }
                .btn-fraud { background: #d32f2f; }
                .btn-safe { background: #388e3c; }
                .btn-more { background: #1976d2; }
                .btn-reset { background: #455a64; } /* Slate gray for reset */
                button:hover { opacity: 0.8; transform: translateY(-1px); }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; background: #fff; }
                th { background: #263238; color: white; padding: 15px; text-align: left; }
                td { padding: 12px; border-bottom: 1px solid #eee; }
                .tag { padding: 5px 10px; border-radius: 4px; font-size: 0.85em; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Analytical-Minds Fraud Detection Portal</h1>
                <p>Status Filter: <b>{{ 'FRAUD' if status == 1 else 'SECURE' }}</b> | Records Displayed: <b>{{ limit }}</b></p>
                
                <div class="nav-buttons">
                    <button class="btn-fraud" onclick="window.location.href='/?status=1&limit={{ limit }}'">Show Fraud Only</button>
                    <button class="btn-safe" onclick="window.location.href='/?status=0&limit={{ limit }}'">Show Legitimate Only</button>
                    <button class="btn-more" onclick="window.location.href='/?status={{ status }}&limit={{ limit + 20 }}'">Load 20 More</button>
                    <button class="btn-reset" onclick="window.location.href='/?status=1&limit=15'">Reset Dashboard</button>
                </div>

                <table>
                    <thead>
                        <tr>
                            <th>Transaction Type</th>
                            <th>Amount (USD)</th>
                            <th>Old Balance</th>
                            <th>Security Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for item in alerts %}
                        <tr>
                            <td>{{ item.type }}</td>
                            <td>${{ "{:,.2f}".format(item.amount) }}</td>
                            <td>${{ "{:,.2f}".format(item.oldbalanceOrg) }}</td>
                            <td>
                                <span class="tag" style="background: {{ '#ffebee' if item.isFraud == 1 else '#e8f5e9' }}; color: {{ '#c62828' if item.isFraud == 1 else '#2e7d32' }}">
                                    {{ 'FRAUD' if item.isFraud == 1 else 'SECURE' }}
                                </span>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </body>
    </html>
    """
    return render_template_string(html_template, alerts=data_list, status=status_filter, limit=record_limit)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
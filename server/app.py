from flask import Flask, jsonify
import os
from supabase import create_client, Client

app = Flask(__name__)



url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/')
def home():
    try:
        response = supabase.table('Test').select("*").execute()
        # Convert response to JSON
        data = response.get('data', [])
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # Ensure database directory exists
    db_dir = os.path.join(os.path.dirname(__file__), 'database')
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    # Get the port from the system (Mini Deploy uses 8080, local uses 5001)
    port = int(os.environ.get("PORT", 5001))
    # You MUST use host="0.0.0.0" so Docker can "see" your app
    app.run(host="0.0.0.0", port=port, debug=True)
# import openai
# import sqlite3
# import datetime

# # OpenAI API setup
# openai.api_key = "your-openai-api-key"

# # Database setup
# DB_FILE = "history.db"

# def init_database():
#     """Initialize the SQLite database to store world history."""
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()
#         # Events table
#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS events (
#             id INTEGER PRIMARY KEY,
#             date TEXT,
#             location TEXT,
#             description TEXT,
#             characters TEXT
#         )
#         ''')
#         # Characters table (optional for detailed character tracking)
#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS characters (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             type TEXT, -- e.g., "individual", "family", "tribe", "nation"
#             description TEXT
#         )
#         ''')
#         conn.commit()

# def save_event(date, location, description, characters):
#     """Save a new event to the database."""
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#         INSERT INTO events (date, location, description, characters)
#         VALUES (?, ?, ?, ?)
#         ''', (date, location, description, characters))
#         conn.commit()

# def get_history(location=None, date=None):
#     """Retrieve history based on location and/or date."""
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()
#         query = "SELECT date, location, description, characters FROM events WHERE 1=1"
#         params = []
#         if location:
#             query += " AND location = ?"
#             params.append(location)
#         if date:
#             query += " AND date = ?"
#             params.append(date)
#         cursor.execute(query, params)
#         return cursor.fetchall()

# def generate_context(prompt, history):
#     """Use OpenAI to generate a scene context based on a prompt and history."""
#     messages = [{"role": "system", "content": "You are a world-building assistant for a fantasy RPG."}]
#     if history:
#         history_text = "\n".join([f"{event[0]} at {event[1]}: {event[2]} ({event[3]})" for event in history])
#         messages.append({"role": "user", "content": f"Here is the world history:\n{history_text}"})
#     messages.append({"role": "user", "content": prompt})
    
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=messages
#     )
#     return response["choices"][0]["message"]["content"]

# def add_details_to_history(location, new_details, characters):
#     """Process generated details and save them back to the database."""
#     now = datetime.datetime.now().strftime("%Y-%m-%d")
#     save_event(date=now, location=location, description=new_details, characters=characters)

# # Example usage
# if __name__ == "__main__":
#     init_database()

#     # Example prompt and retrieval of history
#     location = "Elven Forest"
#     date = None  # Retrieve all events for the location
#     history = get_history(location=location, date=date)

#     # Generate context for a new scene
#     scene_prompt = "Describe a mysterious event that happens in the Elven Forest."
#     context = generate_context(prompt=scene_prompt, history=history)
#     print("Generated Scene Context:\n", context)

#     # Save the generated details to the database
#     add_details_to_history(location, context, characters="Group of elves")
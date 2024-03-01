import json
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_data(data, filename="data.json"):
    try:
        with open(filename, "w") as f:
            json.dump(data, f)
        logging.info("Data saved successfully.")
    except Exception as e:
        logging.error(f"Error saving data to {filename}: {e}")

def load_data(filename="data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Silently initialize a new data structure without logging a warning
        return {}  # Return an empty dict if the file doesn't exist
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from {filename}.")
        return {}
    except Exception as e:
        logging.error(f"An error occurred while loading data from {filename}: {e}")
        return {}

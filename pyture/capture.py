import json
import uuid
from datetime import datetime
import csv

_captures = []
_session_id = str(uuid.uuid4())  # unique ID per run
_session_start = datetime.now().isoformat()  # timestamp


class Pyture:
    def __init__(self, mode="normal"):
        self.buffer = []
        self.mode = mode

    def capture(self, **kwargs):
        capture_data = {
            "timestamp": datetime.now().isoformat(),  
            "session_id": _session_id,
            "data": kwargs
        }

        self.buffer.append(kwargs)
        _captures.append(capture_data)

        if self.mode == "dev":
            print(f"[Captured] {kwargs}")

    def save(self, filename, mode="full"):
        """Save data with flexible formatting: raw, timestamp, session, or full"""

        try:
            data_to_save = []

            for item in _captures:
                if mode == "raw":
                    data_to_save.append(item["data"])
                elif mode == "timestamp":
                    data_to_save.append({
                        "timestamp": item["timestamp"],
                        "data": item["data"]
                    })
                elif mode == "session":
                    data_to_save.append({
                        "session_id": item["session_id"],
                        "data": item["data"]
                    })
                else:
                    data_to_save.append(item)
                
            with open(filename, "w") as file:
                json.dump(data_to_save, file, indent=4)
                if self.mode == "dev":
                    print(f"[Saved] ({mode}) → {filename}")
        except Exception as e:
            print(f"[Error] Failed to save: {e}")

    def load(self, filename):
        """Load captured data from a JSON file into the buffer"""
        try:
            with open(filename, "r") as file:
                self.buffer = json.load(file)
            if self.mode == "dev":
                print(f"[Loaded] Data loaded from '{filename}'")
        except Exception as e:
            print(f"[Error] Failed to load: {e}")

    def clear(self):
        """Clear all captured data"""
        self.buffer.clear()
        _captures.clear()

        if self.mode == "dev":
            print(f"[Cleared] Capture buffer is now empty.")


    def get_session_info(self):
        return {
        "session_id": _session_id,
        "started_at": _session_start,
        "captures": len(_captures)
       }
    
    # Adding export_csv here

    def export_csv(self, filename):
        """Export captured data to a CSV file"""
        try:
            if not _captures:
                print("[CSV Export] No data to export.")
                return
            
            # Find all possible user keys (flattened)
            all_keys = set()
            for entry in _captures:
                all_keys.update(entry["data"].keys())

            fieldnames = ["timestamp", "session_id"] + sorted(all_keys)

            with open(filename, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for entry in _captures:
                    row = {
                        "timestamp": entry["timestamp"],
                        "session_id": entry["session_id"],
                    }
                    row.update(entry["data"]) # adds user data keys/values
                    writer.writerow(row)
            
            if self.mode == "dev":
                print(f"[Exported] Data exported to '{filename}'")

        except Exception as e:
            print(f"[Error] Failed to export CSV: {e}")
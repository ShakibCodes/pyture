
<div align="center">
<div align="center" style="margin: 0 auto; max-width: 80%;">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="img/pyturelogo.png">
    <source media="(prefers-color-scheme: light)" srcset="img/pyturelogo.png">
    <img alt="mcp use logo" src="img/pyturelogo.png" width="80%" style="margin: 20px auto;">
  </picture>
</div>

<h1 align="center">Capture Everything. Elegantly.</h1>

<p align="center">
  <a href="https://github.com/ShakibCodes/pyture/stargazers" alt="GitHub stars">
    <img src="https://img.shields.io/github/stars/ShakibCodes/pyture?style=social" /></a>
  <a href="https://pepy.tech/projects/pyture"><img src="https://static.pepy.tech/personalized-badge/pyture?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads" alt="PyPI Downloads"></a>

  <a href="https://pypi.org/project/pyture/" alt="PyPI Version">
    <img src="https://img.shields.io/pypi/v/pyture.svg"/></a>
  <a href="https://github.com/ShakibCodes/pyture/blob/main/LICENSE" alt="License">
    <img src="https://img.shields.io/github/license/ShakibCodes/pyture" /></a>
  <a href="https://pyture.vercel.app" alt="Website">
    <img src="https://img.shields.io/badge/website-pyture.vercel.app-blue" /></a>
</p>
</div>


## What is PyTure

PyTure is a lightweight Python library for capturing and recording code execution.
It gives you structured visibility into your program by logging:

- Inputs & outputs of your functions

- Timestamps and unique session IDs

- Captured data/events during runtime

- Flexible export options (JSON or CSV)

With just a few lines, you can start collecting full context about your code — making it perfect for debugging, teaching, experimenting, or building smarter workflows.

**One line. Full context. Pure Python.**

## Why Pyture?

When debugging or experimenting, developers often rely on scattered `print()` statements or heavy debuggers to understand what’s happening in their code. Both approaches can get messy and disruptive.

Pyture provides a clean middle ground: a lightweight way to capture runtime variables with timestamps and session IDs, all in just one line. Instead of cluttering your code, you can log exactly the values you care about and export them later for inspection.

Captured data can be saved as JSON (with multiple levels of detail) or exported to CSV for spreadsheet-friendly analysis. This makes it easy to trace variable changes, group them by session, and review your program’s behavior at any stage — without breaking its flow.x

## Features


PyTure focuses on capturing structured runtime data in the simplest way possible. Instead of cluttering your code with print() statements, you can log variables, save them in multiple formats, and revisit them later for debugging, analysis, or reporting.


### Key Features

- Runtime Variable Capture – Log any number of variables at once using capture(**kwargs).

- Flexible Save Formats – Export to JSON in four modes (raw, timestamp, session, full) depending on how much metadata you want.

- CSV Export – Generate spreadsheet-friendly logs with .export_csv().

- Session Tracking – Every run gets a unique session ID and start timestamp.

- Development Mode – Enable "dev" mode to see real-time console feedback for capture, save, clear, and export operations.

- Data Management – Reload previous captures with .load() or reset everything with .clear().

- Session Info API – Query session metadata (ID, start time, capture count) with .get_session_info().


### Features overview
 

| Feature | Description |
|---------|-------------|
| 📝 **Runtime Capture** | Log variables at runtime as key-value pairs using [`capture(**kwargs)`](#usage--code-examples). |
| 📂 **JSON Export (4 modes)** | Save captures in different detail levels: `raw`, `timestamp`, `session`, `full` via [`save(filename, mode)`](#usage--code-examples). |
| 📊 **CSV Export** | Export captured data into a spreadsheet-friendly format using [`export_csv(filename)`](#usage--code-examples). |
| 🆔 **Session Management** | Each run is tagged with a unique session ID and start timestamp (auto-managed internally). |
| ⚡ **Development Mode** | Print debug info during operations by initializing with [`Pyture(mode="dev")`](#api-reference). |
| 📥 **Data Reloading** | Reload captured data from JSON files into the buffer with [`load(filename)`](#usage--code-examples). |
| 🧹 **Data Clearing** | Reset buffer and clear all current session captures using [`clear()`](#usage--code-examples). |
| 🔍 **Session Info** | Retrieve metadata like session ID, start time, and capture count using [`get_session_info()`](#usage--code-examples). |



## Installation

Install Pyture using pip:

```
pip install pyture
```

## Usage & Code Examples

PyTure is managed through the `Pyture` class. Here are examples of its core functionality.  

### Basic Capture & Save

This example demonstrates how to capture data and save it in the default `"full"` mode.

```python
from pyture import Pyture

# Initialize the capture manager
cap = Pyture(mode="dev")  # dev mode prints status messages

# Capture some variables
user_id = 101
request_path = '/api/data'
cap.capture(user_id=user_id, request_path=request_path)

# Capture more data later in the code
response_code = 200
status = 'success'
cap.capture(response_code=response_code, status=status)

# Save the captured data to a JSON file (default mode is 'full')
cap.save('full_output.json')

```


### Saving with Different Modes

The `.save()` method allows you to specify a mode for the output JSON.

```python
from pyture import Pyture

cap = Pyture()
cap.capture(username='john_doe', role='admin')
cap.capture(is_authenticated=True)

# Save only the captured data (no metadata)
cap.save('raw_output.json', mode='raw')

# Save with only the timestamp
cap.save('timestamp_output.json', mode='timestamp')

# Save with only the session ID
cap.save('session_output.json', mode='session')

# Save with all metadata (timestamp, session_id, and data)
cap.save('full_output.json', mode='full')
```

### Exporting to CSV

Use the .export_csv() method to save your data in a flattened CSV format.

```python
from pyture import Pyture

cap = Pyture()
cap.capture(event='user_login', user_id=123)
cap.capture(event='purchase', product_id=987, amount=45.99)

cap.export_csv('capture_log.csv')
```

### Loading & Clearing Data

You can reload previously saved data into the buffer or clear everything in the current session.

```python
from pyture import Pyture

cap = Pyture()

# Load data back into the buffer
cap.load('full_output.json')

# Clear all captures for a fresh start
cap.clear()
```

### Session Info

Retrieve information about the current session.

```python
from pyture import Pyture

cap = Pyture()
cap.capture(a=1, b=2)

print(cap.get_session_info())

# Example:
# {
#   "session_id": "4fa3e914-2bd9-49a2-8c7e-ff2df228c14b",
#   "started_at": "2025-08-30T19:20:31.556729",
#   "captures": 1
# }
```



## API Reference  

The core functionality of PyTure is provided through the `Pyture` class.  
Each method is designed to capture, manage, and export runtime data in a structured way.  

---

### `class Pyture(mode="normal")`  

Create a new capture manager instance.  

- **Parameters**:  
  - `mode` (*str*, optional): Controls verbosity.  
    - `"normal"` (default): Silent operation (no console output).  
    - `"dev"`: Prints status messages during `capture()`, `save()`, `load()`, `clear()`, and `export_csv()`.  

---

### `Pyture.capture(**kwargs)`  

Capture one or more runtime variables as key-value pairs.  

- **Parameters**:  
  - `**kwargs`: Any number of variables to record. Keys become column names in JSON/CSV output.  

- **Behavior**:  
  - Automatically adds `timestamp` and `session_id`.  
  - Stores data in both the internal buffer (`self.buffer`) and the global capture log (`_captures`).  

---

### `Pyture.save(filename, mode="full")`  

Save captured data to a JSON file with flexible formatting.  

- **Parameters**:  
  - `filename` (*str*): Destination filename (e.g., `"output.json"`).  
  - `mode` (*str*, optional): Export format.  
    - `"raw"`: Captured data only.  
    - `"timestamp"`: Include timestamp + data.  
    - `"session"`: Include session ID + data.  
    - `"full"` (default): Include timestamp, session ID, and data.  

---

### `Pyture.export_csv(filename)`  

Export all captures to a CSV file.  

- **Parameters**:  
  - `filename` (*str*): Destination filename (e.g., `"output.csv"`).  

- **Behavior**:  
  - Columns include `timestamp`, `session_id`, plus all unique keys from captured data.  
  - Each capture becomes a row.  

---

### `Pyture.load(filename)`  

Load previously saved JSON data into the buffer.  

- **Parameters**:  
  - `filename` (*str*): Path to JSON file created via `.save()`.  

- **Behavior**:  
  - Overwrites the current buffer (`self.buffer`).  
  - Does **not** repopulate `_captures`.  

---

### `Pyture.clear()`  

Clear all captured data from the current session.  

- **Behavior**:  
  - Empties both `self.buffer` and the global `_captures` list.  
  - Useful for starting fresh within the same script run.  

---

### `Pyture.get_session_info()`  

Retrieve metadata about the current session.  

- **Returns** (*dict*):  
  ```json
  {
    "session_id": "2fd9e3c6-3a14-4931-88b0-6b374a2c6a2a",
    "started_at": "2025-08-30T20:15:12.439884",
    "captures": 1
  }
  ```




## Example Output

Below are examples of what PyTure generates when saving or exporting captured data.  

---

### JSON Preview (mode = `"full"`)  
When you save using:  

```python
cap.save("full_output.json", mode="full")
```

You’ll get a JSON file like this:

```json
[
  {
    "timestamp": "2025-08-30T20:30:45.123456",
    "session_id": "2fd9e3c6-3a14-4931-88b0-6b374a2c6a2a",
    "data": {
      "user_id": 101,
      "request_path": "/api/data"
    }
  },
  {
    "timestamp": "2025-08-30T20:30:45.678901",
    "session_id": "2fd9e3c6-3a14-4931-88b0-6b374a2c6a2a",
    "data": {
      "response_code": 200,
      "status": "success"
    }
  }
]

```

- Each entry is a dictionary with a `timestamp`, `session_id`, and your captured `data`.

- Timestamps are in ISO 8601 format with microseconds (Python’s `datetime.now().isoformat()`).

- All captures from the same run share the same `session_id`.


### CSV Preview

When you export using:
```python
cap.export_csv("capture_log.csv")
```

You’ll get a spreadsheet-friendly CSV like this:

```json
timestamp,session_id,event,user_id,product_id,amount
2025-08-30T20:30:45.123456,2fd9e3c6-3a14-4931-88b0-6b374a2c6a2a,user_login,123,,
2025-08-30T20:30:45.678901,2fd9e3c6-3a14-4931-88b0-6b374a2c6a2a,purchase,,987,45.99
```
- The first two columns (`timestamp`, `session_id`) are always present.

- All unique keys from your captured data are flattened into extra columns (`event`, `user_id`, `product_id`, `amount`).

- Missing values are left blank for rows where a key was not present.

👉 **For more details and advanced usage, visit the [PyTure Documentation](https://pyture.vercel.app/docs/getting%20started/intro.html).**


## Contributing  

We welcome contributions to PyTure! 🎉  
Whether it’s fixing a bug, adding a feature, or improving documentation — your help makes the project better.  

To contribute:  
1. **Fork** the repository  
2. Create a new branch for your feature or bug fix  
3. Implement your changes and ensure everything runs correctly  
4. Submit a **pull request** with a clear description of your changes  

You can also open **issues** for feature requests, questions, or bug reports.  

👉 **To know more about contributing, visit the [PyTure Contributions Guide](https://pyture.vercel.app/docs/resources/contribute.html).**

---


## License  

PyTure is released under the **MIT License**.  
For more details, see the [LICENSE](./LICENSE) file.  



---


👉 **For common questions, visit the [PyTure FAQ section](https://pyture.vercel.app/docs/resources/faq.html).**
<br>
<br>
⭐ **If you find PyTure useful, please consider giving this repository a star!**  
It helps support the project and lets others discover it too 🚀


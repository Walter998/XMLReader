# DefineConst.py

# Application Constants
APP_TITLE = "XML Reader"
APP_SIZE = (800, 600)

# UI Constants
FILE_LABEL = "XML File Path:"
SEARCH_LABEL = "Element to search:"
BROWSE_BUTTON_TEXT = "Browse"
SEARCH_BUTTON_TEXT = "Search"
HISTORY_BUTTON_TEXT = "History"
RESULTS_FRAME_TEXT = "Results"

# File Dialog Constants
FILE_TYPES = "XML files (*.xml);;All files (*)"

# TreeView Constants
COLUMN_NAMES = ("name", "value", "xpath")
COLUMN_HEADINGS = {
    "name": "Element Name",
    "value": "Value",
    "xpath": "XPath"
}
COLUMN_WIDTHS = {
    "name": 150,
    "value": 250,
    "xpath": 350
}

# Message Constants
ERROR_TITLE = "Error"
INFO_TITLE = "Information"
HISTORY_TITLE = "Search History"
NO_FILE_SELECTED = "Please select an XML file first"
NO_SEARCH_TERM = "Please enter an element to search for"
LOAD_FAILED = "Failed to load XML file: {}"
NO_RESULTS = "No elements found with tag '{}'"
NO_HISTORY = "No search history available"
HISTORY_LIST_ITEM = "{}. File: {} | Term: {}"
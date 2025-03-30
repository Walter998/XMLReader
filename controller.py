# controller.py
from model import XMLParserSingleton, SearchHistory
from DefineConst import *

class XMLReaderController:
    def __init__(self, view):
        self.view = view
        self.xml_parser = XMLParserSingleton()
        self.history = SearchHistory()
        
        # Set up event handlers
        self.view.set_browse_callback(self.browse_file)
        self.view.set_search_callback(self.search_elements)
        self.view.set_history_callback(self.show_history)
        
    def browse_file(self):
        file_path = self.view.browse_file()
        if file_path:
            success = self.xml_parser.load_file(file_path)
            if not success:
                self.view.show_error(LOAD_FAILED.format(file_path))
                
    def search_elements(self):
        file_path = self.view.get_file_path()
        search_term = self.view.get_search_element()
        
        if not file_path:
            self.view.show_error(NO_FILE_SELECTED)
            return
            
        if not search_term:
            self.view.show_error(NO_SEARCH_TERM)
            return
        
        # Make sure file is loaded
        if self.xml_parser.current_file != file_path:
            success = self.xml_parser.load_file(file_path)
            if not success:
                self.view.show_error(LOAD_FAILED.format(file_path))
                return
        
        # Perform search
        results = self.xml_parser.search_elements(search_term)
        
        # Add to history
        self.history.add_search(file_path, search_term)
        
        # Display results
        self.view.display_results(results)
        
        if not results:
            self.view.show_info(INFO_TITLE, NO_RESULTS.format(search_term))
            
    def show_history(self):
        history_items = self.history.get_history()
        self.view.display_history(history_items)
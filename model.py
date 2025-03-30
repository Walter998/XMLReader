# model.py
import xml.etree.ElementTree as ET
from typing import List, Dict
import os

class XMLParserSingleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(XMLParserSingleton, cls).__new__(cls)
            cls._instance.current_file = None
            cls._instance.root = None
        return cls._instance
    
    def load_file(self, file_path: str) -> bool:
        """Load XML file and return success status"""
        if not os.path.exists(file_path):
            return False
            
        try:
            tree = ET.parse(file_path)
            self.root = tree.getroot()
            self.current_file = file_path
            return True
        except ET.ParseError:
            return False
    
    def search_elements(self, element_tag: str) -> List[Dict[str, str]]:
        """Search for elements with the given tag"""
        if not self.root:
            return []
            
        results = []
        for element in self.root.findall(f".//{element_tag}"):
            xpath = self._get_xpath(element)
            results.append({
                "name": element.tag,
                "value": element.text.strip() if element.text else "",
                "xpath": xpath
            })
        return results
    
    def _get_xpath(self, element) -> str:
        """Generate XPath for the given element"""
        path = []
        parent = element
        while parent is not None:
            path.append(parent.tag)
            parent = parent.getparent() if hasattr(parent, 'getparent') else None
        
        return '/' + '/'.join(reversed(path))


class SearchHistory:
    def __init__(self):
        self.history = []
        
    def add_search(self, file_path: str, search_term: str) -> None:
        """Add a search to history"""
        self.history.append({"file": file_path, "term": search_term})
        
    def get_history(self) -> List[Dict[str, str]]:
        """Return the search history"""
        return self.history
        
    def clear_history(self) -> None:
        """Clear search history"""
        self.history = []
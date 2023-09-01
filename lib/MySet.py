class MySet:
    def __init__(self, enumerable=None):
        # Initialize the set as a dictionary with keys representing elements.
        self.dictionary = {}
        
        # Check if an enumerable (list, tuple, etc.) is provided, and add its elements to the set.
        if enumerable is not None:
            for value in enumerable:
                self.dictionary[value] = True
    
    def has(self, value):
        # Check if a value is in the set.
        return value in self.dictionary
    
    def add(self, value):
        # Add a value to the set as a key in the dictionary.
        self.dictionary[value] = True
        
        # Return the updated set.
        return self
    
    def delete(self, value):
        # Remove a value from the set if it exists.
        self.dictionary.pop(value, None)
        
        # Return the updated set.
        return self
    
    def size(self):
        # Return the number of elements in the set.
        return len(self.dictionary)
    
    def clear(self):
        # Clear all elements from the set.
        self.dictionary.clear()
        
        # Return the cleared set.
        return self
    
    def __str__(self):
        # Return a string representation of the set.
        elements = ','.join(map(str, self.dictionary.keys()))
        return f'MySet: {{{elements}}}'

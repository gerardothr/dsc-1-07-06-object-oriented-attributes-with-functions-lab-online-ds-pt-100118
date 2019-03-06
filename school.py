class School:
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster
        
    def add_student(self, name, grade):
        if str(grade) in self.roster:
            pass
        else:
            self.roster[str(grade)] = []
        self.roster[str(grade)].append(name)
        
    def grade(self, grade):
        return self.roster[str(grade)]
    
    def sort_roster(self):
        for i in self.roster:
            self.roster[i].sort()
        return self.roster

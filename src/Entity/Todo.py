class Todo:
    def __init__(self, plan_id, content, start = None, end = None, checked = False):
        self.id = None
        self.plan_id = plan_id
        self.content = content
        self.start = start
        self.end = end
        self.checked = checked
    
    def getPlanId(self):
        return self.plan_id
    
    def getContent(self):
        return self.content
    
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end

    def getChecked(self):
        return self.checked
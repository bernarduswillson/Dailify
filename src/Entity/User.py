from UserManager import *

class User():
    def __init__(self, userInstance):
        self.id = userInstance[0]
        self.username = userInstance[1]
        self.uncompletedTodos = userInstance[2]
        self.unreachedTargets = userInstance[3]
        self.reachedTargets = userInstance[4]
        self.createdJournals = userInstance[5]
    
    def getName(self):
        return self.username
    
    def setName(self, name):
        self.username = name

    def getUncompletedTodos(self):
        return self.uncompletedTodos
    
    def getUnreachedTargets(self):
        return self.unreachedTargets
    
    def getReachedTargets(self):
        return self.reachedTargets
    
    def getCreatedJournals(self):
        return self.createdJournals
    
    def setCreatedJournals(self, journals):
        self.createdJournals = journals
        UserManager.updateUser(self.id, self)

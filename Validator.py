class Validator:
    def __init__(self, rules, fields):
        self.__rules = rules
        self.__fields = fields
        self.__errors = []
        
    def required(self, field):
        if not(field) in self.__fields or self.__fields[field] == "" or self.__fields[field] == None:
            self.__errors.append("O campo %s é obrigatório." % field)
            return False
        return True
        
    def validate(self):
        for field in self.__rules:
            rulesList = str(self.__rules[field]).split()
            for rule in rulesList:
                validator = getattr(self, rule)
                if validator == None:
                    self.__errors.append("The Validator method '%s' unknown" % rule)
                    continue
                
                validator(field)
                
        return len(self.__errors) == 0
        
    def getErrors(self):
        return self.__errors
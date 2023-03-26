from faker import Faker
fake = Faker()


class BaseClass():
    def __init__(self):
        pass
    
    def parse_config(self,config):
        for a in config.keys():
            setattr(self,a,config[a])
            
    def execute(self,config):
        self.parse_config(config)

class Name(BaseClass):
    def __init__ (self):
        pass
    
    def execute(self,config):
        self.return_value = fake.name()
        super().execute(config)
        self.parse_config(config)
        
        if self.fname_only:
            self.return_value = fake.first_name()
        
        return self.return_value
    
     
class Address(BaseClass):
    def __init__ (self):
        pass
    
    def execute(self,config):
        super().execute(config)
        return fake.address().replace('\n', ' ')
    
class Text(BaseClass):
    def __init__ (self):
        self.ret = fake.text()
    
    def process_text(self):
        types = {
            "word": fake.word(),
            "sentence":fake.sentence(),
            "paragraph":fake.paragraph()
            
        }
        self.ret = types[self.string_type]
        self.ret = self.prefix + self. ret + self.suffix
        if self.upper:
            self.ret = self.ret.upper()
        
    def execute(self,config):
        super().execute(config)
        self.process_text()
        return self.ret


config = {
    
    "name":Name(),
    "address":Address(),
    "text":Text()
}

def runner(payload):
    errors = []
    result = {}
    for key in payload.keys():
        handler_class = config[payload[key]['entity']]
        result[key] = handler_class.execute(payload[key])
    
    if errors != [] :
        return errors
    else:
        return result
        
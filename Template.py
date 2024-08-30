class Header:
    def __init__(self, name, data_type, mandatory, template_type, template_name):
        self.name = name
        self.data_type = data_type
        self.mandatory = mandatory
        self.template_type = template_type
        self.template_name = template_name
    
    def __repr__(self):
        return (f"Header(Name={self.name}, DataType={self.data_type}, Mandatory={self.mandatory}, TemplateType={self.template_type}, TemplateName={self.template_name})")

class Template:
    def __init__(self, template_type, template_name):
        self.template_type = template_type
        self.template_name = template_name
        self.headers = []

    def add_header(self, name, data_type, mandatory):
        header = Header(name, data_type, mandatory, self.template_type, self.template_name)
        self.headers.append(header)

    def __repr__(self):
        return (f"Template(Type={self.template_type}, Name={self.template_name},Headers={self.headers})")

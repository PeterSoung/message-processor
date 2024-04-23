class Company:

    def __init__(self, company_name, company_id):
        self.company_name = company_name
        self.company_id = company_id

    def get_company_name(self):
        return self.company_name

    def get_company_id(self):
        return self.company_id

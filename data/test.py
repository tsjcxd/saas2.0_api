

class TestStatus:

    def __init__(self):
        self.conn = self.connection()

    def connection(self):
        return coon


    def insert(self):
        self.conn.insert_sql(sql)


    def update(self):
        self.conn.update_sql(sql)


    def select(self):
        self.conn.select_sql(sql)


    # def __init__(self):
    #     self.status =0
    
    # def first_status(self):
    #     if self.status == 0:
    #         self.status = 1
        
    # def second_status(self):
    #     if self.status == 1:
    #         self.status = 2
    #     else:
    #         print("status not 1.")
    
    # def third_status(self):
    #     if self.status == 2:
    #         self.status = 3
        
    #     else:
    #         print("status not 2")

    def first_status(self):
        status = 1
        return status
    
    def second_status(self):

        status = self.first_status()
        if status == 1:
            return 2
    
    def third_status(self):
        stauts = self.second_status()
        if stauts == 2:
            return 3

if __name__ == "__main__":
    s = TestStatus()
    # print("init: {}".format(s.status))
    status = s.first_status()
    print("first: {}".format(status))
    status = s.second_status()
    print("second: {}".format(status))
    status = s.third_status()
    print("third: {}".format(status))
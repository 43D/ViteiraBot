from viteirabot.dao.daoMaster import DaoMaster
from viteirabot.entity.template import Template

class DaoTemplate:
    def __init__(self, dao: DaoMaster):
        self.dao = dao
        self.cursor = self.dao.getCursor()

    def func_example_save(self, t: Template):
        print("teste save template")
        print(t)

    def close(self):
        self.dao.close()
from UI自动化框架2.page1.app1 import App


class TestXueQiu:
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()



    def test_search(self):
        self.search.search("阿里巴巴-SW")
        assert self.search.is_choose("阿里巴巴-SW")
class FakeDocIdManager:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    """ Mock data to supply a list of all docIDs in the system"""
    @staticmethod
    def get_all_id():
        return ['0', '1', '2']

import unittest
from create_project_for_stock_analy import execute_feature

class TestCreateProjectForStockAnaly(unittest.TestCase):
    def test_feature_execution(self):
        res = execute_feature()
        self.assertEqual(res["status"], "success")
        self.assertTrue(res["ready"])

if __name__ == "__main__":
    unittest.main()

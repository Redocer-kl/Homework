import Runner
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.guy1 = Runner.Runner("Усейн", 10)
        self.guy2 = Runner.Runner("Андрей", 9)
        self.guy3 = Runner.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(f"{result} : {cls.all_results[result]}")


    def test_run1(self):
        t1 = Runner.Tournament(90, self.guy1, self.guy3)
        self.all_results.update(t1.start())
        self.assertTrue(self.all_results[2] == "Ник")

    def test_run2(self):
        t1 = Runner.Tournament(90, self.guy2, self.guy3)
        self.all_results.update(t1.start())
        self.assertTrue(self.all_results[2] == "Ник")

    def test_run3(self):
        t1 = Runner.Tournament(90, self.guy1, self.guy2, self.guy3)
        self.all_results.update(t1.start())
        self.assertTrue(self.all_results[3] == "Ник")


if __name__ == "__main__":
    unittest.main()

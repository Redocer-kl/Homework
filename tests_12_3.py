import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        guy = Runner.Runner("Chill guy")
        for i in range(10):
            guy.walk()
        self.assertEqual(guy.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        guy = Runner.Runner("Chill guy")
        for i in range(10):
            guy.run()
        self.assertEqual(guy.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        guy1 = Runner.Runner("Chill guy")
        guy2 = Runner.Runner("Chill guy")
        for i in range(10):
            guy1.walk()
            guy2.run()
        self.assertNotEqual(guy1.distance, guy2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run1(self):
        t1 = Runner.Tournament(90, self.guy1, self.guy3)
        self.all_results.update(t1.start())
        self.assertTrue(self.all_results[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run2(self):
        t1 = Runner.Tournament(90, self.guy2, self.guy3)
        self.all_results.update(t1.start())
        self.assertTrue(self.all_results[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run3(self):
        t1 = Runner.Tournament(90, self.guy1, self.guy2, self.guy3)
        self.all_results.update(t1.start())
        self.assertTrue(self.all_results[3] == "Ник")


if __name__ == "__main__":
    unittest.main()
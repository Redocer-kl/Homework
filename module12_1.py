import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        guy = Runner.Runner("Chill guy")
        for i in range(10):
            guy.walk()
        self.assertEqual(guy.distance, 50)

    def test_run(self):
        guy = Runner.Runner("Chill guy")
        for i in range(10):
            guy.run()
        self.assertEqual(guy.distance, 100)

    def test_challenge(self):
        guy1 = Runner.Runner("Chill guy")
        guy2 = Runner.Runner("Chill guy")
        for i in range(10):
            guy1.walk()
            guy2.run()
        self.assertNotEqual(guy1.distance, guy2.distance)

if __name__ == "__main__":
    unittest.main()
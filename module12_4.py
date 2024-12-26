import logging
import Runner
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            guy = Runner.Runner("Chill guy", -10)
            for i in range(10):
                guy.walk()
            self.assertEqual(guy.distance, 50)
            logging.info("test_walk выполнен успешно")
        except Exception as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            guy = Runner.Runner(12, 5)
            for i in range(10):
                guy.run()
            self.assertEqual(guy.distance, 100)
            logging.info("test_run выполнен успешно")
        except Exception as e:
            logging.warning( "Неверный тип данных для объекта Runner")

    def test_challenge(self):
        guy1 = Runner.Runner("Chill guy")
        guy2 = Runner.Runner("Chill guy")
        for i in range(10):
            guy1.walk()
            guy2.run()
        self.assertNotEqual(guy1.distance, guy2.distance)


if __name__ == "__main__":
    unittest.main()
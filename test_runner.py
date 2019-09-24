import unittest
from tigr.test.test_drawer import TestCaseDrawer
from tigr.test.test_reader import TestCaseSourceReader
from tigr.test.test_turtle import TestCaseTurtleWorker
from tigr.test.test_tkinter import TestCaseTkinterWorker
from tigr.test.test_peg_parser import TestCasePegParser



the_suite = unittest.TestSuite()

the_suite.addTest(unittest.makeSuite(TestCaseDrawer))
the_suite.addTest(unittest.makeSuite(TestCaseSourceReader))
the_suite.addTest(unittest.makeSuite(TestCaseTkinterWorker))
the_suite.addTest(unittest.makeSuite(TestCaseTurtleWorker))
the_suite.addTest(unittest.makeSuite(TestCasePegParser))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(the_suite)



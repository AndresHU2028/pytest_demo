import unittest
import sys

sys.path.append("/home/codio/workspace/") 
from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

  def test_Normal_case_3x3(self):
    grid = [["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]]
    dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["abc", "abdhi", "cfi", "dea"]
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_Normal_case_4x4(self):
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"], ["G", "Z", "Q", "R"], ["O", "N", "T", "A"]]
    dictionary = ["WENT", "TEN", "NET"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["WENT", "TEN", "NET"]
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_Scalability_case_5x5(self):
    grid = [["A" for _ in range(5)] for _ in range(5)]
    dictionary = ["AAAAA"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["AAAAA"]
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_Scalability_case_6x6(self):
    grid = [["X" for _ in range(6)] for _ in range(6)]
    grid[0][0], grid[0][1], grid[0][2] = "B", "U", "G"
    dictionary = ["BUG"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["BUG"]
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_Scalability_case_7x7(self):
    grid = [["S" for _ in range(7)] for _ in range(7)]
    dictionary = ["SSSSSS"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["SSSSSS"]
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_Scalability_case_13x13(self):
    grid = [["Z" for _ in range(13)] for _ in range(13)]
    grid[0][0], grid[0][1], grid[0][2] = "B", "I", "G"
    dictionary = ["BIG"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["BIG"]
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

class TestSuite_Simple_Edge_Cases(unittest.TestCase):

  def test_SquareGrid_case_1x1(self):
    grid = [["A"]]
    dictionary = ["a", "b", "c"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_EmptyGrid_case_0x0(self):
    grid = [[]]
    dictionary = ["hello", "there"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_EmptyDictionary_case(self):
    grid = [["A", "B"], ["C", "D"]]
    dictionary = []
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

class TestSuite_Complete_Coverage(unittest.TestCase):

  def test_Tile_Reuse_case(self):  
    grid = [["A", "B"], ["C", "D"]]
    dictionary = ["ABA"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_NonSquare_Grid_case(self):
    grid = [["A", "B", "C"], ["D", "E", "F"]]
    dictionary = ["ABC"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

class TestSuite_Qu_and_St(unittest.TestCase):

  def test_Qu_Handling_case(self): 
    # Rearranged grid so letters for QUARTZ are adjacent
    # Q(0,0) -> A(0,1) -> R(0,2) -> T(1,2) -> Z(1,1)
    grid = [
        ["Q", "A", "R"], 
        ["X", "Z", "T"], 
        ["X", "X", "X"]
    ]
    dictionary = ["QUARTZ"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["QUARTZ"]
    expected = [x.upper() for x in expected]
    self.assertEqual(sorted(expected), sorted(solution))

  def test_St_Handling_case(self): 
    grid = [["ST", "A", "R"], ["X", "X", "X"], ["X", "X", "X"]]
    dictionary = ["STAR"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["STAR"]
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

if __name__ == '__main__':
  unittest.main()
  

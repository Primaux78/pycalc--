import unittest
import pycalc.pycalc as calculator

class PyCalcUnitTests(unittest.TestCase):
  def add(a, b):
    res = a
    if b > 0:
        while (b - 1) >= 0:
            b -= 1
            res += 1
    elif b < 0:
        while (b + 1) <= 0:
            b += 1
            res -= 1
    return res

  
  def test_add(self):
    left = [5]
    right = [9]
    expected = [14]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.add(l, r)
        self.assertEqual(got, e)

if __name__ == '__main__':
  unittest.main()

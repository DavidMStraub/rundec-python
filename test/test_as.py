import unittest
import rundec

class Alphas(unittest.TestCase):
    def test_AlL2AlH(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mtop = 173.0

      top    = rundec.TriplenfMmu()
      bottom = rundec.TriplenfMmu()

      top.nf   = 6
      top.Mth  = 173.0
      top.muth = 173.0

      bottom.nf = 5
      bottom.Mth = 4.8
      bottom.muth = 4.8


      dec = rundec.TriplenfMmuArray(4)
      dec[0] = top

      loops = 5
      self.assertAlmostEqual(crd.AlL2AlH(asMZ,MZ,dec,800.,loops),0.090493107274928766401,delta=1e-5)

      dec[0] = top
      dec[1] = bottom
      self.assertAlmostEqual(crd.AlL2AlH(0.22,4.,dec,800.,loops),0.089296507041035146862,delta=1e-5)
    
    def test_AlH2AlL(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mtop = 173.0

      top    = rundec.TriplenfMmu()
      bottom = rundec.TriplenfMmu()

      top.nf   = 6
      top.Mth  = 173.0
      top.muth = 173.0

      bottom.nf = 5
      bottom.Mth = 4.8
      bottom.muth = 4.8

      dec = rundec.TriplenfMmuArray(4)
      dec[0] = top

      loops = 5
      self.assertAlmostEqual(crd.AlH2AlL(0.090,800,dec,MZ,loops),0.1170572315,delta=1e-5)

      dec[0] = top
      dec[1] = bottom
      self.assertAlmostEqual(crd.AlH2AlL(0.090,800,dec,4.0,loops),0.2245399988,delta=1e-5)

    def test_AlphasExact(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mbMS = 4.18
      
      nf = 5

      loops = 5
      self.assertAlmostEqual(crd.AlphasExact(asMZ, MZ, mbMS, nf, loops),0.224248705,delta=1e-5)

      loops = 4
      self.assertAlmostEqual(crd.AlphasExact(asMZ, MZ, mbMS, nf, loops),0.2242363603,delta=1e-5)

      loops = 3
      self.assertAlmostEqual(crd.AlphasExact(asMZ, MZ, mbMS, nf, loops),0.2239618329,delta=1e-5)

      loops = 2
      self.assertAlmostEqual(crd.AlphasExact(asMZ, MZ, mbMS, nf, loops),0.2232085998,delta=1e-5)

      loops = 1
      self.assertAlmostEqual(crd.AlphasExact(asMZ, MZ, mbMS, nf, loops),0.2118462908,delta=1e-5)

      loops = 5
      nf = 4
      self.assertAlmostEqual(crd.AlphasExact(asMZ, MZ, mbMS, nf, loops),0.2493330857,delta=1e-5)

      nf = 3
      self.assertAlmostEqual(crd.AlphasExact(asMZ, MZ, mbMS, nf, loops),0.2825081752,delta=1e-5)

    def test_AlphasLam(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mbMS = 4.18
      mtop = 173
      Lambda = 0.2074569921

      loops = 5
      nf = 5
      self.assertAlmostEqual(crd.AlphasLam(Lambda, MZ, nf, loops),0.1178938389,delta=1e-5)

      loops = 3
      nf = 3
      self.assertAlmostEqual(crd.AlphasLam(Lambda, MZ, nf, loops),0.09811687777,delta=1e-5) 

      loops = 5
      nf = 5
      self.assertAlmostEqual(crd.AlphasLam(Lambda, mtop, nf, loops),0.1075199029,delta=1e-5)


  

if __name__ == '__main__':
   unittest.main()
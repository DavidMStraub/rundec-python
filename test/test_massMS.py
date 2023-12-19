import unittest
import rundec

class masses(unittest.TestCase):
    def test_mMS2mOS(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mbMS = 4.18
      scale_mbMS = mbMS
      mcMS = rundec.RunDecPair()
      mq = rundec.RunDecPairArray(4)

      #Calculate alpha_s at mbMS

      as5 = crd.AlphasExact(asMZ, MZ, mbMS, 5, 5)

      #Calculate on-shell bottom quark mass from MS-bar bottom quark mass.
      #without charm mass effects

      loops = 4
      nf = 5
      self.assertAlmostEqual(crd.mMS2mOS(mbMS,None,as5,scale_mbMS,nf,loops),5.053056783,delta=1e-5)

      #with charm mass effects

      mcMS.first = 0.993
      mcMS.second = 3.0
      mq[0] = mcMS
      
      loops = 4
      self.assertAlmostEqual(crd.mMS2mOS(mbMS,mq,as5,scale_mbMS,nf,loops),5.075469604,delta=1e-5)

      loops = 3
      self.assertAlmostEqual(crd.mMS2mOS(mbMS,mq,as5,scale_mbMS,nf,loops),4.941379483,delta=1e-5)
            
      loops = 2
      self.assertAlmostEqual(crd.mMS2mOS(mbMS,mq,as5,scale_mbMS,nf,loops),4.782817403,delta=1e-5)

    def test_mOS2mMS(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mtop = 173.0
      scale_mtopMS = 163.0
      mbMS = rundec.RunDecPair()
      mcMS= rundec.RunDecPair()
      mq = rundec.RunDecPairArray(4)

      #Calculate MS mass of top quark mass from on-shell mass.
      #without bottom and charm mass effects

      top    = rundec.TriplenfMmu()

      top.nf   = 6
      top.Mth  = 173.0
      top.muth = 173.0

      dec = rundec.TriplenfMmuArray(4)
      dec[0] = top
      loops = 5
      
      as6 = crd.AlL2AlH(asMZ,MZ,dec,scale_mtopMS,loops)
 
      nf = 6
      loops = 4
      self.assertAlmostEqual(crd.mOS2mMS(mtop,None,as6,scale_mtopMS,nf,loops),163.2257536,delta=1e-5)

      #include bottom mass effects

      mbMS.first  = 4.18
      mbMS.second = 4.18
      mq[0] = mbMS
      self.assertAlmostEqual(crd.mOS2mMS(mtop,mq,as6,scale_mtopMS,nf,loops),163.2071241,delta=1e-5)      
                             
      #include bottom and charm effects
                             
      mcMS.first  = 0.993
      mcMS.second = 3.0
      mq[0] = mbMS
      mq[1] = mcMS

      self.assertAlmostEqual(crd.mOS2mMS(mtop,mq,as6,scale_mtopMS,nf,loops),163.2015983,delta=1e-5)


    def test_mThr2mMS(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mbMS = 4.18
      scale_mbMS = mbMS
      mcMS = 1.3
      scale_mcMS = 1.3

      #run down to 2*mbMS
      astmp = crd.AlphasExact(asMZ,MZ,2*mbMS,5,5)
      #decouple as5 -> as4
      astmp = crd.DecAsDownSI(astmp,mbMS,2*mbMS,4,5)
      #run down to 3 GeV
      astmp= crd.AlphasExact(astmp,2*mbMS,3.0,4,5)
      #decouple as4 -> as3
      as3 = crd.DecAsDownSI(astmp,mcMS,3.0,3,5)

      self.assertAlmostEqual(as3,0.2444637693,delta=1e-5)

      #convert PS mass to MS mass
      mcPS = 1.153
      scale_mpPS = 2.0
      self.assertAlmostEqual(crd.mPS2mMS(mcPS,None,as3,3.0,scale_mpPS,3,4),0.9862692441,delta=1e-5)
     
      #convert 1S mass to MS mass
      mc1S = 1.5145
      self.assertAlmostEqual(crd.m1S2mMS(mc1S,None,as3,3.0,3,4),0.9575677386,delta=1e-5)

      #convert RS mass to MS mass
      mcRS = 1.043
      self.assertAlmostEqual(crd.mRS2mMS(mcRS,None,as3,3.0,2.0,3,4),1.006783427,delta=1e-5)

      #convert RS' mass to MS mass
      mcRSp = 1.357
      self.assertAlmostEqual(crd.mRSp2mMS(mcRSp,None,as3,3.0,2.0,3,4),0.9661584143,delta=1e-5)

    def test_mMS2mThr(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mbMS = 4.18
      scale_mbMS = mbMS

      #run down to 2*mbMS
      astmp = crd.AlphasExact(asMZ,MZ,2*mbMS,5,5)
      #decouple as5 -> as4
      astmp= crd.DecAsDownSI(astmp,mbMS,2*mbMS,4,5)
      #run down to mbMS
      as4= crd.AlphasExact(astmp,2*mbMS,mbMS,4,5)

      #convert MS mass to PS mass
      self.assertAlmostEqual(crd.mMS2mPS(mbMS,None,as4,mbMS,2.0,4,4),4.498302237,delta=1e-5)
     
      #convert MS mass to 1S mass
      self.assertAlmostEqual(crd.mMS2m1S(mbMS,None,as4,mbMS,4,4),4.684559198,delta=1e-5)

      #convert MS mass to RS mass
      self.assertAlmostEqual(crd.mMS2mRS(mbMS,None,as4,mbMS,2.0,4,4),4.348011645,delta=1e-5)

      #convert MS mass to RS' mass
      self.assertAlmostEqual(crd.mMS2mRSp(mbMS,None,as4,mbMS,2.0,4,4),4.74021953,delta=1e-5)

    def test_mMS2mkin(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mbMS = 4.163
      scale_mbMS = mbMS
      mcMS = rundec.RunDecPair()
      mq = rundec.RunDecPairArray(4)

      #run down to 2*mbMS
      astmp = crd.AlphasExact(asMZ,MZ,2*mbMS,5,5)
      #decouple as5 -> as4
      astmp= crd.DecAsDownSI(astmp,mbMS,2*mbMS,4,5)
      #run down to mbMS
      as4= crd.AlphasExact(astmp,2*mbMS,mbMS,4,5)

      mcMS.first = 0.993
      mcMS.second = 3.0
      mq[0] = mcMS
      loops = 3
      muWC = 1.0
      #convert MS mass to kinetic mass, scheme A
      scheme=0
      self.assertAlmostEqual(crd.mMS2mKIN(mbMS,mcMS,as4,mbMS,muWC,loops,scheme),4.541932121,delta=1e-5)
      #convert MS mass to kinetic mass, scheme B
      scheme=1
      self.assertAlmostEqual(crd.mMS2mKIN(mbMS,mcMS,as4,mbMS,muWC,loops,scheme),4.525651485,delta=1e-5)  
      #convert MS mass to kinetic mass, scheme C
      scheme=2
      self.assertAlmostEqual(crd.mMS2mKIN(mbMS,mcMS,as4,mbMS,muWC,loops,scheme),4.547027037,delta=1e-5)
      #convert MS mass to kinetic mass, scheme D
      scheme=3
      self.assertAlmostEqual(crd.mMS2mKIN(mbMS,mcMS,as4,mbMS,muWC,loops,scheme),4.543448616,delta=1e-5) 

    def test_mkin2mMS(self):
      crd = rundec.CRunDec()
      asMZ = 0.1179
      MZ = 91.1876
      mbkin = 4.550
      mbMS = 4.163
      muWC = 1.0
      mcMS = rundec.RunDecPair()
      mq = rundec.RunDecPairArray(4)

      #run down to 2*mbMS
      astmp = crd.AlphasExact(asMZ,MZ,2*mbMS,5,5)
      #decouple as5 -> as4
      astmp= crd.DecAsDownSI(astmp,mbMS,2*mbMS,4,5)
      #run down to mbMS
      as4= crd.AlphasExact(astmp,2*mbMS,mbkin,4,5)

      #run as4 to 3.0 GeV
      astmp=crd.AlphasExact(astmp,2*mbMS,3.0,4,5)
      #decouple as4 -> as3
      astmp=crd.DecAsDownMS(astmp,0.993,3.0,3,5)
      #run as3 to mbkin
      as3=crd.AlphasExact(astmp,3.0,mbkin,3,5)

      mcMS.first = 0.993
      mcMS.second = 3.0
      mq[0] = mcMS
      loops = 3
      muWC = 1.0

      #convert kinetic mass to MS mass, scheme A
      scheme=0
      self.assertAlmostEqual(crd.mKIN2mMS(mbkin,mcMS,as3,mbkin,muWC,loops,scheme),4.134409357,delta=1e-5)

      #convert kinetic mass to MS mass, scheme B
      scheme=1
      self.assertAlmostEqual(crd.mKIN2mMS(mbkin,mcMS,as4,mbkin,muWC,loops,scheme),4.126363246,delta=1e-5)

      #convert kinetic mass to MS mass, scheme C
      scheme=2
      self.assertAlmostEqual(crd.mKIN2mMS(mbkin,mcMS,as4,mbkin,muWC,loops,scheme),4.106094652,delta=1e-5)

      #convert kinetic mass to MS mass, scheme D
      scheme=3
      self.assertAlmostEqual(crd.mKIN2mMS(mbkin,mcMS,as3,mbkin,muWC,loops,scheme),4.134150911,delta=1e-5)

if __name__ == '__main__':

   unittest.main()
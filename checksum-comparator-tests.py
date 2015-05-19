from unittest import TestCase, TestLoader, TextTestRunner
from checksumcomparator import ChecksumCompare

class ChecksumComparatorTests(TestCase):

   def setup(self):
      self.compare = ChecksumCompare()

      self.big_list = ["e0861941c1ac038836097a8f2a3e729482fe1acd E3/Speeches/1 Community & Voluntary Sector/2007/Deptnotes/First AGM Speech1220415DA - speech.doc",
         "318e91cdfca61d11a250a907bad6fd039c91b5d0 E3/Speeches/1 Community & Voluntary Sector/2007/1229032DA - Digital Future Summit Speech Notes - revised DRAFT.doc",
         "203a7c3aebf65f93552774accd7fa268a587667b E3/Speeches/1 Community & Voluntary Sector/2007/1234400DA - Briefing Release of COGS Profile 2006-07.dot"]

      self.small_list = ["e0861941c1ac038836097a8f2a3e729482fe1acd E3/Speeches/1 Community & Voluntary Sector/2007/Deptnotes/First AGM Speech1220415DA - speech.doc", \
         "318e91cdfca61d11a250a907bad6fd039c91b5d0 E3/Speeches/1 Community & Voluntary Sector/2007/1229032DA - Digital Future Summit Speech Notes - revised DRAFT.doc"] 
   
      self.odd_one_out = "203a7c3aebf65f93552774accd7fa268a587667b E3/Speeches/1 Community & Voluntary Sector/2007/1234400DA - Briefing Release of COGS Profile 2006-07.dot"
   
   def test_sizing(self):
      self.setup()
   
      bigger_list = self.compare.order_by_size(self.big_list, self.small_list)[self.compare.BIGGER]
      
      #Do we get the list back that we expect, verbatim...
      self.assertEqual(bigger_list, set(self.big_list)) 
      
      #Ensure we're not getting something else...
      self.assertNotEqual(bigger_list, set(self.small_list))
      
   def test_differences(self):
      self.setup()
      lists = self.compare.order_by_size(self.big_list, self.small_list)
      diff = self.compare.__getDiff__(lists)
      
      #We know we're only expecting one result, compare.
      self.assertEqual(diff[0], self.odd_one_out)
      
def main():
	suite = TestLoader().loadTestsFromTestCase(ChecksumComparatorTests)
	TextTestRunner().run(suite)
	
if __name__ == "__main__":
	main()
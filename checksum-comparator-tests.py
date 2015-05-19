from unittest import TestCase, TestLoader, TextTestRunner
from checksumcomparator import ChecksumCompare

class ChecksumComparatorTests(TestCase):

   def setup(self):
      self.compare = ChecksumCompare()

      self.big_list = ["e0861941c1ac038836097a8f2a3e729482fe1acd Files/Data/Open Data Community/2007/Data Processing/Speech.doc",
         "318e91cdfca61d11a250a907bad6fd039c91b5d0 Files/Data/Open Data Community/2007/0024601DA - Web of Objects - DRAFT.doc",
         "203a7c3aebf65f93552774accd7fa268a587667b Files/Data/Open Data Community/2007/2006-07-Collaboration-Template.dot"]

      self.small_list = ["e0861941c1ac038836097a8f2a3e729482fe1acd Files/Data/Open Data Community/2007/Data Processing/Speech.doc", \
         "318e91cdfca61d11a250a907bad6fd039c91b5d0 Files/Data/Open Data Community/2007/0024601DA - Web of Objects - DRAFT.doc"] 
   
      self.odd_one_out = "203a7c3aebf65f93552774accd7fa268a587667b Files/Data/Open Data Community/2007/2006-07-Collaboration-Template.dot"
   
   #Vital that the smaller set it compared to the bigger set to test for inclusion, and no change for remaining objects
   #Example, pre-distillation: bigger list (all objects received), post-distillation: smaller list (we've removed objects)
   def test_sizing(self):
      self.setup()
   
      bigger_list = self.compare.order_by_size(self.big_list, self.small_list)[self.compare.BIGGER]
      
      #Do we get the list back that we expect, verbatim...
      self.assertEqual(bigger_list, set(self.big_list)) 
      
      #Ensure we're not getting something else...
      self.assertNotEqual(bigger_list, set(self.small_list))
    
   #Test that the differences we see are the differences that we're expecting
   def test_differences(self):
      self.setup()
      
      #Create ordered lists... 
      lists = self.compare.order_by_size(self.big_list, self.small_list)
      
      #Get diff and same lists...
      diff = self.compare.__getDiff__(lists)
      same = self.compare.__getSame__(lists)
      
      #We know we're only expecting one result, compare...
      self.assertEqual(diff[0], self.odd_one_out)
      
      #And double confirm value is not in samelist...

      self.assertTrue(self.odd_one_out in diff and self.odd_one_out not in same)

   #Lists are allowed to be equal, so ensure equivalence works.
   def test_identical_lists(self):
      self.setup()
      
      len_compare = len(self.big_list)
      ZERO = 0
      
      #Create ordered lists... 
      lists = self.compare.order_by_size(self.big_list, self.big_list)
      
      #Get diff and same lists...
      diff = self.compare.__getDiff__(lists)
      same = self.compare.__getSame__(lists)
      
      #Test difference list is zero...
      self.assertEqual(len(diff), ZERO)
      self.assertNotEqual(len(diff), len_compare)
      
      #Test same list is the what we're expecting (len(self.big_list) == 3)
      self.assertEqual(len(same), len_compare)
      self.assertNotEqual(len(same), ZERO)
        
def main():
	suite = TestLoader().loadTestsFromTestCase(ChecksumComparatorTests)
	TextTestRunner().run(suite)
	
if __name__ == "__main__":
	main()
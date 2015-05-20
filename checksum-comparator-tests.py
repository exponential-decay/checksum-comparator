from unittest import TestCase, TestLoader, TextTestRunner
from checksumcomparator import ChecksumCompare

class ChecksumComparatorTests(TestCase):

   def setup(self):
      self.compare = ChecksumCompare()

      # MOCK CSV STRUCTURE FOR TESTING
      self.big_list_csv = [["e0861941c1ac038836097a8f2a3e729482fe1acd","Files/Data/Open Data Community/2007/Data Processing/Speech.doc"],
         ["318e91cdfca61d11a250a907bad6fd039c91b5d0","Files/Data/Open Data Community/2007/0024601DA - Web of Objects - DRAFT.doc"],
         ["203a7c3aebf65f93552774accd7fa268a587667b","Files/Data/Open Data Community/2007/2006-07-Collaboration-Template.dot"]]

      self.big_list_pre_csv = [["e0861941c1ac038836097a8f2a3e729482fe1acd","Files/Data/Open Data Community/2007/Data Processing/Speech.dot"],
         ["318e91cdfca61d11a250a907bad6fd039c91b5d0","Files/Data/Open Data Community/2007/0024601DA - Web of Objects - DRAFT.dot"],
         ["203a7c3aebf65f93552774accd7fa268a587667b","Files/Data/Open Data Community/2007/2006-07-Collaboration-Template.doc"]]

      # CONVERTED LISTS FOR TESTING
      self.huge_list = ["e0861941c1ac038836097a8f2a3e729482fe1acd Files/Data/Open Data Community/2007/Data Processing/Speech.doc",
         "318e91cdfca61d11a250a907bad6fd039c91b5d0 Files/Data/Open Data Community/2007/0024601DA - Web of Objects - DRAFT.doc",
         "203a7c3aebf65f93552774accd7fa268a587667b Files/Data/Open Data Community/2007/2006-07-Collaboration-Template.dot",
         "eafbb61269b1623a868b9927506a27eeb0ea4ac8,Files/Non-data/Unit Testing/Industrial Data.doc",
         "1f844ce0afe0e14199ad6249e3140b0d1298e41a,Files/Non-data/Unit Testing/Digital Preservation Guidelines.doc",
         "e73964c528aa2dff7f1b0e032b37890deb116b3f,Files/Non-data/Unit Testing/2015-05-19-data.doc",
         "29a684474a508657c63adea9a08765fd07c0bb1a,Files/Non-data/Unit Testing/1f844ce0afe0e14199ad6249e3140b0d1298e41a.cs",
         "04975ddebf7cd90871169fca382d76b155ba891e,Files/Non-data/Unit Testing/optical storage guidance.doc",
         "e799b815fe815e66893b841e283e5f0ea90d7532,Files/Non-data/Unit Testing/process documentation.doc",
         "ede775ec22480873e558e3561adf4c9d709e52db,Files/Non-data/Unit Testing/process documentation-template.dot",
         "ae51ac3d1239d8db00b0d12d055142dde24f3bbb,Files/Non-data/Unit Testing/list of incorrect objects.doc",
         "a4dd72241ce70e3a3cb0a80c7aaa7a98f33c935d,Files/Non-data/Unit Testing/2007/a file.doc",
         "45ecb934283da3f5c6bda6640109b07f9166a7af,Files/Non-data/Unit Testing/2007/the last word.doc"]

      self.small_list = ["e0861941c1ac038836097a8f2a3e729482fe1acd Files/Data/Open Data Community/2007/Data Processing/Speech.doc", \
         "318e91cdfca61d11a250a907bad6fd039c91b5d0 Files/Data/Open Data Community/2007/0024601DA - Web of Objects - DRAFT.doc"] 
   
      self.odd_one_out = "203a7c3aebf65f93552774accd7fa268a587667b Files/Data/Open Data Community/2007/2006-07-Collaboration-Template.dot"

      self.bigger_odd_one_out = ["203a7c3aebf65f93552774accd7fa268a587667b Files/Data/Open Data Community/2007/2006-07-Collaboration-Template.dot",
         "eafbb61269b1623a868b9927506a27eeb0ea4ac8,Files/Non-data/Unit Testing/Industrial Data.doc",
         "1f844ce0afe0e14199ad6249e3140b0d1298e41a,Files/Non-data/Unit Testing/Digital Preservation Guidelines.doc",
         "e73964c528aa2dff7f1b0e032b37890deb116b3f,Files/Non-data/Unit Testing/2015-05-19-data.doc",
         "29a684474a508657c63adea9a08765fd07c0bb1a,Files/Non-data/Unit Testing/1f844ce0afe0e14199ad6249e3140b0d1298e41a.cs",
         "04975ddebf7cd90871169fca382d76b155ba891e,Files/Non-data/Unit Testing/optical storage guidance.doc",
         "e799b815fe815e66893b841e283e5f0ea90d7532,Files/Non-data/Unit Testing/process documentation.doc",
         "ede775ec22480873e558e3561adf4c9d709e52db,Files/Non-data/Unit Testing/process documentation-template.dot",
         "ae51ac3d1239d8db00b0d12d055142dde24f3bbb,Files/Non-data/Unit Testing/list of incorrect objects.doc",
         "a4dd72241ce70e3a3cb0a80c7aaa7a98f33c935d,Files/Non-data/Unit Testing/2007/a file.doc",
         "45ecb934283da3f5c6bda6640109b07f9166a7af,Files/Non-data/Unit Testing/2007/the last word.doc"]

      self.big_list = ["e0861941c1ac038836097a8f2a3e729482fe1acd Files/Data/Open Data Community/2007/Data Processing/Speech.doc",
         "318e91cdfca61d11a250a907bad6fd039c91b5d0 Files/Data/Open Data Community/2007/0024601DA - Web of Objects - DRAFT.doc",
         "203a7c3aebf65f93552774accd7fa268a587667b Files/Data/Open Data Community/2007/2006-07-Collaboration-Template.dot"]

      self.big_list_pre = ["e0861941c1ac038836097a8f2a3e729482fe1acd Files/Data/Open Data Community/2007/Data Processing/Speech.dot",
         "318e91cdfca61d11a250a907bad6fd039c91b5d0 Files/Data/Open Data Community/2007/0024601DA - Web of Objects - DRAFT.dot",
         "203a7c3aebf65f93552774accd7fa268a587667b Files/Data/Open Data Community/2007/2006-07-Collaboration-Template.doc"]

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
      
      even_bigger_list = self.compare.order_by_size(self.huge_list, self.big_list)[self.compare.BIGGER]
      
      #Do we get the list back that we expect, verbatim...
      self.assertEqual(even_bigger_list, set(self.huge_list)) 
      
      #Ensure we're not getting something else...
      self.assertNotEqual(even_bigger_list, set(self.big_list))
    
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

      #Testing with additional lists...
      #Create ordered lists... use the largest list and biggest list
      lists = self.compare.order_by_size(self.huge_list, self.small_list)
      
      #Get diff and same lists...
      diff = self.compare.__getDiff__(lists)
      same = self.compare.__getSame__(lists)
      
      #We know we're only expecting one result, compare...
      self.assertEqual(diff, list(set(self.bigger_odd_one_out)))
      
      #And double confirm value is not in samelist...
      self.assertTrue(self.bigger_odd_one_out[0] in diff and self.bigger_odd_one_out[6] not in same)

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

   # If we're stripping filename extensions then test the capability to compare
   def test_pre_conditioned_objects(self):
      self.setup()
      
      len_compare = len(self.big_list_csv)
      ZERO = 0
      
      #lists need to simulate CSV
      #not mocking a csv file...
      big_list = self.compare.preconditionlist(self.big_list_csv, True)
      big_list_pre = self.compare.preconditionlist(self.big_list_pre_csv, True)
            
      #identical list code, but pre-conditioned
      #Create ordered lists... 
      lists = self.compare.order_by_size(big_list, big_list_pre)
      
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
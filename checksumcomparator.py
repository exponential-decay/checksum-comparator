import datetime
import argparse
import csv
import sys

class ChecksumCompare:

   BIGGER = 0
   SMALLER = 1

   def outputformattedtext(self, check1, check2, same, diff, verbose):
      sys.stdout.write("File 1: " + check1 + "\nFile 2: " + check2 + "\n\nChecksum comparison: " +  str(datetime.datetime.now()) + "\n\n")
      
      sys.stdout.write("Matching objects: " + str(len(same)) + "\n")
      sys.stdout.write("Differing objects: " + str(len(diff)) + "\n")

      sys.stdout.write("\n")
      sys.stdout.write("Different objects: \n")
      for d in diff:
         sys.stdout.write(d + "\n")
      
      if verbose:
         sys.stdout.write("\n")
         sys.stdout.write("Identical objects: \n")
         for d in same:
            sys.stdout.write(d + "\n")

   def returncsvaslist(self, csvfile, pre):
      list = []
      with open(csvfile, 'rb') as csvfile1: 
         list1 = csv.reader(csvfile1, delimiter=',')
         for item in list1: 
            if pre:
               row = item[0] + " " + item[1].rsplit('.', 1)[0]
            else:
               row = item[0] + " " + item[1]
            list.append(row)
      return list

   def order_by_size(self, csvlist1, csvlist2):
      #bigger should be non-distilled list
      #smaller will be distilled
      #equal, will be a staightforward comparison
      
      if len(csvlist1) > len(csvlist2):
         bigger = set(csvlist1)
         smaller = set(csvlist2)
      elif len(csvlist2) > len(csvlist1):    #verbose code style
         bigger = set(csvlist2)
         smaller = set(csvlist1)
      else:                                  #again, verbose
         bigger = set(csvlist1)
         smaller = set(csvlist2)
         
      return bigger, smaller

   def doCompare(self, check1, check2, pre, verbose):
      csvlist1 = self.returncsvaslist(check1, pre)
      csvlist2 = self.returncsvaslist(check2, pre)
      
      ordered_lists = self.order_by_size(csvlist1, csvlist2)
      
      #in smaller but not in bigger
      diff = list(set(ordered_lists[self.BIGGER]) - set(ordered_lists[self.SMALLER]))
      
      #common elements in both
      same = ordered_lists[self.SMALLER] & ordered_lists[self.BIGGER]

      #output a report of findings...
      self.outputformattedtext(check1, check2, same, diff, verbose)

def checksumcompare(check1, check2, pre, verbose):

   compare = ChecksumCompare()
   compare.doCompare(check1, check2, pre, verbose)

def main():

   #	Usage: 	--csv [droid report]
   #	Handle command line arguments for the script
   
   #  TODO: Format of checksums in README
   parser = argparse.ArgumentParser(description='Compare two lists of non-identical checksums.')

   #TODO: Consider optional and mandatory elements... behaviour might change depending on output...
   #other options droid csv and rosetta schema
   #NOTE: class on its own might be used to create a blank import csv with just static options
   parser.add_argument('--check1', help='Checksum file one.', default=False, required=False)
   parser.add_argument('--check2', help='Checksum file two.', default=False, required=False)
   parser.add_argument('--pre', help='Pre-conditioned objects.', default=False, required=False, action="store_true")
   parser.add_argument('--v', help='Verbose: Output comparison files.', default=False, required=False, action="store_true")

   if len(sys.argv)==1:
      parser.print_help()
      sys.exit(1)

   #	Parse arguments into namespace object to reference later in the script
   global args
   args = parser.parse_args()
   
   #TODO: Additional help text to describe two discrete sets of options
   
   if args.check1 and args.check2:
      checksumcompare(args.check1, args.check2, args.pre, args.v)
   else:
      parser.print_help()
      sys.exit(1)

if __name__ == "__main__":
   main()
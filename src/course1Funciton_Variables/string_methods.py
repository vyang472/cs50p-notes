Names = [
    "   aLiCe   ",
    "boB   ",
    "   chArLie",
    "  dAvid   li   ",
    "  eVa   WANG",
    "   mIKe  zhou   ",
    "JACK   Ma   ",
    "   sArAh   connor ",
    "     liLY   chen",
    "  JAMES  bond   ",

]



def main():
   cleaned_names = []
   for name in Names:
      name = name.strip().title()
      cleaned_names.append(name)
    
    
   print(" , ".join(cleaned_names))

    


main()
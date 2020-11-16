#Myrendy #9-6-2017 ... CogAlg, Todor's interpretation/notation/...
#it's not python

Compare!{

  process.+
  fuzzy.+
  sign.
  range{   	
     wider{
	 }
	 average.
	 value.
	 valueList+value
	 
	 alternate.
	 
	 pattern.	 	
  }
  
  scan+
  overlap
  ...
  
  #formation of difference pattern dP ...
 
  ?  biggerRange
	[differentSign | borderCoordinate]
     
      ? longMissLine
	    biggerAccumulatedDifference
		{
		 increment		 
		          incrementalDerivation
				          \+
		          differencesList.
		}	  
	averagePixelDifference.				    #pd = Id/len...
	differencePattern
	differencePatternList.+
	
	alternative #alt = len(dP_) ...
	alernativeList.+
	
	
	differencePattern.0
	sameSignDifference
	overlap					  #owd+=1
	accumulatedPixelDfference #Id += pri_p = pri_p
	accumulatedDfference
	accumulatedValue
	differenceList.+
	
	=transmit=	
	
Level1(framePixelsList) {
  zeroFrame
  resolution
  filters
  rangeMinimum #should be a connection
  
  scanLines(y)
    takeLine
	?zeroRangeMinimum
	  -- connect(averages)
	  - zero(averages)
	?zeroOneRange
	  -- connect(accumulatedDfference, averageDiferenceFilter) 
	  - zero(accumulatedDfference)	  
	zero(fuzzy)
	zero(range)
	zero(coordinate)
	valuePattern+
	differencePattern+
	
	scanColumns(x)
	  takePixel	# % обх
	  ? !ZeroCoordinate    #ineff
	      Compare!
		  
	  previousPixel
	linePatternList.+(valuePaternList, differencePatternList)
	framePatternList.+(linePatternList)
	
 transmit(framePatternList)
}
		  
      	  
#Да знае какви параметри са нужни за определено извикване
  
  if x > r+2 and (sd != pri_sd or x == W-1):  # if derived pri_sd miss, dP is terminated

   if{
    { x[>]r+2} and { sd[!=]pri_sd  or x == W-1 }    
	biggerRange
	[differentSign | borderCoordinate]	  
  }
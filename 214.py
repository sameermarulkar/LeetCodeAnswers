class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        r = list()
    	j = list()
    	d = {}
    	op = list()
    	
    	# Creating 2 lists r and j for range and respective range values
    	for a in buildings:
    		r.append(list(range(a[0], a[1]+1, 1)))
    		j.append(a[2])
    		
    	# Creating empty dict capturing max value present in the range list
    	for i in range(1,(max(max(r)))+1):
    		d[i] = 0 
    	
    	# Mapping dict values to their corresponding ranges (j)
    	q = 0
    	for a in r:
    		for i in a:
    			if d[i] < j[q]:
    				d[i] = j[q]
    		q = q+1
    		
    	# Format conversion
    	mem = 0
    	for z in d:
    		if mem > d[z]:
    			op.append([z-1, d[z]])
    			mem = d[z]
    		elif mem < d[z]:
    			op.append([z, d[z]])
    			mem = d[z]
    			
    			
    	op.append([(max(max(r))), 0]) 
    	
        return op
		
        
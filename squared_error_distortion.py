import math

class TXT_Extract:
    def __init__(self,dna_file):
        f = open(dna_file,'r')
        
        self.lists = []
        for line in f:
            line = line.strip()
            if line[0] != '-':
                line = line.split(" ")
                for n,x in enumerate(line):
                    line[n] = float(x)
                self.lists.append(line)
    
        self.num_center = int(self.lists.pop(0)[0])
        self.num_data   = len(self.lists) - self.num_center
        
        self.center =[]
        for i in range(self.num_center):
            self.center += [self.lists[i]]  # cooridnate center
        
        f.close()

    def search_center(self):
        distance = []
        
        for i in self.lists:
            if i not in self.center:
                distance += [ self.min_center(i,self.center)**2 ]
    
    
        return sum(distance)/float(self.num_data)
                
    def print_center(self):
        print "%.3f" %( self.search_center() )

    def min_center(self, datapoint, center):
        """calculate the d(DataPoint,Center),
            return the minimum distance"""
        distance = []
        for i in center:
            distance += [ euclidean(datapoint,i) ]

        return min(distance)


def euclidean(c1, c2):
    distance =0
    for i,j in zip(c1,c2):
        distance += (i-j)**2
    
    return math.sqrt(distance)

if __name__=="__main__":
    #test=TXT_Extract('test.txt')
    test=TXT_Extract('dataset_10927_3.txt')
    test.print_center()



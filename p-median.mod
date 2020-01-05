/*********************************************
 * OPL 12.9.0.0 Model
 * Author: Vathanan
 * Creation Date: 3 janv. 2020 at 18:25:07
 *********************************************/

 int n = ...;//Number of points
 int d = ...;//Number of Dimension
 int c = ...;//Number of cluster
 
 float points= ...;
 float distance[points][points]= ...;
 
 dvar boolean Z[points][points];//Un s'ils sont dans le meme cluster
 
 minimize
 	sum( p1 in points )
 	  sum(p2 in points)
 	    distance[p1][p2]*Z[p1][p2];
 	    
 subject to {
 	ct1:
 	forall(p1 in points)
 	  sum(p2 in points)
 	    Z[p1][p2]==1;
 	
 	ct2:
 	forall(p1 in points)
 	  forall(p2 in points)
 	    if (z[p1][p2] <= z[p2][p2])
 	    	sum(p3 in point)//P3 c bon????
 	    	  z[p3][p3]==c;
 	 
 	ct3:///Regle boolean????
 	forall(p1 in points,c1 in cluster)
 	  
 
  
 }

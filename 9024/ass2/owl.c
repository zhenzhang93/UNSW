//9024 ass2
//
// Authors:
// Sijie Hou (z5193712@unsw.edu.au)

// Written: 23/07/2019

//update:  06/08/2019  remove some useless code
//update:  01/08/2019  remove global varibele for totalpath
//update:  31/07/2019  judge empty input
//update:  30/07/2019  remove global variable for input number



#include<stdio.h> 
#include<stdbool.h>
#include<string.h> 
#include<math.h> 
#include "Graph.h"
#include<stdlib.h>

//the length of dictionary words is less than or equal to 20
#define MAXSIZE 21 



//basic idea is compare each charater one by one
//so it need to divide into 3 condition

bool differByOne(char *s1, char *s2){
	int len1=strlen(s1);
	int len2=strlen(s2);
	if(abs (len1 - len2) > 1 ){
		//return false if the length difference larger then 1 
		return false;
	}
	if(abs(len1 - len2) == 1){
		//int shortlength = len1 > len2? len2:len1; 	
	
		//condition1:len1 > len 2
		if (len1 > len2){		
			int i = 0,j = 0,notequal = 0;
			while( i < len2 && j < len1){
				//compare from start of each string
				if(s1[j] != s2[i]){
					// if is not equal,increase the index of the longer string
					j++;
					notequal++;
				}
				else{
					i++;
					j++;
				}
			}
			if(notequal > 1){
				return false;
			}
			return true;
		}
		//condition2:len2 > len1
		else{
			int i = 0,j = 0,notequal = 0;
			while( i < len1 && j < len2){
		
				if(s2[j] != s1[i]){
					j++;
					notequal++;
				}
				else{
					i++;
					j++;
				}
			}
			if(notequal > 1){
				return false;
			}
			return true;
		}
	}	
	// condition3:len1 equals to len2
	else{
		int i,innercount = 0;
		for(i = 0; i < len1; i++){
			if(s1[i] == s2[i]){
				innercount++;
			}
		}			
		return innercount == len1 - 1;		
	} 
	return true;
}

//function to implement phase2
//print the things we need
void phase2(char **arr,int len,Graph g){
	int i;
	printf("Dictionary\n");
	for(i = 0; i< len; i++){
		printf("%d: %s\n",i,arr[i]);
	}
	printf("Ordered Word Ladder Graph\n");
	showGraph(g);
}



//fuction to transfer the arr to a graph
//add valid vertex into graph
//By a O(n^2) method 
Graph generateGraph(char **arr,int len){	
	Graph g = newGraph(len);
	int i,j;
	for(i=0;i<len;i++){
		for(j = i+1 ;j < len;j++){
			if(differByOne(arr[i],arr[j])){
				Edge e = newEdge(i,j);
				insertEdge(e,g);
			} 
			
		}
	} 	
	return g;	
}


//Find the longest path first.
//the basic idea is dp
//dp[i] stands for the maxlength of each vertex
//time complexity is O(n^2)
//check ecah vertex is connected to another
//if it is, then the maxlength can be the former one + 1 or the length of it self.
int findLongest(Graph g,int count){
	//if there is no input
	if(g == NULL){
		return 0;
	} 
	int reslen = 0;
	int i,j;
	int dp[count];
	for(i = 0; i<count;i++){
		dp[i] = 1;
	}
	for( i = 1;i < count; i++){
		for(j = 0; j < i; j++){
			if(isEdge(newEdge(i,j),g)!=0 ){
				dp[i] = dp[i] > dp[j] + 1?dp[i]:dp[j]+1;
			} 
			
		}
	}
	for(i= 0;i<count;i++){
		reslen = dp[i] > reslen? dp[i]:reslen;
	}
	
	return reslen;
}




//function to implement the phase3,by recursive dfs
//start means the start vertex of the graph, from this start to find all possible paths
//vistited is a array to record the vertex has been visited
//maxlength is the maxlength of the word ladder
//currentlen means the cuurent length of certain path
//arr is the input content
//count is the input number
//variable totalPath to record the total possible paths

//isnotchild is a array to record whether some vertex is the part of a path
//eg: one path is an->ao->at, and it is the longest part, then there is no need to run this function from ao
//because it is the part of this path, so all the paths from this vertex will be shorter than 3.
//this can help reduce the time 



void phase3(Graph g,int start,int *visited,int maxlength,int currentlen,char **arr,int *isnotchild,int count,int *totalPath){	
	
	// find the longest length
	int i;	
	// using visited arr to record which word is chosen. 
	// 1 means it is chosen.
	
	visited[start] = 1; 
	//when the currentlen equal to maxlength,means find a path
	//then print it out 		
    if(currentlen == maxlength){
    	if(*totalPath < 100){	
			printf("%2d: ",*totalPath);
			*totalPath = *totalPath+1;
			//to find the last vertex		
			int innercount = 0;
			for(i = 0; i < count; i++){
				// last node and visited 
				if(innercount == maxlength - 1 && visited[i]){
					printf("%s\n",arr[i]);
					//do not need to find path from all these vertex  
					isnotchild[i] = 0;
					break;
				}
				else if(visited[i]){						
					printf("%s -> ",arr[i]);	
					innercount++;				
					isnotchild[i] = 0;
				}			
			}	
		}
		//totalPath > 100, do not print
		else return;
	}
	//recursive part
	else{	   
		//judge where the next vertex is connected and not visited.
		for (i = start + 1; i < count; i++) { 
	        if (isEdge(newEdge(start,i),g) && ! visited[i]) {	
				//visit this vertex,make visited[i] euqal to 1		 
	            visited[i] = 1;
	            
	            //find the remaing path from i,the current length of this vertex puls one
	            phase3(g,i,visited,maxlength,currentlen+1,arr,isnotchild,count,totalPath);
	            
	            //back tracing the visited vertex     
	            visited[i] = 0;
	          
	        }
	    }
	    
	}
	visited[start] = 0;

} 

//excute all possible paths from 0 vertex to the last vertex of the graph
void excuteAllWord(int *isnotchild,int start,Graph g,int *visited,int maxlength,int currentlen,char **arr,int count,int *totalPath){
	int i;
	for(i = 0; i < count; i++){	
		if(isnotchild[i]){
    		phase3(g,i,visited,maxlength,currentlen,arr,isnotchild,count,totalPath);
   		}
	}	
}



int main(void){
	
	
	
	//variable to record the input number
	int count = 0;

	//read the input from keyborad or file
	//using a 2d array to store the input data
	char **res = NULL;
	//malloc a new memory to store single word
	char *arr = (char*)malloc(MAXSIZE*sizeof(char));
	while(scanf("%s",arr)!=EOF){
		//realloc according to the input size
		res = (char **)realloc(res,(count+1)*sizeof(char*));
		if(res == NULL){
            fprintf(stderr, "out of memory\n");
            exit(1);
		}
		int len = strlen(arr);
		*(res+count) =(char*)malloc((len+1)*sizeof(char));
		if( *(res+count) == NULL){
			fprintf(stderr, "out of memory\n");
            exit(1);
			
		}
		int i;
		//judge there is duplicated word
		int flag = 0;
		for(i = 0 ;i < count; i++){
			if(strcmp(arr,res[i]) == 0){
				flag = 1;
			}
		} 
		if(flag){
			//there is duplicated word
			continue;
		}
		
		//add the word into arr
		for(i = 0;i < len;i++){
			*(*(res+count)+i) = *(arr+i);
		}
		*(*(res+count)+len)  = '\0';
		count++;
	}
	//judge if it is empty input
	if(count == 0){
		return 0;
	}
	
	//read input finish
 
	int i;
	int visited[count];
	//init visited array to 0,means none of them is visited
	for(i = 0;i<count;i++){
		visited[i] = 0;
	}
	int isnotchild[count];
	//init isnotchild array to 1, means all of them can be regarded as a start vertex
	for(i = 0;i<count;i++){
		isnotchild[i] = 1;
	}	
	
	//generate a grpah 
	Graph g = generateGraph(res,count);
	
	
	phase2(res,count,g);
	
	//find the logest path
	int maxlength = findLongest(g,count);

	printf("Longest ladder length: %d\n",maxlength);
	printf("Longest ladders:\n");
	
	// every word has length 1
	//the total path is printed from 1
	int totalPath = 1;
	
	//excute phase3
	excuteAllWord(isnotchild,0,g,visited,maxlength,1,res,count,&totalPath);
	
	
	//free the graph and input array
	freeGraph(g);
	
	for(i = 0;i < count;i++){
		if(res[i] !=NULL){
			free(res[i]);
			res[i] = NULL;
		}
	}
	free(res);
	res = NULL;
	free(arr);
	arr = NULL;
	
	return 0;
	
}


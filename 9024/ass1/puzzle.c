#include <stdio.h>
#include "boardADT.h"


/*
date: 23/6/2019
*/
 
int main(int argc, char **argv)
{
	//deal with start input
	char *start_array = NULL;
	start_array = (char*)malloc(KB*KB*KB*sizeof(char));
	if(start_array==NULL){
		printf("Memory not allocated.\n");	
		return EXIT_FAILURE;	
	}
	//printf("1");
	Board board_start = readInputString(start_array);
	
	if(!checkBoardNumber(board_start)){
		printf("Not correct input number of start.\n");
		return EXIT_FAILURE;
	} 
	
	//printf("2");	
	
	
	char **start=NULL;
	start = dealInputString(start_array,board_start);
	
	free(start_array);
	start_array=NULL;
	
	//printf("3");
	
	// initiate start board
	
	if(!dealAllInput(start,board_start)){
		printf("Invalid input.\n");
		return EXIT_FAILURE;
	}
	
	board_start = charArrayToIntArray(start,board_start);
			
	//free the space of start
	
	freeArray(start,board_start);
	
	//printf("6");
	
	
	
	
	//deal with goal input
	char *goal_array =NULL;
	goal_array = (char*)malloc(KB*KB*KB*sizeof(char));
	
	if(goal_array==NULL){
		printf("Memory not allocated.\n");	
		return EXIT_FAILURE;	
	}
	
	Board board_goal  =  readInputString(goal_array);

	
	if(!checkBoardNumber(board_goal)){
		printf("Not correct input number of goal.\n");
		return EXIT_FAILURE;
	}
	
	
	char **goal=NULL;
	goal =  dealInputString(goal_array,board_goal);
	
	free(goal_array);
	goal_array=NULL;
	
	// initiate goal board
	
	if(!dealAllInput(goal,board_goal)){
		printf("Invalid input.\n");
		return EXIT_FAILURE;
	}
	
	board_goal = charArrayToIntArray(goal,board_goal);
	
	//free the space of goal
	
	freeArray(goal,board_goal);
	
	
	
	//juduge the board	

	if(!checkTwoboardEqual(board_start,board_goal)){
		printf("Not same number of input.\n");
		return EXIT_FAILURE;
	}
		
	if(!checkValid(board_start) || !checkValid(board_goal)){
		printf("Invalid input.\n");
		return EXIT_FAILURE;
	}

	printSolvable(board_start,board_goal);	
	
	freeBoard(board_start);
	freeBoard(board_goal);
	
    return EXIT_SUCCESS;
}


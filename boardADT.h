#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define KB 1024


typedef struct struct_board *Board;

Board readInputString(char *);

Board charArrayToIntArray(char **,Board);

int hasDuplicate(Board);

int checkLargerOrSmall(Board,int);

int checkValid(Board);

int disorder(Board);

int judgeSolvable(Board,Board);

void printSolvable(Board,Board);

int checkBoardNumber(Board);

int checkTwoboardEqual(Board,Board);

int isCorrectInput(char); 

int numberToN(Board);

int dealSingArray(char *);

int dealAllInput(char **,Board);

char **dealInputString(char *,Board);

void freeArray(char **,Board);

void freeBoard(Board);

int mergeSort(int *,int,int,int);

int merge(int *,int *,int,int,int,int);

int *findRownumber(int *,int);


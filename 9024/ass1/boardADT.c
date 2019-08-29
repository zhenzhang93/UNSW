#include "boardADT.h"

struct struct_board{
    // data
    int *data;
    // input size 
    int inputsize;
    //board size
    int size;
};
/**
 * create the board and get the size of it
 * @return board size and inputsize
 */ 
Board readInputString(char *array){
	//inputsize is count of char of input
	//size is count of input number
	char c;
	Board board = malloc(sizeof(struct struct_board));
    int count = 0;
	int numOfInput=0;
    int flag = -1;
    while((c=getchar())!='\n'){
    	*(array+count)=c;
    	count++;

		if(c=='\t' || c==' '){
			if(flag == 1){
				numOfInput++;		
			}			
			flag = 0;
		}
		else {
			flag = 1;
		} 	
    }

    board->inputsize = count; 
    board->size = (flag == 1)?numOfInput+1:numOfInput;
    board->data = NULL;
	return board;
}

// N is the row or the column, number is N*N
int hasDuplicate(Board start){
	// 0 means not valid,has duplicate number
	int number = start->size;
	int i;
	int *ptr=NULL;
	ptr = (int *)malloc(number*sizeof(int));
	if(ptr == NULL){
		printf("Memory not allocated.\n");
		exit(EXIT_FAILURE);
	}
	memset(ptr,0,number*sizeof(int));
	for(i =0; i < number; i++){		
			int temp= *(start->data + i);
			if (*(ptr+temp)==1){
				free(ptr);
				return 0;
			} 		
			*(ptr+temp) = 1;			
	}
	free(ptr);
	return 1;
}

int checkLargerOrSmall(Board start,int N){
	// 0 means not valid,large or small.
	int i,j;
	for(i =0; i < N; i++){		
		for(j=0; j < N; j++){
			if (*(start->data+(i*N+j)) > N*N-1){
				return 0;
			}	
			if(*(start->data+(i*N+j)) < 0){
				return 0;
			}		
		}
	}	
	return 1;
}

int checkValid(Board start){
	int N = numberToN(start);
	if(checkLargerOrSmall(start,N) && hasDuplicate(start)){
		return 1; // valid;
	}
	return 0; //not valid
}

/*
int disorder(Board start){
	//rownumber is thw row where there is a blank
	int i,j;
	int number = start->size;
	int rownumber=0;
	unsigned int disorder=0;
	int N = sqrt(number);
	for(i =0; i < number; i++){
		int temp = *(start->data + i);
		if(temp ==0){
			rownumber = i/N +1;
			continue;
		}
		for(j =i+1; j < number;j++){
			int numberj = *(start->data + j);
			if(numberj ==0) continue;
			
			if(temp > numberj){
				disorder++;
			}
		}
		
	}		
	if(N%2==0){
		disorder += rownumber;
	}
	return disorder;	
}

*/

int mergeSort(int *arr,int size,int left,int right){
	unsigned int disorder = 0;
	int *temp = (int*)malloc(size*sizeof(int));
	if(left < right){
		int mid = (left + right)/2;
		disorder += mergeSort(arr,size,left,mid);
		disorder += mergeSort(arr,size,mid+1,right);
		disorder += merge(arr,temp,left,mid,right,size);		
	}
	free(temp);	
	return disorder;
	
}

int merge(int *arr,int *temp,int left,int mid,int right,int size){
	int i = left;
	int j = mid+1;
	int k =left;
	unsigned int disorder = 0;	
	while(i <= mid  && j <=right){
		if( *(arr+i) < *(arr+j)){
			*(temp + k++) = *(arr+i);
			i++;
		}
		else{
			*(temp +k++) =*(arr+j);
			j++;
			disorder += mid+1-i;
		}
		
	}
	while(i<=mid){
		*(temp + k++) = *(arr+i);
		i++;
	}
	while(j<=right){
		
		*(temp +k++) =*(arr+j);
		j++;
	}	
	for (i = left; i <= right; i++)  
        *(arr+i) = *(temp+i);  
	return disorder;
	
}

int *findRownumber(int *arr,int size){
	int *res=NULL;
	res=(int*)malloc(2*sizeof(int)); 
	int i;
	int rownumber=0;
	int rowindex = -1;
	int N = sqrt(size);
	for(i=0;i<size;i++){
		if(*(arr+i)==0){
			rownumber = i/N+1;
			rowindex = i;
		}
	}
	*res = rownumber;
	*(res+1) = rowindex; 
	//printf("%d\n",rownumber);
	//printf("%d\n",rowindex);
	return res;
}


int disorder(Board start){
	int size = start->size;
	int *copy =(int*)malloc(sizeof(int)*size);
	memcpy(copy,start->data,size*sizeof(int));
	int *temp = findRownumber(copy,size);
	int rownumber=*(temp);
	int rowindex = *(temp+1);
	free(temp); 
	int N = sqrt(size);
	int res = mergeSort(copy,size,0,size-1);
	unsigned int disorder = res-rowindex;
	
	if(N%2==0){
		disorder += rownumber;
	}
	free(copy); 
	return disorder;
}



int judgeSolvable(Board start,Board goal){
	//return 1 if it is solveable;
	int disorder_start = disorder(start);
	int disorder_goal = disorder(goal);
	//printf("%d\n",disorder_start);
	//printf("%d\n",disorder_goal);
	if((disorder_start % 2 ==0 && disorder_goal % 2==0) || (disorder_start % 2!=0 &&disorder_goal % 2 !=0)){
		return 1;
	}
	else return 0;	
}

void printSolvable(Board start,Board goal){
	int number = start->size;
	int res=judgeSolvable(start,goal);
	int i;
	printf("start: ");
	for(i =0;i < number; i++){
		if(*(start->data+i) == 0){
			if(i==number-1){
				printf("b");
			}
			else {		 
				printf("b ");
			} 
		} 
		else {
			if(i==number-1){
				printf("%d",*(start->data + i));
			}
			else{
				printf("%d ",*(start->data + i));
			}
		}
		
	}
	putchar('\n');
	printf("goal: ");
	for(i =0;i < number; i++){
		if(*(goal->data+i) == 0){
			if(i==number-1){
				printf("b");
			}
			else {		 
				printf("b ");
			} 
		} 
		else {
			if(i==number-1){
				printf("%d",*(goal->data + i));
			}
			else{
				printf("%d ",*(goal->data + i));
			}
		}
	}
	putchar('\n');
	if(res==1){
		printf("solvable\n");
	}
	else{
		printf("unsolvable\n");
	}
}


int isCorrectInput(char c){
	//return 1 means correct
	if( c>='0' && c<='9') return 1;
	return 0;

}


int dealSingArray(char *array){
	//check the input is valid
	//0 means not valid
	int i;
	int length = strlen(array);	
	if(*(array)=='0' && length>=1){
		return 0;
	} 
	if(*(array)=='b' && length>1){
		return 0;
	}	
	else{
		if(*(array)=='b') return 1;
	}
	for(i=0; i < length; i++){
		if(!isCorrectInput(*(array+i))){
			return 0;
		}	
	}
	return 1;	
}

int dealAllInput(char **chararray,Board board){
	
	//1 means the input is valid 
	int size = board->size;
	int i;
	for(i=0; i<size; i++){
		if(!dealSingArray(*(chararray+i))){
			return 0;
		}
	}
	return 1;
}

Board charArrayToIntArray(char **chararray,Board board){
	//transfer the array to a int array;
	int i;	
	int size = board->size;
	board->data=NULL;
	board->data= (int*)malloc(size*sizeof(int));	
	if(board->data == NULL){
		printf("Memory not allocated.\n");
		exit(EXIT_FAILURE);
	}
	for(i=0;i<size;i++){
		char *temp = *(chararray+i);
		if(strcmp(temp, "b") == 0){
			*(board->data+i) = 0; 
		}
		else{
			int num = atoi(temp);
			*(board->data+i) = num; 
		}
	}
	return board;	
}



//deal input string to make it can be sotred in the board

char **dealInputString(char *array,Board board){	
	int i;
	int inputsize = board->size;
	int arraysize = board->inputsize; 
	if(inputsize==0){
		printf("Invalid input.\n");
		exit(EXIT_FAILURE);
	}
	char **chararray = (char**)malloc(inputsize*sizeof(char*));
	if(chararray==NULL){
		printf("Memory not allocated.\n");
		exit(EXIT_FAILURE);
	}
	
	//printf("3");
	//printf("%d\n",inputsize); 
	//printf("%d\n",arraysize); 
	
	for(i = 0; i < inputsize; i++){
		*(chararray+i)=(char*)malloc(sizeof(char));	
	}
	int j;
	int startOfArray = 0;
	for(j = 0; j < inputsize;j++){
		int start = 0;
		while(startOfArray < arraysize){
			char temp = *(array+startOfArray);
			while(startOfArray < arraysize && (temp == '\t' || temp ==' ')) {
				startOfArray++;
				temp = *(array+startOfArray);
			}
			while(startOfArray < arraysize && temp !='\t' &&  temp !=' ') { 
				*(chararray+j) = (char*)realloc(*(chararray+j),(start+2)*sizeof(char));
				if(*(chararray+j)==NULL){
					printf("Memory not allocated.\n");	
					exit(EXIT_FAILURE);			
				}
				
				//printf("4");
				
				//printf("%d\n",sizeof(*(chararray+j)));
				*(*(chararray+j)+start) = temp;
				start++;
				startOfArray++;
				temp = *(array+startOfArray);
			}
			*(*(chararray+j)+start) ='\0';
			break;			
		}
	}
	return chararray;
}


int checkBoardNumber(Board board){
	//return 1 if it is valid
	int number = board->size;
	if(number<4) return 0;
	double a;
	a = sqrt(number);
	if ((int)a == a) return 1;
	return 0;
	
}

int checkTwoboardEqual(Board start,Board goal){
	//return 1 if it is valid
	int a = start->size;
	int b = goal->size;
	if(a==b){
		return 1;
	}
	return 0;
}

int numberToN(Board board){
	int number = board->size;
	return sqrt(number);
}

void freeArray(char **start,Board board){
	int i;
	int start_inputsize=board->size;
	for(i = 0; i < start_inputsize; i++){	
		free(*(start+i));
		
	} 
	free(start);
	start = NULL;
	
}


void freeBoard(Board board) {
	if(board!=NULL){
		if(board->data!=NULL){
			free(board->data);
		}
		free(board);
	}

}



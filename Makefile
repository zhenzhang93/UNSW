CC=9024 dcc
CFLAGS=-O3

puzzle: puzzle.o boardADT.o
	$(CC) puzzle.o boardADT.o $(CFLAGS) -o puzzle 

puzzle.o: puzzle.c boardADT.h
	$(CC) -c puzzle.c 

boardADT.o: boardADT.c boardADT.h 
	$(CC) -c boardADT.c 
 
clean:
	rm -f puzzle puzzle.o boardADT.o core

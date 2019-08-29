CC=~cs9024/bin/dcc
CFLAGS=-I.
DEPS=Graph.h Quack.h
OBJ=GraphAM.o Quack.o owl.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

owl: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean
clean:
	rm -f *.o owl core

// Graph.h: generic interface for undirected/unweighted graphs

#define UNVISITED -1

typedef int Vertex;               // define a VERTEX

typedef struct {                  // define an Edge
  Vertex v;
  Vertex w;
} Edge;

typedef struct graphRep *Graph;   // define a GRAPH

Graph newGraph(int);              // create a new graph
Graph freeGraph(Graph);           // free the graph mallocs
void showGraph(Graph);            // print the graph

Edge newEdge(Vertex, Vertex);     // create a new edge
void insertEdge(Edge, Graph);     // insert an edge
void removeEdge(Edge, Graph);     // remove an edge
int  isEdge(Edge, Graph);         // check edge exists
void showEdge(Edge);              // print an edge

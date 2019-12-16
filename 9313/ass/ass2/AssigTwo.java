import java.io.Serializable;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Iterator;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.PairFlatMapFunction;
import org.apache.spark.api.java.function.PairFunction;

import scala.Tuple2;


/*
 * map part:
 * map to this format
 * (N4,-1:[(N0,4), (N1,4), (N5,6)], path), means the start node to N4, and the distance to it
 * then we will get all the node and distance, like this
 * N0,-1   N1,-1  N3, 2  N0, 6:N2(also record the distance,means the distance from start node to N0 through N2 is 6)]
 * also, the adjacent nodes are emitted as well
 * 
 * reduce part:
 * reduce the above output,we can get all the path and distance from one node to another
 * then we choose the shortest one 
 * then update the path and keep doing next map and reduce.
 * 
 * main part:
 * keep the map reduce process 
 * until there is no change
 * means we find all the path
 * 
 * in the end, sort the output and format the output 
 * 
 * @author 
 */

public class AssigTwo{

	//class for record the path
	public static class MyPath implements Serializable {
		private ArrayList<String> nodes;

		public ArrayList<String> getNodes() {
			return nodes;
		}

		public void setNodes(ArrayList<String> nodes) {
			this.nodes = nodes;
		}

		public MyPath(ArrayList<String> node) {
			this.nodes = node;
		}

		public String toString() {
			StringBuffer sb = new StringBuffer();
			for (int i = 0; i < nodes.size(); i++) {
				if (i == nodes.size() - 1) {
					sb.append(nodes.get(i));
				} else {
					sb.append(nodes.get(i)).append("-");
				}
			}
			return sb.toString();
		}

		@Override
		public int hashCode() {
			return nodes.toString().hashCode();
		}

		@Override
		public boolean equals(Object obj) {
			if (this.toString().equals(obj.toString())) {
				return true;
			}
			return false;
		}

	}

	//class for map reduce, it is a format
	public static class OutputClass implements Serializable {
		private String adjacent;
		private Integer distance;
		private MyPath path;

		public OutputClass(String adjacent, Integer distance, MyPath path) {

			this.adjacent = adjacent;
			this.distance = distance;
			this.path = path;
		}

		public String getAdjacent() {
			return adjacent;
		}

		public void setAdjacent(String adjacent) {
			this.adjacent = adjacent;
		}

		public Integer getDistance() {
			return distance;
		}

		public void setDistance(Integer distance) {
			this.distance = distance;
		}

		public MyPath getPath() {
			return path;
		}

		public void setPath(MyPath path) {
			this.path = path;
		}

		public String toString() {
			StringBuffer sb = new StringBuffer();
			sb.append(distance).append(",").append(adjacent).append(",").append(path);
			return sb.toString();
		}

		@Override
		public int hashCode() {

			return adjacent.hashCode() + distance + path.hashCode();
		}

		@Override
		public boolean equals(Object obj) {
			if (this.toString().equals(obj.toString())) {
				return true;
			}
			return false;
		}
	}

	//class for store the node and the path
	public static class NodeAndPath implements Serializable {
		private String node;
		private MyPath path;

		public NodeAndPath(String node, MyPath path) {
			this.node = node;
			this.path = path;
		}

		public String getNode() {
			return node;
		}

		public void setNode(String node) {
			this.node = node;
		}

		public MyPath getPath() {
			return path;
		}

		public void setPath(MyPath path) {
			this.path = path;
		}

		@Override
		public String toString() {
			return node + "," + path;
		}
	}

	//class for format the output
	public static class FinalClass implements Serializable {
		private String startNode;
		private Integer distance;
		private MyPath path;

		public FinalClass(String startNode, Integer distance, MyPath path) {
			this.startNode = startNode;
			this.distance = distance;
			this.path = path;
		}

		public String toString() {
			StringBuffer sb = new StringBuffer();
			sb.append(startNode).append(",").append(distance).append(",").append(path);
			return sb.toString();
		}

	}

	//comparator class for sort the output
	public static class MyComp implements Comparator<Integer>, Serializable {

		@Override
		public int compare(Integer o1, Integer o2) {
			if (o1 != -1 && o2 != -1) {
				return o1.compareTo(o2);
			} 
			else if(o1 == -1 && o2 == -1 ) {
				return 0;
			}
			else {
				return o1 == -1 ? 1:-1;
			}
		}
	}

	public static void main(String[] args) {

	    if (args.length !=3 ) {
	      System.err.println("Usage: Assign2 <STARTING_NODE> <INPUT_PATH> <OUTPUT_PATH>");
	      System.exit(1);
	    }

		SparkConf conf = new SparkConf().setAppName("ass2").setMaster("local");

		JavaSparkContext context = new JavaSparkContext(conf);

		String inputpath = args[1];

		String outputpath = args[2];

		JavaRDD<String> input = context.textFile(inputpath);

		String sourcenode = args[0];

		//get the original data
		//format like this, node and its adjacent nodes
		//N4,[(N0,4), (N1,4), (N5,6)]
	
		JavaPairRDD<String, Iterable<Tuple2<String, Integer>>> allnode = input
				.mapToPair(new PairFunction<String, String, Tuple2<String, Integer>>() {

					@Override
					public Tuple2<String, Tuple2<String, Integer>> call(String line) throws Exception {
						String[] parts = line.split(",");
						String startNode = parts[0];
						String endNode = parts[1];
						int dis = Integer.parseInt(parts[2]);
						return new Tuple2<String, Tuple2<String, Integer>>(startNode, new Tuple2<>(endNode, dis));
					}
				}).groupByKey();



		JavaPairRDD<String, OutputClass> initRdd = allnode
				.mapToPair(new PairFunction<Tuple2<String, Iterable<Tuple2<String, Integer>>>, String, OutputClass>() {

					@Override
					public Tuple2<String, OutputClass> call(Tuple2<String, Iterable<Tuple2<String, Integer>>> line)
							throws Exception {
						ArrayList<String> node = new ArrayList<String>();
						String key = line._1;
						int distance = -1;
						String adjacent = line._2.toString();

						if (key.equals(sourcenode)) {
							distance = 0;
						}
						return new Tuple2<String, OutputClass>(key,
								new OutputClass(adjacent, distance, new MyPath(node)));
					}

				});

		

		// the format of initRdd is like this
		// (N4,-1:[(N0,4), (N1,4), (N5,6)]), the start node to N4,and the distance to this node
		// also record the this node's adjacent nodes.

		// core part
		// map reduce process
		// using a while loop to keep map reduce process, until there is nothing updated
		boolean undone = true;
		while (undone == true) {

			// map to node,distance
			// means the distance from the start node to this node.


			//map
			JavaPairRDD<String, OutputClass> mapper = initRdd
					.flatMapToPair(new PairFlatMapFunction<Tuple2<String, OutputClass>, String, OutputClass>() {

						@Override
						public Iterator<Tuple2<String, OutputClass>> call(Tuple2<String, OutputClass> input)
								throws Exception {

							ArrayList<Tuple2<String, OutputClass>> res = new ArrayList<>();
							// add original info
							res.add(input);
							OutputClass obj = input._2;
							int initdist = obj.getDistance();
							String adjacent = obj.getAdjacent();
							MyPath path = obj.getPath();

							// this node has adjacent nodes
							if (adjacent.length() != 0) {
								String[] adj = adjacent.substring(1, adjacent.length() - 1).split(", ");
								
								for (int i = 0; i < adj.length; i++) {
									String nodeDist = adj[i].substring(1, adj[i].length() - 1);
									String node = nodeDist.split(",")[0];
									String dist = nodeDist.split(",")[1];
									if (initdist != -1) {
									// through node get a distance
										ArrayList<String> newarr = new ArrayList<String>(path.getNodes());
										newarr.add(node);
										int newdist = Integer.parseInt(dist) + initdist;
										res.add(new Tuple2<String, OutputClass>(node,
												new OutputClass("", newdist, new MyPath(newarr))));
									}
											
									//through node still unreachable
									else {
										res.add(new Tuple2<String, OutputClass>(node,
												new OutputClass("", -1, path)));
									}													
								}
							}
							return res.iterator();
						}

					});

			

			// update the path and then iterate the output again
			// reduce
			JavaPairRDD<String, OutputClass> reducer = mapper.groupByKey()
					.mapToPair(new PairFunction<Tuple2<String, Iterable<OutputClass>>, String, OutputClass>() {

						@Override
						public Tuple2<String, OutputClass> call(Tuple2<String, Iterable<OutputClass>> output)
								throws Exception {
							String node = output._1;
							String adj = "";
							int newdist = Integer.MAX_VALUE;
							MyPath path = new MyPath(new ArrayList<String>());
							
							//find the shortest distance
							for (OutputClass val : output._2) {
								int dist = val.getDistance();
								String myadj = val.getAdjacent();
								if (!myadj.equals("")) {
									adj = myadj;
								}
								// there is a shorter path
								if (dist != -1 && dist < newdist) {
									newdist = dist;
									path = val.getPath();
								}
							}
						
							// still unreachable
							if (newdist == Integer.MAX_VALUE) {
								newdist = -1;
							}
							return new Tuple2<String, OutputClass>(node, new OutputClass(adj, newdist, path));
						}

					});

			
			JavaPairRDD<String, OutputClass> sub = reducer.subtract(initRdd);

			//there is no change
			if (sub.isEmpty()) {
				// all nodes has been updated
				undone = false;
			}

			initRdd = reducer;

		}

		

		// format the output to the spec
		// using a new JavaPairRdd,the key is the distance
		// so we can sort according to this key
		// using function sortByKey
		JavaPairRDD<Integer, NodeAndPath> forsort = initRdd
				.flatMapToPair(new PairFlatMapFunction<Tuple2<String, OutputClass>, Integer, NodeAndPath>() {

					@Override
					public Iterator<Tuple2<Integer, NodeAndPath>> call(Tuple2<String, OutputClass> input)
							throws Exception {
						ArrayList<Tuple2<Integer, NodeAndPath>> res = new ArrayList<Tuple2<Integer, NodeAndPath>>();
						String node = input._1;
						OutputClass obj = input._2;
						int dist = obj.getDistance();
						MyPath path = obj.getPath();
						if (!node.equals(sourcenode)) {
							ArrayList<String> newpath = path.getNodes();
							if (dist != -1) {
								newpath.add(0, sourcenode);
							}
							res.add(new Tuple2<Integer, NodeAndPath>(dist, new NodeAndPath(node, new MyPath(newpath))));
						}

						return res.iterator();

					}

				});

		
		//sort the res and then output
		JavaRDD<FinalClass> outputres = forsort.sortByKey(new MyComp())
				.flatMap(new FlatMapFunction<Tuple2<Integer, NodeAndPath>, FinalClass>() {

					@Override
					public Iterator<FinalClass> call(Tuple2<Integer, NodeAndPath> line) throws Exception {
						ArrayList<FinalClass> al = new ArrayList<FinalClass>();
						int dist = line._1;
						NodeAndPath nodeAndPath = line._2;
						String node = nodeAndPath.getNode();
						MyPath path = nodeAndPath.getPath();
						al.add(new FinalClass(node, dist, path));
						return al.iterator();
					}

				});

		//outputres.collect().forEach(x -> System.out.println(x));
		

		// save the output
		outputres.saveAsTextFile(outputpath);

	}

}

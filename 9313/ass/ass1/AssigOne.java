import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;


import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;




public class AssigOne {
	
	
	
	public static class MyMapper extends Mapper<LongWritable, Text, Text, Text>{

		
		Text userId = new Text();

 		@Override
		protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
				throws IOException, InterruptedException {
			
 			//to make the data like below
 			//userid::movieid,rating
 			//U1	::M1,2
			
			String[] strarr = value.toString().split("::");
			if(strarr.length == 4) {		
				userId.set(strarr[0].trim());	
				context.write(userId, new Text(strarr[1]+","+strarr[2])); 
				
			}
		}
		
	}
	
	public static class MyReducer extends Reducer<Text, Text, Text, Text>{

		@Override
		protected void reduce(Text movie, Iterable<Text> values, Reducer<Text, Text, Text, Text>.Context context)
				throws IOException, InterruptedException {
			
 			//aggregate the value according to the givenkey,like this
			//userid::movieid,rating movieid,rating(it is a list)
			//U2	::M2,3 M3,1
			
			ArrayList<String> al = new ArrayList<String>();
 			//String res = "";
			for(Text val:values) {
				al.add(val.toString());
				//res = res.concat(val.toString() +" ");
			}
			//sort the value according to the string
			//like: U1 ::M1,5 M2,4 M3,7
			Collections.sort(al, new Comparator<String>() {

				public int compare(String o1, String o2) {
					return o1.compareTo(o2);
				}
				
			});
			context.write(movie, new Text("::"+al.toString()));
		}
		
	}
	
	
		
	
	
	public static class MyMapper1 extends Mapper<LongWritable, Text, Text, Text>{

		@Override
		protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
				throws IOException, InterruptedException {
			
			//System.out.println(value.toString().split("::")[0]);
			String[] strarr = value.toString().split("::");
			
			//starr[0] is the userid
			
			ArrayList<String> al = new ArrayList<String>();
			
			//split the value and add all the arraylist
			
			String[] strings= strarr[1].substring(1,strarr[1].length()-1).toString().split(", ");
			
			
			for(String s:strings) {
			
				al.add(s.toString());
			}
			
			// if the user has rated at least two movies
			if(al.size() != 1) {
				//making the pair become the key
				for(int i = 0; i < al.size();i++) {
					
					String movieAndRating1 = (String)al.get(i);
					String movie1 = movieAndRating1.split(",")[0];
					
					for(int j = i+1; j < al.size(); j++) {
						
						String movieAndRating2 = (String)al.get(j);
						String movie2 = movieAndRating2.split(",")[0];
						// if two movies not same, become a pair
						if(!movie1.equals(movie2)) {
							String pair = "("+movie1 +"," +movie2+")"; 
							
							context.write(new Text(pair), new Text("("+strarr[0].toString().trim()+","+movieAndRating1.split(",")[1].trim()+","+movieAndRating2.split(",")[1].trim()+")"));
						}
					}
					
				}
			}
			
			
		}
	}
	
	public static class MyReducer1 extends Reducer<Text, Text, Text, Text>{

		@Override
		protected void reduce(Text pair, Iterable<Text> values, Reducer<Text, Text, Text, Text>.Context context)
				throws IOException, InterruptedException {
			
			//add to the arraylist and return
			ArrayList<String> al = new ArrayList<String>();
			for(Text val: values) {
				al.add(val.toString());
			}
			//format the output
			context.write(pair, new Text(al.toString().replace(" ", "")));
			
		}
	}
	
	
	

	public static void main(String[] args) throws Exception {
		if(args.length !=2) {
			System.err.println("Usage: AssigOne <in> <out>");
			System.exit(1);	
		}
		Path out = new Path(args[1]);
		
		//first job
		Job job1 = Job.getInstance(new Configuration(), "Ass1_p1");
		
		
		job1.setMapperClass(MyMapper.class);
		job1.setReducerClass(MyReducer.class);
		
		job1.setMapOutputKeyClass(Text.class);
		job1.setMapOutputValueClass(Text.class);
		
		job1.setOutputKeyClass(Text.class);
		job1.setOutputValueClass(Text.class);
		
		FileInputFormat.addInputPath(job1,new Path(args[0]));
		FileOutputFormat.setOutputPath(job1, new Path(out,"out1"));
		
		
		
		//second job
		Configuration conf = new Configuration();
		//format the output
		conf.set("mapred.textoutputformat.separator", " ");
		Job job2 = Job.getInstance(conf, "Ass1_p2");
		
		
		job2.setMapperClass(MyMapper1.class);
		job2.setReducerClass(MyReducer1.class);
		
		job2.setMapOutputKeyClass(Text.class);
		job2.setMapOutputValueClass(Text.class);
		
		job2.setOutputKeyClass(Text.class);
		job2.setOutputValueClass(Text.class);
		
		FileInputFormat.addInputPath(job2,new Path(out,"out1"));
		FileOutputFormat.setOutputPath(job2, new Path(out,"out2"));
		
		
		job1.waitForCompletion(true);
		job2.waitForCompletion(true);
	}

}

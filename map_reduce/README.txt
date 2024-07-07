Applying MapReduce to K-Means Clustering
Master Component:
Responsible for coordinating the entire computation.
Receives parameters such as number of mappers (M), number of reducers (R), number of centroids (K), and number of iterations.
Divides the input data (points.txt) into smaller chunks (input splits) for parallel processing by mappers.

Mapper Component:
Each mapper processes an input split independently.
Reads its assigned portion of the data points and the current list of centroids.
Computes the nearest centroid for each data point and emits intermediate key-value pairs:
Key: Index of the nearest centroid.
Value: Data point.
Outputs are written to local partition files within the mapper’s directory (Mappers/M1, Mappers/M2, ...).

Partition Function:
Partitions the intermediate key-value pairs into smaller partitions based on a simple partitioning function (e.g., key % R).
Ensures all key-value pairs with the same key (centroid index) are sent to the same partition file.

Reducer Component:
Each reducer receives partitions from multiple mappers.
Performs shuffle and sort to group intermediate key-value pairs by key (centroid index).
For each centroid, collects all data points assigned to it from multiple mappers.
Computes the updated centroid based on the mean of these data points and emits:
Key: Centroid Id.
Value: Updated Centroid.
Outputs are written to local reducer files (Reducers/R1.txt, Reducers/R2.txt, ...).
Centroid Compilation by Master:
After all reducers have completed their tasks, the master compiles the final list of centroids from reducer output files.
This list serves as the input for the next iteration of the K-means algorithm.

gRPC Communication:
Master-Mapper: Master sends parameters and invokes mappers for map and partition tasks.
Master-Reducer: After mapping phase completes, master invokes reducers with necessary parameters.
Reducer-Mapper: Reducers communicate with mappers to fetch input data before performing shuffle, sort, and reduce operations.
Master-Reducer (Final Phase): Master retrieves the final output data files from reducers.
Fault Tolerance:
Handles failures by rerunning tasks that return "unsuccessful" or "failed" messages.
Implements mechanisms to reassign failed tasks to other mappers or reducers.

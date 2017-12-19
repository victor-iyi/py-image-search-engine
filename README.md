# Building an Image Search Engine

In this project, an image query is accepted through a command line interface & the algorithm performs searching and ranking for similar images

Here's a review of how it works:

- **Step 1: Define Image Descriptor.** Before building an image search engine, consideration for how to represent and quantify images using only a list of number (ie. a feature vector) needs to be set in motion. Three aspects of an image that can be easily described: *color, texture and shape*
- **Step 2: Indexing Dataset.** After selecting a descriptor, it will be applied to extract features from each and every image in our dataset. The process of extracting features from an image is called *"indexing".* These features are then written to disk for later use. Indexing is also a task that's easily made parallel by utilizing multiple cores/processors on your machine.
- **Step 3: Defining Similarity Metric.** In step 1, we defined a method to extract features from an image. Now, we need to define a method to compare our feature vectors. A distance function should accept two feature vectors and then return a value indicating how *"similar"* they are. Common choice for similarity functions include (but are certainly not limited to) *Euclidean, Manhattan, Cosine and Chi-squared distances.*
- **Step 4. Searching and Ranking.** Here is where we're now finally ready to perform the last step in building an image search engine.


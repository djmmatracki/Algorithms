# Data Algorithms

Topics:

- Data Classifications
- Data storage algorithms
- Using algorithms for data compression
- Using algorithms for data streaming

## Data Classifications

Features that should be taken into account in the context of data algorithms:

- Input size. It captures the amount of data that needs to be processed and stored in the algorithm

- Ramp rate. It defines the speed at which new data is generated. "Hot data" is increasing quickly, "Cold data" is increasing slowly.

- Variety of content and structure. It refers to the variety and number of types of structured and unstructured data that need to be combined into a single table.

## Data storage algorithms

A reliable and efficient data repository is the heart of a distributed system. If such a repository was created with analysis in mind, we call it a data lake.

#### Data storage strategies

An appropriate data retention strategy depends on the type of data, the intended usage pattern, and non-functional requirements. The CAP (Consistency, avaibility, partition tolerance) theorem is the basis of most data storage strategies in distributed systems.

### CAP theorem

It draws attention to numerous compromises, inevitable in the process of designing a distributed storage system.

To understand its assumptions, it is worth defining three characteristics: consistency, availability, and partitioning resistance.

- **Consistency**. Consistency guarantees that at some point in time t1, regardless of which node we use, we will get the same result. Each read operation will either return the latest consistent data across the repository or result in an error.

- **Availability**. It guarantees that any node will be able to handle the data immediately.

- **Partitioning Resistance**. Partitioning resilience ensures that if a communication error occurs with a small number of nodes, the system continues to run.

The theorem states that a system can only have two of the three characteristics.

Three types of distributed systems:

#### CA systems

They are characterized by consistency and accessibility. Examples are MySQL, PostgreSQL, Oracle ...

#### AP systems

Optimized for availability. They are used for real-time monitoring, e.g. in a sensor network. An example is Cassandra.

#### CP systems

They ensure consistency and resistance to partitioning. A common use case for such systems is storing a file in JSON format. MongoDB.


### Data streaming algorithms

Streaming applications:

- fraud detection
- system monitoring
- setting out the order route
- screens visualizing indicators in real time
- motion sensors on highways
- credit card transaction control

## Data compression algorithms

### Lossless compression algorithms

These are algorithms that can compress data so that no information is lost when decompressed. Usage:

- document compression
- source code packet compression
- convert a large number of small files into a small number of large ones

#### Hoffman encoding

Hoffman encoding is one of the simplest data compression methods, based on the creation of the Hoffman tree, which is the basis for encoding and decoding data.

Hoffman coding notes:

- Coding. In the context of data, it means representing them in some other form.
- Code word. A specific character in coded form.
- Fixed length code. Each character is encoded with the same number of bits.
- Variable length code.
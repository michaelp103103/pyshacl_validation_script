This script validates the data graphs in a directory using shape graphs in another directory.

This script takes in three arguments: the data graph directory, the shapes graph directory, and the directory where the validation reports should be stored.

```
python validate.py /data/graph/directory /shapes/graph/directory /output/directory
```

It is assumed that for each data graph file in the data graph directory, there is exactly one corresponding shapes graph file in the shapes graph directory that shares the same filename prefix.

For example, if the data graph directory contains a file "SomeOntology.ttl", then there must be exactly one file in the shapes graph directory that has a filename with the prefix "SomeOntology", like "SomeOntologyShapes.ttl" or "SomeOntology_shapes.ttl".
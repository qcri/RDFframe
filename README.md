# RDFrame


A Python library that enables data scientists to extract data from knowledge graphs encoded in [RDF](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) into familiar tabular formats using familiar procedural Python abstractions.
RDFrames provides an easy-to-use, efficient, and scalable API for users who are familiar with the PyData (Python for Data) ecosystem but are not experts in [SPARQL](https://www.w3.org/TR/sparql11-query/).
The API calls are internally converted into optimized SPARQL queries, which are then executed on a local RDF engine or a remote SPARQL endpoint.
The results are returned in tabular format, such as a pandas dataframe.

## Installation via ``pip``


You can directly install the library via pip by using:

```
 $ pip install RDFrame
```   
## Getting started

First create a ``KnowledgeGraph`` to specify any namespaces that will be used in the query and optionally the graph name and URI.
For example:
```python
graph = KnowledgeGraph(prefixes={
                               "swrc": "http://swrc.ontoware.org/ontology#",
                               "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                               "dc": "http://purl.org/dc/elements/1.1/",
                           })
```

Then create a ``Dataset`` using one of our convenience functions. All the convenience functions are methods in the
```KnowledgeGraph``` class. 
For example, the following code retrieves all instances of the class ``swrc:InProceedings``:

```python
dataset = graph.entities(class_name='swrc:InProceedings',
                             new_dataset_name='papers',
                             entities_col_name='paper')
```

There are two types of datasets: ``ExpandableDataset`` and ``GroupedDataset``. 
An ``ExpandableDataset`` represents a simple flat table, while a ``GroupedDataset`` is a table split into groups as a result of a group-by operation.
The convenience functions on the ``KnowledgeGraph`` return an ``ExpandableDataset``.

After instantiating a dataset, you can use the API to perform operations on it. 
For example, the following code retrieves all authors and titles of conference papers:
```python
dataset = dataset.expand(src_col_name='paper', predicate_list=[
        RDFPredicate('dc:title', 'title'),
        RDFPredicate('dc:creator', 'author'),
        RDFPredicate('swrc:series', 'conference')])\
```

Using the ``group_by`` operation results in a ``GroupedDataset``:
```python
grouped_dataset = dataset.group_by(['author'])
```

Aggregation can be done in both an ``ExpandableDataset`` and ``GroupedDataset``.
For example, the following code counts the number of papers per author and keeps only the authors that have more than 20 papers:
```python
grouped_dataset = grouped_dataset.count(aggregation_fn_data=[AggregationData('paper', 'papers_count')])\
        .filter(conditions_dict={'papers_count': ['>= 20']})
```




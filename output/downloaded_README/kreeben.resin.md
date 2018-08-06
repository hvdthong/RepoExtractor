# Resin Search Engine

## A full-text search server.

Gather all of your business entities with their varying types of variable-length fields. Analyze, compress and store each entity and their meta-data in a set of disk-based bitmaps designed for fast reading and full-text lookup. Distribute the data onto a set of  servers that you can connect to in a RPC-like manner through a simple type system and over TCP or, through a JSON HTTP API. Host on-premise or in the cloud.

## Main building blocks

### Resin.Documents

Map and compress variable sized business entities into fixed-sized bitmaps.

### Resin.Search

Query and maintain a full-text index of your business data.

### Resin.SearchServer

Query your data with a JSON HTTP API

### Resin.Cli

Read, write and analyze your index with a commandline tool.

## Some use cases

- a disk-based replacement to your in-memory business entity cache
- a training data vector store
- a index of your data
- a distributed database
- a framework for experimenting with scoring models 
- a big data analysis tool
- a search engine

## Scale

1. Distribute data and load and increase performance of the JSON HTTP server by serving postings and documents from two separate servers.

2. Add more disks and RAM on all three servers.

3. Move your HTTP, postings and documents servers to the cloud and to a service that can supply you with 500 TB disks or larger, or build a fast networked storage solution.

4. For redundancy and load balancing, create more HTTP servers, each one supported by a pair of postings and documents servers. Let a JSON HTTP server, a postings server and a document server constitute either a shard or a mirror.

Alternatively, scale only the postings and document services by placing both behind load balancers. Then do the same with the HTTP server.

## Query language and execution plan

Resin provides term-based lookups. A term references both a field (key) and a word (value):

	title:rambo
	
Issuing such a statement will yield all documents with the word `rambo` somwhere in the title, sorted by relevance.

A query string may contain groups of `key:value` pairs. Each such pair is a query term:

	title:rambo genre:action

Query terms may be concatenated by a `space` (meaning OR), a `+` sign (meaning AND) or a `-` sign (meaning NOT):

	title:first title:blood
	title:first+title:blood
	title:first-title:blood

Query terms may be grouped together by enclosing them in parenthesis:

	title:jesus+(genre:history genre:fiction)

### Fuzzy, prefix, range and phrase queries are re-written

A fuzzy query term is suffixed with a `~`:

	body:morpheous~

A prefix query term is suffixed with a `*`:

	body:morph*
	
A greater-than query term separates the key and the value with a `>`:

	created_date>2017-07-15

A less-than query term separates the key and the value with a `<`:

	created_date<2017-07-15

A range query:

	created_date<2017-07-15+created_date>2017-07-15

Same query re-ordered:

	created_date>2017-07-15+created_date<2017-07-15

This is a phrase query:
	
	title:"the good bad ugly and"

Resin re-writes it into:

	title:the title:good title:bad title:ugly title:and

A phrase can be fuzzy:

	title:"the good bad ugly and"~
	
Resin re-writes that into:

	title:the~ title:good~ title:bad~ title:ugly~ title:and~

When Resin is subjected to a fuzzy, prefix or range query it expands it to include all terms that exists in the corpus and that lives within the boundaries as specified by the prefix, fuzzy or range operators (`* ~ < >`).

E.g.

	title:bananna~

will be expanded into:

	title:banana title:bananas
	
...if those are the terms that exists in the corpus and are near enough to the original term.

You may follow the parsing of the query and its execution plan by switching to DEBUG logging (in log4net.config) and then issuing the query through the CLI.

## Full-text search

### Character trie index
ResinDB's main index data structure is a disk-based doubly-linked character trie. Querying operations support includes term, fuzzy, prefix, phrase and range. 

### Tf-idf weighted continuous bag-of-words model

Scores are calculated using a word vector space tf-idf continuous bag-of-words model for phrases and through a simpler tf-idf model for term-based queries.

## Field-oriented indexing options

Resin creates and maintains an index per document field. 

You may opt out of indexing entirely. You may index unanalyzed data. You may choose to store data both is its original and its analyzed state or in one or the other.

Indexed fields (both analyzed and unanalyzed) can participate in queries. Preferably primary keys or paths used as identifiers should not be analyzed but certanly indexed.

## Compression

Stored document fields can be compressed individually with either QuickLZ or GZip. For unstructured data this leaves a smaller footprint on disk and enables faster writes.

Compressing documents affect querying performance very little. The reason for this is that no data needs to be read and deflated until scoring and pagination has been performed.

## Flexible and extensible

Most parts such as analyzers, tokenizers, scoring schemes and more are customizable.

## Runtime environment

Resin is built for .Net Core 1.1.

## CLI

### Some test data

[Gutenberg DVD](https://www.google.se/search?q=gutenberg+dvd+torrent&oq=gutenberg+dvd+torrent).  
[Wikipedia as JSON](https://dumps.wikimedia.org/wikidatawiki/entities/).

### Syntax

Clone the source or [download the latest source as a zip file](https://github.com/kreeben/resin/archive/master.zip), build and then run the CLI (rn.bat) with the following arguments:

	rn write --file source_json_filename --dir store_directory [--pk primary_key] [--skip num_of_items_to_skip] [--take num_to_take] [--gzip] [--lz]  
	rn query --dir store_directory -q query_statement [-p page_number] [-s page_size] [--net use_rpc_true_or_false]
	rn delete --ids comma_separated_list_of_ids --dir store_directory  
	rn merge --dir store_directory [--pk primary_key] [--skip num_of_items_to_skip] [--take num_to_take]  
  	rn export --source-file rdoc_filename --target-file json_filename
	rn status --dir store_directory
	rn start-servers --dir store_directory --ps posting_server_host_name --ds document_server_hostname --pport posting_port --dport document_port
E.g.:

	rn write --file c:\temp\wikipedia.json --dir c:\resin\data\wikipedia --pk "id" --skip 0 --take 1000000
	rn query --dir c:\resin\data\wikipedia -q "label:the good the bad the ugly" -p 0 -s 10
	rn delete --ids "Q1476435" --dir c:\resin\data\wikipedia
	rn merge --dir c:\resin\data\wikipedia --pk "id" --skip 0 --take 1000000
	rn rewrite --file c:\temp\resin_data\636326999602241674.rdoc --dir c:\temp\resin_data\pg --pk "url"
	rn export --source-file c:\temp\resin_data\636326999602241674.rdoc --target-file c:\temp\636326999602241674.rdoc.json
	rn status c:\resin\data\wikipedia
	rn start-servers --dir c:\resin\data\wikipedia --ps localhost --ds localhost --pport 11111 --dport 11112
	
## API
### A document (serialized).

	{
		"id": "Q1",
		"label":  "universe",
		"description": "totality of planets, stars, galaxies, intergalactic space, or all matter or all energy",
		"aliases": "cosmos The Universe existence space outerspace"
	}


### Store and index documents

	var docs = GetDocuments();
	var dir = @"c:\resin\data\mystore";
	
	// From memory
	using (var firstBatchDocuments = new InMemoryDocumentStream(docs))
	using (var writer = new UpsertTransaction(dir, new Analyzer(), Compression.NoCompression, primaryKey:"id", firstBatchDocuments))
	{
		long versionId = writer.Write();
	}
	
	// From stream
	using (var secondBatchDocuments = new JsonDocumentStream(fileName))
	using (var writer = new UpsertTransaction(dir, new Analyzer(), Compression.NoCompression, primaryKey:"id", secondBatchDocuments))
	{
		long versionId = writer.Write();
	}

	// Implement the base class DocumentStream to use any type of data in any format you need as your data source.

### Query the index.

	var result = new Searcher(dir).Search("label:good bad~ description:leone", page:0, size:15);

	// Document fields and scores, i.e. the aggregated tf-idf weights a document recieve from a simple 
	// or compound query, are included in the result:

	var scoreOfFirstDoc = result.Docs[0].Score;
	var label = result.Docs[0].Fields["label"];
	var primaryKey = result.Docs[0].Fields["id"];

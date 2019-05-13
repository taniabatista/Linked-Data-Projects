
from SPARQLWrapper import SPARQLWrapper, JSON, XML, RDF
import xml.dom.minidom



def getLocalLabel (instancia):
 	sparqlSesame = SPARQLWrapper("http://localhost:8080/rdf4j-server/repositories/SocialNetwork",  returnFormat=JSON)
	queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX sn:  <http://ciff.curso2015/ontologies/owl/socialNetwork#> SELECT ?label WHERE { sn:" + instancia + " rdfs:label ?label }"
	sparqlSesame.setQuery(queryString)
	sparqlSesame.setReturnFormat(JSON)
	query   = sparqlSesame.query()
	results = query.convert()
	devolver = []
	for result in results["results"]["bindings"]:
		label = result["label"]["value"]
		if 'xml:lang' in result["label"]:
			lang = result["label"]["xml:lang"]
		else:
			lang = None
		print "LABEL ---  " + label
		if 'xml:lang' in result["label"]:
			print "LANGUAGE --- " + lang
		devolver.append((label, lang))
	return devolver



def getDBpediaResource (label, lang, endpoint):
	sparqlDBPedia = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT ?s WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " . } "
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT ?s WHERE { ?s rdfs:label \"" + label + " . } "
	sparqlDBPedia.setQuery(queryString)
	sparqlDBPedia.setReturnFormat(JSON)
	query   = sparqlDBPedia.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"]
		print "RESOURCES --- " + resource


def getLinkedmdbResource (label, lang, endpoint):
	sparqlLinkedmdb = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT ?s WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " . } "
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT ?s WHERE { ?s rdfs:label \"" + label + "\"" "}"
	sparqlLinkedmdb.setQuery(queryString)
	sparqlLinkedmdb.setReturnFormat(JSON)
	query   = sparqlLinkedmdb.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"]
		print "RESOURCES --- " + resource

def getBNEResource (label, lang, endpoint):
	sparqlBNE = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT ?s WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " . } "
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT ?s WHERE { ?s rdfs:label \"" + label + "\"" "}"
	sparqlBNE.setQuery(queryString)
	sparqlBNE.setReturnFormat(JSON)
	query   = sparqlBNE.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"]
		print "RESOURCES ---  " + resource


if __name__ == '__main__':
	print "\n---------INSTANCIA 1------------\n"
	lista = getLocalLabel("instancia1");
	print lista
	endpoint = 'http://dbpedia.org/sparql';
	for result in lista:
		(label, lang) = result
		resource = getDBpediaResource (label, lang, endpoint);


	print "\n---------INSTANCIA 3------------\n"
	lista = getLocalLabel("instancia3");
	print lista
	endpoint = 'http://data.linkedmdb.org/sparql';
	for result in lista:
		(label, lang) = result
		resource = getLinkedmdbResource (label, lang, endpoint);

	print "\n---------INSTANCIA 4------------\n"
	lista = getLocalLabel("instancia4");
	print lista
	endpoint = 'http://datos.bne.es/sparql';
	for result in lista:
		(label, lang) = result
		resource = getBNEResource (label, lang, endpoint);

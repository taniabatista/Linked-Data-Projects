#CODE FOR ADDING 2 PROPERTIES TO INSTANCIA1
#ONLY TWO THINGS NEED TO BE CHANGEd
#    1. ADD MORE PREFIXES IN THE queryString
#    2. ADD THE PROPERTY BELOW RESOURCES HERE
#        for result in results["results"]["bindings"]:

from SPARQLWrapper import SPARQLWrapper, JSON, XML, RDF
import xml.dom.minidom

########### LOCAL
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


############## INSTANCIA 1 DBPEDIA
def getDBpediaResource (label, lang, endpoint):
	sparqlDBPedia = SPARQLWrapper(endpoint)
	if (lang):
        #EXPAND THE PREFIXES IN THE QUERY STRING, TO INCLUDE ALL THE SOURCES
	    queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX dbo: <http://dbpedia.org/ontology/> SELECT ?s ?birthDate ?birthPlace WHERE { ?s dbo:birthDate ?birthDate . ?s dbo:birthPlace ?birthPlace . ?s rdfs:label \"" + label + "\"@" +lang + " . }";
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT ?s WHERE { ?s rdfs:label \"" + label + " . } "
	sparqlDBPedia.setQuery(queryString)
	sparqlDBPedia.setReturnFormat(JSON)
	query   = sparqlDBPedia.query()
	results = query.convert()

    #############   ADD THESE LINES BELOW  #######
	print "\n*********RESULTS FOR PROPERTIES AND RESOURCES*******\n"
    #### THIS PART STAYS ALMOST THE SAME
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"] # resource IS THE PLURAL VALUE
        # JUST INCLUDE THE PROPERTIES
		birthDate = result["birthDate"]["value"]
		birthPlace = result["birthPlace"]["value"]
		print "\n****************************************************\n"
		print "RESOURCES ---: " + resource
		print "BIRTH DATE ---: " + birthDate
		print "BIRTH PLACE  ---: " + birthPlace
		#


############## INSTANCIA 3 get linkedmbd
def getLinkedmdbResource (label, lang, endpoint):
	sparqlLinkedmdb = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> SELECT ?s ?runtime ?releasedate WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " .  ?s movie:runtime ?runtime. ?s movie:initial_release_date ?releasedate .} "
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> SELECT ?s ?runtime ?releasedate WHERE { ?s rdfs:label \"" + label + "\"" ". ?s movie:runtime ?runtime. ?s movie:initial_release_date ?releasedate .}"
	sparqlLinkedmdb.setQuery(queryString)
	sparqlLinkedmdb.setReturnFormat(JSON)
	query   = sparqlLinkedmdb.query()
	results = query.convert()
    #############   ADD THESE LINES BELOW  #######
    #### THIS PART STAYS ALMOST THE SAME
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"] # resource IS THE PLURAL VALUE
        # JUST INCLUDE THE PROPERTIES
		releasedate = result["releasedate"]["value"]
		print "\n****************************************************\n"
		print "RESOURCE ----: " + resource
		print "RELEASE DATE ----: " + releasedate
        		#


def getBNEResource (label, lang, endpoint):
	sparqlBNE = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX ns8:<http://id.loc.gov/authorities/names/> PREFIX ns1:<http://datos.bne.es/resource/> PREFIX ns2:<http://datos.bne.es/def/> SELECT ?s ?biography WHERE { ?s rdfs:label \"" + label + "\"@es . ?s ns2:P3067 ?biography .} "
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX ns8:<http://id.loc.gov/authorities/names/> PREFIX ns1:<http://datos.bne.es/resource/> PREFIX ns2:<http://datos.bne.es/def/> SELECT ?s ?biography WHERE { ?s rdfs:label \"" + label + "\"" ". ?s ns2:P3067 ?biography .}"
	sparqlBNE.setQuery(queryString)
	sparqlBNE.setReturnFormat(JSON)
	query   = sparqlBNE.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"]
		print "\n****************************************************\n"
		biography = result["biography"]["value"]
		print "RESOURCES ---  " + resource
		print "BIOGRAPHY ---- " + biography






##############
if __name__ == '__main__':
	print "\n-----------------------INSTANCIA 1---------------------------------\n"
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

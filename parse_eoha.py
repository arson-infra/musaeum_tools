import json
nodes = []
links = []
with open('eoha-json.json') as f:
    json_string = json.load(f)
    for obj in json_string:
        if 'http://www.w3.org/2000/01/rdf-schema#subClassOf' in obj:
            node = { 'id' : obj['@id']}
            nodes.append(node)
            if len(obj['http://www.w3.org/2000/01/rdf-schema#subClassOf']) >= 1: 
                for link in obj['http://www.w3.org/2000/01/rdf-schema#subClassOf']:
                    link = {'source' : link["@id"], 'target' : obj["@id"]}
                    links.append(link)  

data = [nodes, links]
with open('eoja.json', 'w') as e:
    json.dump(data, e)
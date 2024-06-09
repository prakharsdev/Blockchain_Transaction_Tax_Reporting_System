import apache_beam as beam
import json

def parse_json(element):
    return json.loads(element)

def format_as_json(element):
    return json.dumps(element)

class PrintElement(beam.DoFn):
    def process(self, element):
        print(element)
        yield element

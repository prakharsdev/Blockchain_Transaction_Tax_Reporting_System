import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class TransformData(beam.DoFn):
    def process(self, element):
        return [{
            'symbol': element['symbol'],
            'price_24h': element['price_24h'],
            'volume_24h': element['volume_24h'],
        }]

def run():
    options = PipelineOptions()
    p = beam.Pipeline(options=options)

    input_path = 'gs://your-bucket/raw/blockchain_data.json'
    output_path = 'gs://your-bucket/processed/blockchain_data_transformed.json'

    (p
     | 'Read' >> beam.io.ReadFromText(input_path)
     | 'Parse JSON' >> beam.Map(json.loads)
     | 'Transform Data' >> beam.ParDo(TransformData())
     | 'Write' >> beam.io.WriteToText(output_path)
    )

    p.run().wait_until_finish()

if __name__ == '__main__':
    run()

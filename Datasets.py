import os.path

from Sample import Sample

from lxml import etree
import Metadata


def create_sample(db_path, noise_node):
   path = db_path + os.path.sep + noise_node.xpath("./relativeFilepath")[0].text
   sample_rate, channels, duration = Metadata.get_audio_metadata(path)
   return Sample(path, sample_rate, channels, duration)

def getAudioData(xml_path):
    tree = etree.parse(xml_path)
    root = tree.getroot()
    db_path = root.find("./databaseFolderPath").text
    tracks = root.findall(".//track")

    samples = list()

    for track in tracks:
        # Get mix and sources
        speech = create_sample(db_path, track.xpath(".//source[sourceName='Speech']")[0])
        mix = create_sample(db_path, track.xpath(".//source[sourceName='Mix']")[0])
        noise = create_sample(db_path, track.xpath(".//source[sourceName='Noise']")[0])

        samples.append((mix, noise, speech))

    return samples

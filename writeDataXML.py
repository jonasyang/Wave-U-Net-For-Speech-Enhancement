from lxml import etree
import os

def Generate(mixedDir, cleanDir, outDir, realtiveRoot):
    rootElement = etree.Element('Data')
    etree.SubElement(rootElement, 'databaseFolderPath').text = ''
    absRoot = os.path.abspath(realtiveRoot)

    for root, dirs, files in os.walk(mixedDir):
        for file in files:
            cleanFile = os.path.abspath(os.path.join(cleanDir, file))
            mixedFile = os.path.abspath(os.path.join(root, file))
            outFile = os.path.abspath(os.path.join(outDir, file))
            cleanFile = cleanFile[absRoot.__len__() + 1:]
            mixedFile = mixedFile[absRoot.__len__() + 1:]
            outFile = outFile[absRoot.__len__() + 1:]

            track = etree.SubElement(rootElement, 'track')
            source = etree.SubElement(track, 'source')
            etree.SubElement(source, 'sourceName').text = 'Speech'
            etree.SubElement(source, 'relativeFilepath').text = cleanFile.replace('\\', '/')
            
            source = etree.SubElement(track, 'source')
            etree.SubElement(source, 'sourceName').text = 'Mix'
            etree.SubElement(source, 'relativeFilepath').text = mixedFile.replace('\\', '/')

            source = etree.SubElement(track, 'source')
            etree.SubElement(source, 'sourceName').text = 'Noise'
            etree.SubElement(source, 'relativeFilepath').text = outFile.replace('\\', '/')
    
    etree.ElementTree(rootElement).write('data.xml', pretty_print=True)

Generate(
    r"""E:\Wave_U_Net_Data\2791\noisy_trainset_56spk_wav""",
    r"""E:\Wave_U_Net_Data\2791\clean_trainset_56spk_wav""",
    r"""E:\Wave_U_Net_Data\2791\train_generated_wav""",
    r"""E:\Wave_U_Net_Data\2791"""
)
import sys
import invert_and_mix_audio
import os

def Genearte(mixedDir, cleanDir, outDir):
    for root, dir, files in os.walk(mixedDir):
        for file in files:
            invert_and_mix_audio.Convert(os.path.join(root, file), os.path.join(cleanDir, file), os.path.join(outDir, file))


Genearte(
    r"""E:\Wave_U_Net_Data\1942\noisy_testset_wav""",
    r"""E:\Wave_U_Net_Data\1942\clean_testset_wav""",
    r"""E:\Wave_U_Net_Data\1942\test_generated_wav""")

Genearte(
    r"""E:\Wave_U_Net_Data\1942\noisy_trainset_wav""",
    r"""E:\Wave_U_Net_Data\1942\clean_trainset_wav""",
    r"""E:\Wave_U_Net_Data\1942\train_generated_wav""")

Genearte(
    r"""E:\Wave_U_Net_Data\2791\noisy_trainset_56spk_wav""",
    r"""E:\Wave_U_Net_Data\2791\clean_trainset_56spk_wav""",
    r"""E:\Wave_U_Net_Data\2791\train_generated_wav""")

Genearte(
    r"""E:\Wave_U_Net_Data\2791\noisy_testset_wav""",
    r"""E:\Wave_U_Net_Data\2791\clean_testset_wav""",
    r"""E:\Wave_U_Net_Data\2791\test_generated_wav""")
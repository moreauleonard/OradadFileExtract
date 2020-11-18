from config import Settings
from oradad_file import OradadFile
from datetime import datetime
from pathlib import Path

PRIVATE_KEY = '/Users/leo/Documents/Programmation/test_oradad_uncrypt/ORADAD_Extract/private.pem'
COMPRESSED_FILE = '//Users/leo/Documents/Programmation/test_oradad_uncrypt/compressed/metadata.tsv.oradad'
ENCRYPTED_FILE = '/Users/leo/Documents/Programmation/test_oradad_uncrypt/encrypted/metadata.tsv.oradad'
ENCRYPTED_AND_COMPRESSED_FILE = '/Users/leo/Documents/Programmation/test_oradad_uncrypt/ORADAD_tars/ace.lan_20201003-072800/ace.lan/20201003-072800/metadata.tsv.oradad'
ENCRYPTED_AND_COMPRESSED_FILE = '/Users/leo/Documents/Programmation/test_oradad_uncrypt/ORADAD_tars/vsiparis.local_20201110-112110/vsiparis.local/20201110-112110/domaindns/vsiparis.local/top.tsv.oradad'


ENC_DIR = "/Users/leo/Documents/Programmation/test_oradad_uncrypt/ORADAD_tars/ace.lan"

if __name__ == "__main__":
    start_time = datetime.now()
    for oradadfile in list(Path(ENC_DIR).rglob("*.oradad")):
        file = OradadFile(str(oradadfile), private_key_file=PRIVATE_KEY)
        file.process()
        print("Processed file {0} in {1}s".format(oradadfile, file.processed_time.total_seconds()))
    print("Total elapsed time: {0}s".format((datetime.now() - start_time).total_seconds()))
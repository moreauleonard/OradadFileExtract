from config import Settings
from oradad_file import OradadFile
from datetime import datetime
from pathlib import Path

PRIVATE_KEY = './private.pem'
ENC_DIR = "./ORADAD_tars/domain.local"

if __name__ == "__main__":
    start_time = datetime.now()
    for oradadfile in list(Path(ENC_DIR).rglob("*.oradad")):
        file = OradadFile(str(oradadfile), private_key_file=PRIVATE_KEY)
        file.process()
        print("Processed file {0} in {1}s".format(oradadfile, file.processed_time.total_seconds()))
    print("Total elapsed time: {0}s".format((datetime.now() - start_time).total_seconds()))
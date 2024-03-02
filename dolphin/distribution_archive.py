from .bridge_page import BridgePage
from . import script_indexer
import zipfile


class DistributionArchive:
    def __init__(self, file):
        self.archive = zipfile.ZipFile(file, compression=zipfile.ZIP_DEFLATED, compresslevel=9)

        bridge_page_contents = self.archive.read('main.html')
        self.bridge_page = BridgePage(bridge_page_contents.decode('utf-8'))
        self.bridge_page.parse()

        self.indexed_scripts = {}
        self.index_bridge_page_scripts()

    def index_bridge_page_scripts(self):
        for script in self.bridge_page.scripts:
            script_contents = self.archive.read(script)
            self.indexed_scripts[script] = \
                script_indexer.index_script(script_contents.decode('utf-8'))

        return self.indexed_scripts

from html.parser import HTMLParser


class BridgePageParser(HTMLParser):
    def __init__(self, script_callback):
        self.script_callback = script_callback
        super().__init__(convert_charrefs=True)

    def get_specific_attribute_value(self, needed_attribute, attributes):
        for attribute in attributes:
            if attribute[0] == needed_attribute:
                return attribute[-1]

    def handle_starttag(self, tag, attributes):
        if tag != 'script':
            return

        src_value = self.get_specific_attribute_value("src", attributes)

        if src_value:
            self.script_callback(src_value)


class BridgePage:
    def __init__(self, contents):
        self.parser = BridgePageParser(self.script_callback)
        self.contents = contents
        self.scripts = []

    def parse(self):
        self.parser.reset()
        self.parser.feed(self.contents)

        return self.scripts

    def script_callback(self, script_path):
        if script_path not in self.scripts:
            return self.scripts.append(script_path)

# TCP
raw_data_1 = b'RT\x00\x125\x02\x08\x00\'T\xec\xcd\x08\x00E\x00\x00(\xfe"@' \
             b'\x00@\x06\xd5\xa2\n\x00\x02\x0f\\z\xfe\x81\xd9\x96\x01\xbbH;}' \
             b'\xa9\x10\x960\xe9P\x10\xf9\x9cg%\x00\x00'
# UDP
raw_data_2 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00E\x00' \
             b'\x00J\xeb\xc3@\x00@\x11P\xa9\x7f\x00\x00\x01\x7f\x00\x005\x9a' \
             b'\xfc\x005\x006\xfe}i\xed\x01\x00\x00\x01\x00\x00\x00\x00\x00' \
             b'\x01\x02ru\nwiktionary\x03org\x00\x00\x01\x00\x01\x00\x00)' \
             b'\x04\xb0\x00\x00\x00\x00\x00\x00'


class Args:
    def __init__(self, count=1,
                 headers='eth and (ipv4 or ipv6) and (tcp or udp)',
                 special='any',
                 report=['ip', 'count', 'bytes'], filename='test.pcap_files'):
        self.packets_count = count
        self.headers = headers
        self.specials = special
        self.binary_mod = False
        self.report = report
        self.filename = filename


class TestReport:
    def __init__(self, report):
        self.a = None
        self.report = ['ip', 'count', 'bytes']
        self.s = 0

    def add(self, packet, size):
        self.a = packet
        self.s = size


class TestEthernet:
    def __init__(self):
        self.packet_name = 'eth'
        self.level = 'data_link'

    def to_str(self):
        return self.packet_name


class TestIpv4:
    def __init__(self):
        self.packet_name = 'ipv4'
        self.level = 'network'
        self.d_ip = '000.000.000.000'

    def to_str(self):
        return self.packet_name


class TestTCP:
    def __init__(self):
        self.packet_name = 'tcp'
        self.level = 'transport'
        self.s_port = '80'

    def to_str(self):
        return self.packet_name


class TestSocket:
    ADDRESS = ""

    def __init__(self):
        self.data = raw_data_1

    def receive_from(self):
        return self.data

    def get(self):
        return self

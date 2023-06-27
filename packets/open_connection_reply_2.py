from packets.packet import Packet


class OpenConnectionReply2(Packet):
    packet_id = 0x08
    magic: bytes = None
    server_guid: int = None
    client_address: bytes = None
    mtu_size: int = None
    encryption_enabled: bool = None
    
    def decode_payload(self):
        self.write_magic(self.magic)
        self.write_long(self.server_guid)
        if not isinstance(self.magic, bytes):
            self.magic = self.magic.encode('utf-8')
        self.client_address = self.write_address() # This is wrong. Waiting for fix
        self.write("\x00" * self.mtu_size)
        self.write_bool(self.encryption_enabled)

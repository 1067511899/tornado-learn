import socket
import struct
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
while 1:
    recPacket, addr = s.recvfrom(1024)
    icmp_header = recPacket[20:28]
    type, code, checksum, p_id, sequence = struct.unpack('bbHHh', icmp_header)
    print ("type: [" + str(type) + "] code: [" + str(code) + "] checksum: [" + str(checksum) + "] p_id: [" + str(p_id) + "] sequence: [" + str(sequence) + "]")

'''
WSAETIMEDOUT (10060)

The connection failed due to an error or timeout.

Verify that the destination IP address is correct.

Increase the connection timeout threshold under Global Settings | Connection.

Switch to the opposite data connection type (PASV or PORT) under Site Settings | Type tab.

Verify that the problem is not local by trying to connect to an alternate server.

If a server name was used, verify it resolves to the correct address.

If using a local server table for server name resolution, check to see that it doesn't resolve to an obsolete address.

Try pinging the address.

If you are using a router, verify the router is up and running (check by pinging it and then ping an address outside of the router).

Do a traceroute to the destination to verify all routers along the connection path are operational.

Verify that your subnet mask is setup properly.

 
'''
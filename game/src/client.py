from match_client.match import Match
from match_client.match.ttypes import User

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from sys import stdin

def operator(op, user_id, user_name, score):
    # Make socket
    transport = TSocket.TSocket('localhost', 9090) # 匹配的服务器在本地, 所以是本地地址

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Match.Client(protocol)

    # Connect!
    transport.open()

    user = User(user_id, user_name, score)
    if op == "add": client.add_user(user, "")
    elif op == "remove": client.remove_user(user, "")

    # Close!
    transport.close()

def main():
    for line in stdin:
        op, user_id, user_name, score = line.split(' ')
        operator(op, int(user_id), user_name, int(score))


if __name__ == "__main__":
    main()

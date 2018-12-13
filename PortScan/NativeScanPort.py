import optparse
from socket import *
import traceback
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):

    with socket(AF_INET, SOCK_STREAM) as connSkt:
        try:
            connSkt.connect((tgtHost, tgtPort))
            connSkt.send(b'ViolentPython\r\n')
            results = connSkt.recv(100)
            screenLock.acquire()
            print('Scanning port:%s' % tgtPort)
            print('[+]%d/tcp open' % tgtPort)
            print('[+] ' + str(results))
        except:
            # print(traceback.print_exc())
            screenLock.acquire()
            print('Scanning port:%s' % tgtPort)
            print('[-]%d/tcp closed' % tgtPort)

        finally:
            screenLock.release()
def portScan(tgtHost, tgtPorts):
    try:
        tgt_ip = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host "%tgtHost)
        return None
    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print('\n[+] Scan Results for :'+tgt_name[0])
    except:
        print('\n[+] Scan Results for:'+tgt_ip)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:

        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        # connScan(tgtHost, int(tgtPort))
def main():
    parser = optparse.OptionParser('usage %prog -H' + \
                                   '<tartget host> -P <target port>')

    parser.add_option('-H', dest='tgtHost', type='string', \
                      help='specify target host')

    parser.add_option('-P', dest='tgtPort', type='string', \
                      help='specify target port')

    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print('[-] You must specify a target host and port[s].')
        exit(0)

    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
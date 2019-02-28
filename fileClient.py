import socket

def Main():
    host = '192.168.1.9'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    filename = input("Filename? -> ")
    if filename != 'q':
        s.send(filename.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        if data[:6] == 'EXISTS':
            filesize = int(data[6:])
            message = input("File Exists, " + str(filesize) + "Bytes, download? [Y/N] -> ")
            if message == 'Y':
                s.send('OK'.encode('utf-8'))
                f = open('new_' + filename, 'wb')
                data = s.recv(1024).decode('utf-8')
                totalRecv = len(data)
                f.write(data.encode('utf-8'))
                while totalRecv < filesize:
                    data = s.recv(1024).decode('utf-8')
                    totalRecv += len(data)
                    f.write(data.encode('utf-8'))
                    print("(0:.2f)".format((totalRecv/float(filesize))*100 + "% Done"))
                print("Download Complete")

        else:
            print("File does not exist!")
    s.close()

if __name__ == '__main__':
    Main()

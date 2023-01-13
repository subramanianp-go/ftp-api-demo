from ftplib import FTP
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"
ftp = FTP(FTP_HOST)
ftp.encoding = "utf-8"

def uploadFile(filename):
    # filename = "sales-sample.csv"
    ftp.login(FTP_USER, FTP_PASS)
    with open(filename, "rb") as file:
        ftp.storbinary("STOR sales-sample.csv", file)
    # ftp.quit()



def listFiles():
    ftp.login(FTP_USER, FTP_PASS)
    data = []
    ftp.dir(data.append)
    # ftp.quit()
    return data

# with open(filename, "rb") as file:
#     ftp.retrbinary("RETR sales-sample.csv", file.write)
#
def downloadFile(remoteFilename):
    ftp.login(FTP_USER, FTP_PASS)
    remoteFilename = 'sales-sample.csv'
    localFilename = 'downloaded-' + remoteFilename
    localFile = open(localFilename, 'wb')
    ftp.retrbinary('RETR ' + remoteFilename, localFile.write, 1024)
    # ftp.quit()
    localFile.close()

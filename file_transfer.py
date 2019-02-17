from ftplib import FTP

pi = '172.30.1.150'

def connect():
	ftp = FTP(pi)
	ftp.login('pi', 'WordPass1')
	return ftp

def retrieve_frame(ftp, filepath):
	ftp.cwd('/home/pi/Documents/hack@CEWIT19/imgs')
	ftp.retrbinary('RETR %s' % 'lastsnap.jpg', open(filepath, "wb").write)

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile,  outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished Background zip of :', self.infile)


if __name__ == "__main__":
    background = AsyncZip('test.txt', 'myarchive.zip')
    background.start()

    print('The main program continues to run in foreground.')

    background.join()   #Wait for the background task to finish
    print('Main program waited until background was done')
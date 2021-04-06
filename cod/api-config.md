$ git clone https://github.com/AlexeyAB/darknet.git
$ cd Darknet
$ sed -i 's/OPENCV=0/OPENCV=1/' Makefile
$ sed -i 's/LIBSO=0/LIBSO=1/' Makefile
$ sed -i 's/DEBUG=0/DEBUG=1/' Makefile
$ make

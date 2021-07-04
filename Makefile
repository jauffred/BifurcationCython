PYTHON_INCLUDE=/home/jauffred/anaconda3/include/python3.7m

CPP_FLAGS= -c -O3 -std=c++14 -fPIC -march=native -mtune=native

all:BifurcationCy.so 


BifurcationCy.cpp: BifurcationCy.pyx
	cython --cplus BifurcationCy.pyx

BifurcationCy.o: BifurcationCy.cpp
	g++ $(CPP_FLAGS) -I$(PYTHON_INCLUDE) BifurcationCy.cpp

BifurcationCy.so: BifurcationCy.o
	g++ -shared -fwrapv -o BifurcationCy.so BifurcationCy.o

clean:
	rm *.o;rm BifurcationCy.cpp


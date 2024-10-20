all:
g++ -std=c++11 -c -fPIC fibonacci.cpp -o fibo.o
g++ -std=c++11 -shared -o libfibo.so  fibo.o	
clean:
rm -fr *.o *.so __pycache__
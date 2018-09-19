#ifndef BMPFILE_H_

#include <windows.h>
#include <stdio.h>

class BMPFile {
public:
	SaveBMP(const char *filename, unsigned char *buffer, int width, int height);

};

#endif

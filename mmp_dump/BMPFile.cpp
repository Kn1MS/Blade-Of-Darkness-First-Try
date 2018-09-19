#include "BMPFile.h"
#include <assert.h>

int BMPFile::SaveBMP(const char *filename, 
					 unsigned char *buffer, 
					 int width, 
					 int height)
{
	FILE *f = fopen(filename, "wb");
	assert(f != NULL);

	// BITMAP FILE HEADER

	BITMAPFILEHEADER bfh;
	bfh.bfType = ((WORD) ('M' << 8) | 'B');
	bfh.bfSize = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + width*height*3;
	bfh.bfReserved1 = 0;
	bfh.bfReserved2 = 0;
	bfh.bfOffBits = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

	fwrite(&bfh, sizeof(BITMAPFILEHEADER), 1, f);


	// BITMAPINFOHEADER

	BITMAPINFOHEADER bih;
	bih.biSize = sizeof(BITMAPINFOHEADER);
	bih.biWidth = width;
	bih.biHeight = height;
	bih.biPlanes = 1;
	bih.biBitCount = 24;
	bih.biCompression = BI_RGB;
	bih.biSizeImage = 0; // Set to zero for uncompressed
	bih.biXPelsPerMeter = 0;
	bih.biYPelsPerMeter = 0;
	bih.biClrUsed = 0;
	bih.biClrImportant = 0;

	fwrite(&bih, sizeof(BITMAPINFOHEADER), 1, f);

	int row_bytes = width*3;
	unsigned char *buf = buffer;
	for (int i=height-1; i>=0; --i) {
		buf = buffer + width*3*i;
		for (int j=0; j<width; ++j) {
			// must be written in BGR format
			fwrite(&buf[3*j+2], 1, 1, f);
			fwrite(&buf[3*j+1], 1, 1, f);
			fwrite(&buf[3*j], 1, 1, f);
		}
	}
	fclose(f);
}
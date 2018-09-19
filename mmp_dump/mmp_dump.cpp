#include <stdio.h>
#include "BMPFile.h"


int main(int argc, char **argv)
{
	if (argc < 2) {
		printf("Format: mmp_dump file.mmp\n");
		return 1;
	}
	
	FILE *f = fopen(argv[1], "rb");
	if (f == NULL) {
		printf("Couldn't open %s\n", argv[1]);
		return 1;
	}

	int ntextures;
	fread(&ntextures, 4, 1, f);
	printf("File %s has %d textures\n", argv[1], ntextures);

	BMPFile bmp;

	for (int i=0; i<ntextures; ++i) 
	{
		int two;
		fread(&two, 2, 1, f);
		
		int checksum;
		fread(&checksum, 4, 1, f);

		int size;
		fread(&size, 4, 1, f);

		int len;
		fread(&len, 4, 1, f);
		char *name = (char *) malloc(len+5);
		fread(name, 1, len, f);
		name[len] = '.';
		name[len+1] = 'b';
		name[len+2] = 'm';
		name[len+3] = 'p';
		name[len+4] = '\0';

		int type;
		fread(&type, 4, 1, f);

		int width, height;
		fread(&width, 4, 1, f);
		fread(&height, 4, 1, f);

		int data_len = size - 12;
		unsigned char *data = (unsigned char *) malloc(data_len);
		fread(data, 1, data_len, f);

		printf("Saving %s, (%dx%d, ", name, width, height, type, size);

		// Write the bitmap
		switch (type) {
		case 1:
			{
				printf("paletted)\n");
				unsigned char *palette = data + width*height;//data_len - 768+3;
				unsigned char *truecolour = (unsigned char *) malloc(width*height*3);
				for (int j=0; j<height; ++j)
					for (int k=j*width; k<(j+1)*width; ++k) {
						truecolour[3*k] = palette[data[k]*3] << 2;
						truecolour[3*k+1] = palette[data[k]*3+1] << 2;
						truecolour[3*k+2] = palette[data[k]*3+2] << 2;
					}
				bmp.SaveBMP(name, truecolour, width, height);
				free(truecolour);
				break;
			}
		case 2:
			{
				printf("alpha)\n");
				unsigned char *truecolour = (unsigned char *) malloc(width*height*3);
				for (int j=0; j<height; ++j)
					for (int k=j*width; k<(j+1)*width; ++k) {
						truecolour[3*k]   = data[k];
						truecolour[3*k+1] = data[k];
						truecolour[3*k+2] = data[k];
					}
				bmp.SaveBMP(name, truecolour, width, height);
				free(truecolour);
				break;
			}
		case 4:
			{
				printf("true colour)\n");
				bmp.SaveBMP(name, data, width, height);
				break;
			}
		default:
			printf("Sorry, I don't know the type %d of texture %s\n", type, name);
		}

		free(data);
		free(name);
	}



	return 0;
}
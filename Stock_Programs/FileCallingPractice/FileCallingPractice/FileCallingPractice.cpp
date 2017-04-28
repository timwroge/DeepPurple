#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>




int main(void) {
	FILE *inputfilepointer;
	fscanf(inputfilepointer, "oneRow.dat", "r");
	int x[10];
	//inputting the data into the vector x
	int status = 1;
	int i = 0;
	while (status == 1) {
		status = fscanf(inputfilepointer, "%d", &x[i]);
		while (status == 1) {
			i++;
		}


	}
	int n = i;
	//print the values of x
	for (i = 0; i < n; i++) {

		printf("x[%d]= %d\n", i, x[i]);
	}


	return 0;
}
#include <stdio.h>
#include <iostream>
#include <float.h>
#include <limits.h>
#include <time.h>
struct vect {
	double x;
	double y;
	int pos;
};
vect arr[20] = { {62.0,58.4,1}, {57.5,56.0,2}, {51.7,56.0,3}, {67.9,19.6,4},
				 {57.7,42.1,5}, {54.2,29.1,6}, {46.0,45.1,7}, {34.7,45.1,8},
				 {45.7,25.1,9}, {34.7,26.4,10}, {28.4,31.7,11}, {33.4,60.5,12},
	   			 {22.9,32.7,13}, {21.5,45.8,14}, {15.3,37.8,15}, {15.1,49.6,16},
	             {9.1,52.8,17}, {9.1,40.3,18}, {2.7,56.8,19}, {2.7,33.1,20}
				};
void gen_perm(int k, int n, int i, vect* P,vect* minP,double& min,bool first) {
	int q;

	if (k == -1) {
		for (q = 0; q < n; q++) {
			P[q] = {0.0,0.0};
		}
	}
	if( k != -1)
	P[i] = arr[k];

	if (k == n - 1) {
		double tren = 0;
		for (int j = 0; j < n-1; j++) {
			tren += sqrt((P[j + 1].y - P[j].y)*(P[j + 1].y - P[j].y) + (P[j + 1].x - P[j].x)*(P[j + 1].x - P[j].x));
		}
		if (tren < 0) {
			std::cout << tren;
		}
		if (min > tren) {
			min = tren;
			for (int j = 0; j < n; j++) {
				minP[j] = P[j];
			}
		}

	}

	for (q = 0; q < n; q++) {
		if (P[q].x == 0 && P[q].y==0) {
			gen_perm(k + 1, n, q, P,minP,min,false);
		}
	}
	P[i] = { 0.0,0.0 };
	if (first) {
		std::cout<<"The smallest distance is: "<< min <<std::endl;
		for (int j = 0; j < n; j++) {
			printf("%d ", minP[j].pos);
		}
	}
}

int main() {
	int N = 12;
	clock_t start = clock();
	vect* P = new vect[N];
	vect* minP = new vect[N];
	double val = DBL_MAX;
	gen_perm(-1, N, 0, P, minP, val, true);
	printf("\nTime taken: %.2fs\n", (double)(clock() - start) / CLOCKS_PER_SEC);
	int x;
	scanf_s("%d", &x);
}
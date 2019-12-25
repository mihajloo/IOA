#include <stdio.h>
#include <iostream>

using namespace std;
double matrica[4][6] = {
			{ 1, -20, -30, 0, 0, 0 },
			{ 0, 3, 1, 1, 0, 0 },
			{ 0, 1, 6, 0, 1, 0 },
			{ 0, 1, 3, 0, 0, 1 } };

double niz[] = { 0, 99, 288, 75 };

int nizIndex[3];
 long fun(long a, long b) {
	return 20 * a + 30 * b;
}

void main() {
	int i = 1;
	while (true) {
		bool imaNegativnih = false;
		
		double minNeg = INT_MAX;
	
		for (int k =1 ; k <= 2; k++) {
			if (matrica[0][k] != 0) {
				imaNegativnih = true;
				if (matrica[0][k] < minNeg && matrica[0][k]<0) {
					minNeg = matrica[0][k];
					i = k;
				}
			}
		}
		// i = 1
		cout << "i = " << i << endl;
		if (imaNegativnih == false)
			break;

		int j = 1;
		double min = INT_MAX;
		int minJ = 0;

		for (; j < 4; j++) {
			if (matrica[j][i] > 0 && ((niz[j]+0.0)/ matrica[j][i]) < min) {
				min = ((niz[j] + 0.0) / matrica[j][i]);
				minJ = j;
			}
		}
		cout <<"minJ = "<< minJ << endl;
		nizIndex[i] = minJ;
		// minJ = 2
		double m = matrica[minJ][i];

		cout << "m = " << m << endl;
		for (int k = 0; k < 6; k++) {
			matrica[minJ][k] = (matrica[minJ][k] + 0.0) / m;
		}
		niz[minJ] = (niz[minJ] + 0.0) / m;
		for (int k = 0; k < 4; k++) {
			if (k != minJ && matrica[k][i] != 0) {
				double odnos = (-1)*(matrica[k][i] / matrica[minJ][i]);

				for (int l = 0; l < 6; l++) {
					
					 matrica[k][l] += matrica[minJ][l] * odnos;
				}
				niz[k] += niz[minJ] * odnos;
			}
		}
		
		

		for (int q = 0; q < 4; q++) {
			for (int w = 0; w < 6; w++) {
				cout << matrica[q][w] << " ";
			}
			cout << endl;
		}

		for (int i = 0; i < 4; i++) {
			cout << niz[i] << endl;
		}

		cout << endl << endl << endl;
	}

	
	double max = niz[0];
	double x1 = niz[nizIndex[1]];
	double x2 = niz[nizIndex[2]];
	cout << nizIndex[1] << ", " << nizIndex[2]<<endl;
	cout << "max = " << max << ", x1 = " << x1 << ", x2 = " << x2 << endl;
	int a;
	scanf_s("%d", &a);
	/*System.out.println("max = " + max + ", x1 = " + x1 + ", x2 = " + x2);

	long x11 = Math.round(x1) - 3;
	long x21 = Math.round(x2) - 3;
	long maxA = 0, maxB = 0, maxZ = 0;

	for (int q = 0; q < 6; q++) {
		for (int w = 0; w < 6; w++) {
			long AC = x11 + q;
			long BC = x21 + w;
			if (fun(AC, BC) > maxZ)
				if (3 * AC + BC <= 99)
					if (AC + 6 * BC <= 288)
						if (AC + 3 * BC <= 75) {
							maxA = x11 + q;
							maxB = x21 + w;
							maxZ = fun(x11 + q, x21 + w);
						}
		}
	}

	System.out.println("max = " + maxZ + ", x1 = " + maxA + ", x2 = " + maxB);*/
}
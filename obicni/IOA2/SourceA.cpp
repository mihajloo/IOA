#include <stdio.h>
#include <iostream>

using namespace std;


void main() {
	
	cout << "IOA 2a" << endl;
	for (int a1 = 1; a1 < 712; a1++) {
	
	
		for (int a2 = a1; a2 < 712; a2++) {

			for (int a3 = a2; a3 < 712; a3++) {

				for (int a4 = a3; a4 < 712; a4++) {

					if ((a1 + a2 + a3 + a4) == 711 && a1*a2*a3*a4 == 711000000) {
						cout << "The numbers are: " << (a1 +0.0)/100 <<" "<< (a2 + 0.0) / 100 << " "<<(a3 + 0.0) / 100 << " " << (a4 + 0.0) / 100 << endl;
						int ax;
						scanf_s("%d", &ax);
					}
				//	cout << a1 << " " << a2 << " " << a3 << " " << a4 << endl;
				}

			}
		}
	}
	int x;
	scanf_s("%d", &x);
}
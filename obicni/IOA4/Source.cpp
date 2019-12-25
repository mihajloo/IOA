#define _USE_MATH_DEFINES
#include <stdio.h>
#include <iostream>
#include <cmath>


using namespace std;

double F(double x) {
	double koef[] = { 46189L, 0, -109395L, 0, 90090L, 0, -30030L, 0, 3465L, 0, -63 };
	double exp = 10;
	double F = 0.0;

	for (int i = 0; i < 11; i++) {

		F += koef[i] * pow(x, exp);
		exp--;
	}

	return F;
}
void main() {

	const int n = 10;
	for (double i = 1.0; i <= n; i++) {
		double Xapp = cos(M_PI * ((i - 0.25) / (n + 0.5)));

		double pr = 0.01;

		int p = 0;
		while (p < 14) {
			double a = Xapp - pr;
			double b = Xapp + pr;

			Xapp = (a * F(b) - b * F(a)) / (F(b) - F(a));
			pr *= 0.1;

			p++;
		}
		cout<<"Nula: " << Xapp;
		int a;
		scanf_s("%d", &a);
	}

}
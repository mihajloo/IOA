#define _USE_MATH_DEFINES

#include <stdio.h>
#include <iostream>
#include <complex>

using namespace std;

complex<double> f(int n, double delta, double beta, double d, double teta) {
	complex<double> fs;
	fs.imag(0.0);
	fs.real(0.0);
	double fi = delta + beta * d*cos(teta);
	for (int k = 0; k < n; k++) {
		complex<double> stepen;
		stepen.real(0.0);
		stepen.imag(-1.0*fi*k);
		fs += pow(M_E, stepen);
	}
	return fs;
}
void main() {
	FILE* out;
	fopen_s(&out, "out.txt", "w");
	complex<double> Fs;
	Fs.real(0.0);
	Fs.imag(0.0);
	double moduo = 0.;
	for (double i = 0; i < 2 * M_PI; i += 2 * M_PI / 100) {
		Fs = f(5, i, 20 * M_PI, 1.0 / 20, M_PI / 4);
		moduo = pow(pow(Fs.real(), 2) + pow(Fs.imag(), 2), 0.5);
		fprintf(out, "%.5f %.5f\n", i, moduo);
	}
	fclose(out);

}
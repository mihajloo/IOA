#include <stdio.h>
#include <iostream>
#include <list> 
#include <iterator> 

using namespace std;


void main() {

	cout << "IOA 2c" << endl;
	int fact1 = 2;
	int num1 = 7;
	int fact2 = 3;
	int num2 = 3;
	int fact3 = 5;
	int num3 = 7;
	int fact4 = 79;
	int num4 = 2;
	list<int> list;
	int numb = 0;
	for (int i = 0; i < num1; i++) {
		int tmp1 = pow(fact1, i);
		for (int j = 0; j < num2; j++) {
			int tmp2 = pow(fact2, j);
			for (int k = 0; k < num3; k++) {
				int tmp3 = pow(fact3, k);
				for (int l = 0; l < num4; l++) {
					int tmp4 = pow(fact4, l);
					if (tmp4*tmp3*tmp2*tmp1 < 711)
					list.push_back(tmp4*tmp3*tmp2*tmp1);
					numb++;
				}
			}
		}
	}
	cout << list.size() << endl;
	try {
		
		for (std::list<int>::iterator it1 = list.begin(); it1 != list.end(); it1++) {
			for (std::list<int>::iterator it2 = list.begin(); it2 != list.end(); it2++) {
				for (std::list<int>::iterator it3 = list.begin(); it3 != list.end(); it3++) {
					for (std::list<int>::iterator it4 = list.begin(); it4 != list.end(); it4++) {
						//std::list<int>::iterator it = list.begin();
						//advance(it, i);
						int a1 = *it1;
						//advance(it, j);
						int a2 = *it2;
						//advance(it, k);
						int a3 = *it3;
						//advance(it, l);
						int a4 = *it4;
						//cout << "The numbers are: " << (a1 + 0.0) / 100 << " " << (a2 + 0.0) / 100 << " " << (a3 + 0.0) / 100 << " " << (a4 + 0.0) / 100 << endl;
						//cout << l << endl;
						if ((a1 + a2 + a3 + a4) == 711 && a1*a2*a3*a4 == 711000000) {
							cout << "The numbers are: " << (a1 + 0.0) / 100 << " " << (a2 + 0.0) / 100 << " " << (a3 + 0.0) / 100 << " " << (a4 + 0.0) / 100 << endl;
						
							int ax;
							scanf_s("%d", &ax);
						}
					
					}
				}
			}
		}
	}
	catch (std::exception e) {

	}
	cout << numb << endl;
	int x;
	scanf_s("%d", &x);
}
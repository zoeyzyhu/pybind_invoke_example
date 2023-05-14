#include <iostream>
#include "mult.h"

float mult(int int_param, float float_param) {
	float product = int_param*float_param;
	std::cout << "In the C++ function:"
		<< "\n int - " << int_param
		<< "\n float - " << float_param
		<< "\n product - " << product
		<< std::endl;
	return product;
}

int main() {
    int int_param = 2;
    float float_param = 3.14;
    float product = mult(int_param, float_param);
    std::cout << "The product is " << product << std::endl;
    return 0;
}

#include <cmath>
#include <cstdlib>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

# define deltat 0.01
# define deltax 0.01

float dut;
float dux;
float yn[2][0.5];

int main(){

  for (int i = 0; i<=2; i++){
    for (int j = 0; j<=0.5; j++){
      dut = (yn[i][j+1] - yn[i][j])/deltat;
      dux = (yn[i+1][j] - yn[i][j]/deltax)
    }
  }
  return 0;
}
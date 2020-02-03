#include<iostream>
#include<string>
#include<array>
using namespace std;

//TRAINING

/*
A Piece of cardboard 14 inches by 10 inches. We need to cut the corners to fold up and make a box. Determine height of the box to maximize volume.

*/
double V(double h){
  return (140*h - 48*h*h +4*h*h*h);
}
double V_dot(double h){

 return (140 - 96*h +12*h*h);

}
double GradientDes(double initialPoint, double learningRate){
  double h[1000] ={0};
  h[0] = initialPoint;
  for(int i=1 ;i<1000;i++){
  	 h[i] = h[i-1] +learningRate*V_dot(h[i-1]) ;
  	 
     if(h[i]-h[i-1]<0.000001){
       break;
     }
     cout<<h[i]<<endl;
  }
  return 0;

}
int main(){

  GradientDes(0.0,0.01);
	return 0;
}


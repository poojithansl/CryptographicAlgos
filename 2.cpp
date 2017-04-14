#include <bits/stdc++.h>
#include <unistd.h>
#include <stdlib.h>
#include "math.h"
using namespace std;

typedef long long int lli;

int gcd(int p,int q){
	while(p!=q)
    {
        if(p > q)
            p -= q;
        else
            q -= p;
    }
    return p;
}
int eulerphi(int n)
{
	int i,result=1;
	for(i=2;i<n;i++)
		if(gcd(i,n)==1)
			result++;
	return result;

}
int findr(int n){
	int maxk;
	int R;
	maxk = floor(pow((log10(n)/log10(2)),2));
	int r2,maxr;
	r2 = ceil(pow((log10(n)/log10(2)),5));
	maxr = 3;
	if (r2 > maxr){
		maxr = r2;
	}
	int nextr,r,k;
	nextr = 1;
	//printf("%d",maxr);
	for (r= 2;r< maxr;r++){
		if (nextr == 1){
			nextr = 0;
			long long int intpowm;
			intpowm = n;
			for (k=1;k <= maxk;k++){
				if(nextr == 0){
					
					intpowm = (intpowm*n)%r;
					//printf("%lld %d\n",intpowm,r);
					R = r;
					if ((intpowm == 1)||(intpowm == 0)){
						nextr = 1;
					}
					
				}
			}
		}
	}
	return R;
}
int modpower(int b,int p,int m){
	int midv;
	midv = 1;
	while(p--){
		midv = (midv * b)%m;
	}
	return midv;
}
int* multiply(int *A, int *B,int degree1,int degree2,lli mod)
{
	int l = degree1+degree2+1;
	int *prod = new int[l];
	for (int i = 0; i<l; i++)
		prod[i] = 0;
	for (int i=0; i<degree1+1; i++)
	{
		for (int j=0; j<degree2+1; j++)
		{
			prod[i+j] += A[i]*B[j];
			prod[i+j] = prod[i+j]%mod;
		}
	}
	return prod;
}
int *multiplyexponentiation(int *a,int n,int mod)
{
	int *res = new int[1];
	res[0] = 1;	
	int ord = 0;
	int orda = 1;
	while(n>0)
	{
		if (n&1)
		{
			res = multiply(res,a,ord,orda,mod);
			ord = ord + orda;
		}
		n = n>>1;
		a = multiply(a,a,orda,orda,mod);
		orda = orda + orda;
	}
	return res;
	// printPoly(res,ord);
}
int *PolynomialRemainder(int a[],int degree1,int r)
{
	// printPoly(a,degree1);
	// cout<<r<<endl;
	int *remainder1 = new int[r];
	for (int i = degree1; i >=0;i--)
	{
		if(i>=r)
		{
			int val = a[i];
			a[i] = 0;
			a[i-r]+=val;
		}
		else
			break;
	}
	for (int i = 0; i < r; i++)
	{
		remainder1[i]=a[i];
	}
	return remainder1;
}
int *polynomialmod(int a[],int degree,int mod)
{
	for (int i = 0; i <= degree;i++)
	{
		a[i] = a[i]%mod;
	}
	return a;
}
lli c[10000];
void coef(int n)
{
	int i, j;
 
	if (n < 0 || n > 63) abort(); // gracefully deal with range issue
 
	for (c[i=0] = 1; i < n; c[0] = -c[0], i++)
		for (c[1 + (j=i)] = 1; j > 0; j--)
			c[j] = c[j-1] - c[j];
}
void show(int n)
{	coef(n);
	do printf("%+lldx^%d", c[n], n); while (n--);
}
void printPoly(int *poly,int n)
{
	// int n = sizeof(poly)/sizeof(poly[0]);
	// cout<<"n"<<n<<endl;
    for (int i=0; i<=n; i++)
    {
    	cout << poly[i];
    	if (i != 0)
        	cout << "x^" << i ;
    	if (i != n)
       		cout << " + ";
    }
    cout<<"\n"<<endl;
}
int stepfive(int r, int n)
{
		int maxi,a,x1,x2,x3,x4,frac1,frac2;
		double fract;
		maxi=floor(log10(n)/log10(2)*sqrt(eulerphi(r)));
		printf("%d",maxi);
		for (lli a = 1; a <= maxi;a++)
		{
			//cout<<a<<endl;
		int *p = new int[2];
		p[1] = 1;
		p[0] = a;
		int *in = multiplyexponentiation(p,n,n);
		int *x = PolynomialRemainder(in,n,r);
		 x = polynomialmod(x,r-1,n);
		//printPoly(x,r-1);
		 //show(r-1);
		//cout<<x<<endl;
		int *b = new int[n+1];
		for (lli i = 0; i < n+1; i++)
		 	b[i] = 0;
		 b[n] = 1;
		 b[0] = a;
		 int *y = PolynomialRemainder(b,n,r);
		 for (lli i = 1; i <= r; i++)
		 	if (b[i]!=x[i])
		 		{//cout<<"composite"<<endl;
		 		return 0;}
		 if ((b[0]-x[0])%2!=0)
		 	{//cout<<"composite"<<endl;
		 return 0;}
		 return 1;
	}
		
		return 0;
	
}
int main(){
	int r,a,fl,it;
	lli n;
	//n = 31;	
	cout<<"Enter a number:";
	cin>>n;
	
		//printf("%d\n", it);
		r = findr(n);
	//printf("%d\n",r);
	for (a=r; a>1; a--){
		if ((gcd(a,n) > 1)&&(gcd(a,n)<n)){
			cout<<"composite"<<endl;
			fl=1;

			return 0;
		}
	}

	if (n<=r){
		cout<<"prime\n"<<endl;
		return 0;
	}
	if (stepfive(r,n))
		cout<<"prime"<<endl;
	else
		cout<<"composite"<<endl;
	
	return 0;
}

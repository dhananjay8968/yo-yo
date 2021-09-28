#include <bits/stdc++.h>
using namespace std ;

int main(){
	int m,n,ans;
	cin>>m>>n ;
	ans =0 ;
	int x = m/2 ;
	
	ans += x*n ;
	
	int y = n/2 ;
	ans += (m%2)*y ;
	cout<<ans ;



	
	return 0 ;
}
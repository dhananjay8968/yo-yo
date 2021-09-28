#include <bits/stdc++.h>
using namespace std ;

int main(){
	int n,ans ;
	cin>>n ;
	ans = 0 ;

	for (int i = 0; i < n; ++i)
	{
		/* code */
		int a,b,c,x ;
		cin>>a>>b>>c ;
		x =0 ;
		if(a==1){
			x += 1 ;
		}
		if(b==1){
			x += 1 ;
		}
		if(c==1){
			x+= 1;
		}

		if(x>=2){
			ans +=1 ;
			
		}

	}cout<<ans ;

	
	return 0 ;
}
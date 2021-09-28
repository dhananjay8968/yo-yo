#include <bits/stdc++.h>
using namespace std ;

int main(){
	int table[5][5] ;
	int ans ;
	for (int i = 0; i < 5; ++i)
	{
		/* code */for (int j = 0; j < 5; ++j)
		{
			/* code */int a ;
			cin>>a ;
			if(a==1){
				ans = abs(2-i) ;
				ans += abs(2-j) ;
			}
		}
	}
	cout<<ans ;
	
	return 0 ;
}
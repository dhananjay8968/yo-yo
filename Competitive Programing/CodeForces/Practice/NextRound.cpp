#include <bits/stdc++.h>
using namespace std ;

int main(){
	int n,x,ans ;
	cin>>n>>x ;
	int score[n] ;
	
	ans = 0 ;
	for (int i = 0; i < n; ++i)
	{
		/* code */
		int s ;
		cin>>s ;
		score[i] = s ;
	}
	for (int j = 0; j < n ; ++j)
	{
		/* code */
		
		if((score[j] >= score[x-1]) && (score[j] > 0)){
			ans += 1 ;
			
		}
	}
	cout<<ans ;
	
	return 0 ;
}
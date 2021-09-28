#include <bits/stdc++.h>
using namespace std ;

int main(){
	int n ;
	string s ;
	cin>>n>>s ;

	int ans,flag ;
	flag = 0;
	ans = 0 ;

	for(int i = 1 ; i< n ; i++){
		if(s[i] == s[flag]){
			ans += 1 ;
		}else{
			flag = i ;
		}


	}
	cout<<ans<<endl ;
	
	return 0 ;
}
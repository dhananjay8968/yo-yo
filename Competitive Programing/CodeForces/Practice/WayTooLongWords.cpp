
#include <bits/stdc++.h>
using namespace std ;

void abriviation(string t){
	int x = t.size() ;
	if (x<=10)
	{
		/* code */
		cout<<t<<endl ;
	}else{
		cout<<t[0]<<x-2<<t[x-1]<<endl ;


	}
}

int main(){
	int t ;
	cin>>t ;
	for (int i = 0; i < t; ++i)
	{
		/* code */
		string a ;
		cin>> a ;
		abriviation(a) ;

	}
	return 0 ;
}
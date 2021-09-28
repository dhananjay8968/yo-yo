#include <bits/stdc++.h>
using namespace std ;

int main(){
	int n ;
	cin>>n ;
	int ans = 0 ;
	for (int i = 0; i < n; ++i)
	{
		/* code */
		string a ;
		cin>>a ;
		if (a[1] == '+')
		{
			/* code */
			ans += 1 ;

		}else {
			ans -= 1 ;
		}
	}
	cout<< ans ;
	return 0 ;
}
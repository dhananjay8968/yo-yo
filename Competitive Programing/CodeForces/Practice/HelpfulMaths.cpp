#include <bits/stdc++.h>
using namespace std ;

int main(){
	string s ;
	int a,b,c ;
	a =0 , b =0 , c = 0 ;
	cin>>s;

	for(int i = 0 ; i < s.size() ; i++) {
		if(s[i] == '1'){
			a++;
		}else if(s[i] == '2'){
			b++ ;
		}else if (s[i] == '3'){
			c++ ;
		}
	}

	for(int i = 0 ; i<a-1 ; i++){
		cout<<1<<"+" ;
	}if((a>0) && (b>0 || c>0)){
		cout<<1<<"+" ;
	}else if(a> 0){
		cout<<1<<endl ;
	}

	for(int i = 0 ; i<b-1 ; i++){
		cout<<2<<"+" ;
	}if((b>0) && (c>0)){
		cout<<2<<"+" ;
	}else if(b> 0){
		cout<<2<<endl ;
	}

	for(int i = 0 ; i<c-1 ; i++){
		cout<<3<<"+" ;
	}if(c>0){cout<<3<<endl ;}

	return 0 ;
}
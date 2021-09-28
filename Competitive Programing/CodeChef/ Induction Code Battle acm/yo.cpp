#include<bits/stdc++.h>
# define pb push_back 
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;
  
const int maxt = 1e3, maxn = 1e6, maxm = 1e6;
const int maxs = 5e5;
vector<int> v[maxs + 1];
int main()
{   
    for(int i = 1; i <= maxs; i++){
        for(int j = i; j <= maxs; j += i){
            v[j].pb(i);
        }
    }
    int t; cin >> t;
    while(t--){
        int n, m; cin >> n >> m;
        ll ans = 0;
        for(int a = 2; a <= min(n, m); a++){
            int x = a * (m / a);
            int l = 0, r = v[x].size() - 1;
            int add = 0;
            while(l <= r){
                int m = (l + r) >> 1;
                if(v[x][m] < a){
                    add = m + 1;
                    l = m + 1;
                }else{
                    r = m - 1;
                }
            }
            ans += add;
        }
        for(int a = m + 1; a <= n; a++){
            ans += a - 1;
        }
        cout << ans << endl;
    }}
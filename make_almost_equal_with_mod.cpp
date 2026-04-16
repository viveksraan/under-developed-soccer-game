# include<bits/stdc++.h>
using namespace std;
void solve(){
    int n;
    cin >> n;
    vector<long long> v(n);
    for(int i=0; i<n; i++){
        cin >> v[i];
    }
    int i=0;
    while(i<=61){
        int flag = 1;
        for(int j=0; j<n; j++){
            flag &=((v[j]>>i)&(1));
            cout << v[i] << " " << flag << "\n";
        }
        if(flag==0)
            break;
        i++;
    }
    cout << (1LL<<i) << "\n";
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}
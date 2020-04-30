#include<bits/stdc++.h>
using namespace std;

int32_t main(){
    ios::sync_with_stdio(false);
    ifstream fino;
    string s;
    fino.open("followers.txt");
    set<string>followers;
    set<string>connections;
    while(fino){
        getline(fino,s);
        if(s!="")
        followers.insert(s);

    }
    fino.close();
    fino.open("connections.txt");
    while(fino){
        getline(fino,s);
        if(s!="")
        connections.insert(s);
    }
    fino.close();
    cout<<"Number of followers are: "<<followers.size()<<"\n";
    cout<<"Number of connections are: "<<connections.size()<<"\n";
    cout<<"The people who are your connections but do not follow you are:"<<"\n";
    for(auto g:connections){
        if(followers.find(g)==followers.end()){
            cout<<g<<"\n";
        }
    }
    return 0;
}
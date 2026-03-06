#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int>& parser(string str) {
    static vector<int> v = {};
    string acc = string(1,str[1]);
    int k;
    for (int i = 2 ; i < str.length() - 1 ;i++){
        if ( str[i] != ',' ){
            acc = acc + str[i];
            }
        else {
            k = stoi(acc);
            v.push_back(k);
            acc = "";
            }
        }
    k = stoi(acc);
    v.push_back(k);
    return v;
    }

bool linearSearch(string e, vector<int> vec){
    bool res = false;
    int ei = stoi(e);
    for (int i = 0; (i < vec.size()) && (!res); i++){
        if (ei == vec[i]){
            res = true;
        }
    }
    return res;
}

int main()
{
    string vec;
    cin >> vec;
    vector<int> v = parser(vec);
    string target;
    cin >> target;
    cout << linearSearch(target,v);
    return 0;
}
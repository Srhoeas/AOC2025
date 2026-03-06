#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cmath>
using namespace std;

vector<string>& parser(string str) {
    static vector<string> v = {};
    string acc = string(1,str[0]);
    for (double i = 1 ; i < str.length() ;i++){
        if (str[i] == '+' || str[i] == '*'){
            if (acc != ""){
                v.push_back(acc);
                acc = "";
            }
            v.push_back(string(1,str[i]));
        }
        else if ( (str[i] != ' ') && (str[i] != '\n') ){
            acc = acc + str[i];
            }
        else if (acc != ""){
            v.push_back(acc);
            acc = "";
            }
        }
    if (acc != ""){
        v.push_back(acc);
    }
    return v;
    }

double calculapod(vector <string> inpt){
    int cantOp = 1;
    double res;
    int size = inpt.size();
    while ( (inpt[size-cantOp] == "+") || (inpt[size-cantOp] == "*") ){
        cantOp++;
    }
    cantOp--;
    vector<double> vProducts( cantOp,1);
    double i = 0;
    while (inpt[i] != "+" && inpt[i] != "*"){
        double column = fmod(i,cantOp);
        if (inpt[(size - cantOp) + column] == "*"){
            double t = stod(inpt[i]);
            vProducts[column] = vProducts[column] * t;
        }
        else{
            res += stod(inpt[i]);
        }
        i++;
    }
    // tuve que cambiar el tipo de res ( y otras variables) a double xq los numeros eran muy
    // grandes para guardarlos en un int, los resultados cambiaban de signo, estaba perdiendo
    // informacion del numero debido a typecasting de un numero muy grande a algo que era demasiado
    // pequeño (int).

    for (int k = 0; k < cantOp; k++){
        if (inpt[(size - cantOp) + k] == "*"){
            res += vProducts[k];
        }
    }
    return res;
}
int main()
{
    ifstream file("input.txt");
    if (!file.is_open()){
        cout << "no abrió" << endl;
        return 0;
    }
    else{
        string line;
        string inpt = "";
        while (getline(file,line)){
            inpt = inpt + line + "\n";
        }
        vector <string> vInpt = parser(inpt);
        double solution = calculapod(vInpt);
        cout << solution << endl;
        return 0;
    }
}
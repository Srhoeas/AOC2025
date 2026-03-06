#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cmath>
#include <stack>
using namespace std;

vector<string>& parser(string str, int rows, double col) {
    static vector<string> v = {};
    string acc = "";
    for (double actualCol = col - 1; actualCol >= 0 ;actualCol--){
        for (int actualRow = rows - 1; actualRow > 0; actualRow--){
            int lineFee = actualRow -1;
            int h = (actualCol + (col*(actualRow - 1)) + lineFee);
            char k = str[h];
            if (k != ' '){
                acc = k + acc;
            }
        }
        if (acc != ""){
            v.push_back(acc);
            acc = "";
        }
        int lineFee = rows - 1;
        char actualChar = str[(col)*(rows-1) + actualCol + lineFee];
        if (actualChar == '+' || actualChar == '*'){
            v.push_back(string(1,actualChar));
            actualCol--;
        }

    }
    return v;
    }

double calculapod(vector <string> inpt){
    double res;
    int size = inpt.size();
    double i = 0;
    stack<string> pila;
    while (i < size){
        if (inpt[i] != "+" && inpt[i] != "*"){
            pila.push(inpt[i]);
        }
        else{
            double acc = 1;
            while (!(pila.empty())){
                int num = stod(pila.top());
                pila.pop();
                if (inpt[i] == "+"){
                    res += num;
                }
                else{
                    acc = acc*num;
                }
            }
            if (acc != 1){
                res += acc;
                acc = 1;
            }
        }
        i++;
    }
    // tuve que cambiar el tipo de res ( y otras variables) a double xq los numeros eran muy
    // grandes para guardarlos en un int, los resultados cambiaban de signo, estaba perdiendo
    // informacion del numero debido a typecasting de un numero muy grande a algo que era demasiado
    // pequeño (int).

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
        int rows = 0;
        while (getline(file,line)){
            inpt = inpt + line + "\n";
            rows++;
        }
        double col = line.length();
        file.close();
        vector <string> vInpt = parser(inpt,rows,col);
        double solution = calculapod(vInpt);
        cout << solution << endl;
        return 0;
    }
}
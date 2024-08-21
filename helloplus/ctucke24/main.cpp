#include <iostream>
#include <fstream>

using namespace std;


int main () {

    string filename = "/proc/cpuinfo";
    string input;

    ifstream fin;

    fin.open("/proc/cpuinfo");
        if(fin.is_open() == false) {
            cout <<"shit" << endl;

        }

    while (getline(fin, input) ) {
        if (input.substr(0,9) == "cpu cores") {
            cout << input << endl;
            return 0;
        }
    }



    return 0;
}
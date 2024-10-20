#include <iostream>
#include <vector>
#include <algorithm>  
#include <iterator>   

using namespace std;

int main() {
    vector<int> vec = {50,50,25,12,50,24,15,6};  

    cout << "Original vector: ";
    for (int num : vec) 
    {
        cout << num << " ";
    }
    cout << endl;

    reverse(vec.begin(), vec.end());
    cout << "Reversed vector: ";
    for (int num : vec) 
    {
        cout << num << " ";
    }
    cout << endl;

    sort(vec.begin(), vec.end());
    cout << "Sorted vector: ";
    for (int num : vec) 
    {
        cout << num << " ";
    }
    cout << endl;

    auto it = unique(vec.begin(), vec.end());   
    vec.erase(it, vec.end());  

    cout << "Vector after removing duplicates: ";
    for (int num : vec) 
    {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}

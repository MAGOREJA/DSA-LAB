#include <iostream>
#include <vector>
#include <algorithm>  

using namespace std;

int main() {
    vector<int> vec = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};  
    int target;

    cout << "Enter the integer to search for: ";
    cin >> target;

    auto it = find(vec.begin(), vec.end(), target);

    if (it != vec.end()) 
    {
        int index = distance(vec.begin(), it);
        cout << "Integer " << target << " found at index " << index << "." << endl;
    } 
    else
    {
        cout << "Integer " << target << " not found in the vector." << endl;
    }

    return 0;
}

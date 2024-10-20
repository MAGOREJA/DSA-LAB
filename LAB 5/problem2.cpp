#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec;  // Create an empty vector of integers

    for (int i = 0; i < 100; i++) {
        vec.push_back(i);  // Insert integers into the vector

        // Print the size and capacity after each insertion
        cout << "Insertion " << i + 1 << ": Size = " << vec.size() 
             << ", Capacity = " << vec.capacity() << endl;
    }

    return 0;
}

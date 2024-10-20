#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    vector<string> vec;
    string input;
    int choice;

    while (true) {
        cout << "\nChoose an operation:\n";
        cout << "1. Add string\n";
        cout << "2. Remove string\n";
        cout << "3. Display size and capacity\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        
        if (choice == 1) {
            cout << "Enter string to add: ";
            cin.ignore(); // To clear the newline left in the buffer
            getline(cin, input);
            vec.push_back(input);
            cout << "String added.\n";
        } 
        else if (choice == 2) {
            if (!vec.empty()) {
                cout << "Enter the string to remove: ";
                cin.ignore();
                getline(cin, input);

                auto it = find(vec.begin(), vec.end(), input);
                if (it != vec.end()) {
                    vec.erase(it);
                    cout << "String removed.\n";
                } else {
                    cout << "String not found.\n";
                }
            } else {
                cout << "The vector is empty.\n";
            }
        } 
        else if (choice == 3) {
            cout << "Size: " << vec.size() << ", Capacity: " << vec.capacity() << endl;
        } 
        else if (choice == 4) {
            cout << "Exiting program...\n";
            break;
        } 
        else {
            cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}

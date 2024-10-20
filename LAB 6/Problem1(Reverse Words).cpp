#include<iostream>
using namespace std;
#include<string>

struct Node {
    string data;
    Node* next;
};

class Stack {
    private:
        Node* top;
    public:
        Stack() {
            top = nullptr;
        }

        ~Stack() {
            Node* current = top;
            while (current != nullptr) {
                Node* nextNode = current->next;
                delete current;
                current = nextNode;
            }
            top = nullptr;
        }

        void Push(string value) {
            Node* newNode = new Node();
            newNode->data = value;
            newNode->next = top;
            top = newNode;
        }

        string Pop() {
            if (IsEmpty()) {
                return "No elements to pop";
            }
            Node* nextNode = top->next;
            string poppedValue = top->data;
            delete top;
            top = nextNode;
            return poppedValue;
        }

        bool IsEmpty() {
            return top == nullptr;
        }
};

void ReverseWords(string sentence) {
    Stack wordStack;
    string currentWord = "";

    for (int i = 0; i < sentence.length(); i++) {
        if (sentence[i] == ' ') {
            if (!currentWord.empty()) {
                wordStack.Push(currentWord);  
                currentWord = "";             
            }
        } else {
            currentWord += sentence[i];       
        }
    }

    if (!currentWord.empty()) {
        wordStack.Push(currentWord);          
    }

    cout << "Output: ";
    while (!wordStack.IsEmpty()) {
        cout << wordStack.Pop();
        if (!wordStack.IsEmpty()) {
            cout << " ";                      
        }
    }
}

int main() {
    string input = "I am from University of Engineering and Technology Lahore";
    ReverseWords(input);
    return 0;
}

#include<iostream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cctype>
using namespace std;

struct Node {
    int data;
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

        void Push(int value) {
            Node* newNode = new Node();
            newNode->data = value;
            newNode->next = top;
            top = newNode;
        }

        int Pop() {
            Node* nextNode = top->next;
            int poppedValue = top->data;
            delete top;
            top = nextNode;
            return poppedValue;
        }

        int Peek() {
            return top->data;
        }

        bool IsEmpty() {
            return top == nullptr;
        }

        bool CanPerformBinaryOperation() {
            return (top != nullptr && top->next != nullptr);
        }

        void DisplayStack() {
            cout << "Stack: ";
            Node* current = top;
            while (current != nullptr) {
                cout << current->data << " ";
                current = current->next;
            }
            cout << "\n";
        }
};

bool EvaluatePostfix(Stack& stack, string expression) {
    istringstream inputStream(expression);
    string token;

    while (inputStream >> token) {
        if (isdigit(token[0]) || (token[0] == '-' && token.length() > 1)) {
            stack.Push(stoi(token));
        } 
        else {
            if ((token == "+" || token == "-" || token == "*" || token == "/" || token == "%") && stack.CanPerformBinaryOperation()) {
                int operand2 = stack.Pop();
                int operand1 = stack.Pop();
                int result;
                if (token == "+") {
                    result = operand1 + operand2;
                } 
                else if (token == "-") {
                    result = operand1 - operand2;
                } 
                else if (token == "*") {
                    result = operand1 * operand2;
                } 
                else if (token == "/") {
                    if (operand2 != 0) {
                        result = operand1 / operand2;
                    }
                } 
                else if (token == "%") {
                    if (operand2 != 0) {
                        result = operand1 % operand2;
                    }
                }
                stack.Push(result);
            } 
            else if (token == "?") {
                stack.DisplayStack();
            } 
            else if (token == "^" && (!stack.IsEmpty())) {
                cout << stack.Pop() << endl;
            } 
            else if (token == "!") {
                return false;
            }  
        }
    }
    return true;
}

int main() {
    Stack stack;
    cout << "Enter a post-fix expression, or type '!' to exit:" << endl;
    while (true) {
        string inputExpression;
        cout << ">>";
        getline(cin, inputExpression);
        if (!EvaluatePostfix(stack, inputExpression)) {
            break;
        }
    }
    return 0;
}

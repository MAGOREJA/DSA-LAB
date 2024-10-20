#include<iostream>
using namespace std;
struct Node {
    int value;
    Node * next;
};

class LinkedList {
    private:
        Node * start;
    public:
        LinkedList() {
            start = nullptr;
        }
        ~LinkedList() {
            Node * current = start;
            while (current != nullptr) {
                Node * temp = current->next;
                delete current;
                current = temp;
            }
            start = nullptr;
        }
        Node * getStart() {
            return start;
        }
        bool isEmpty() {
            return start == nullptr;
        }
        Node* insertAtPosition(int pos, int val) {           
            if (pos < 0) return nullptr;
            Node* newNode = new Node();
            newNode->value = val;
            if (pos == 0) {
                newNode->next = start;
                start = newNode;
            } else {
                Node * currentNode = start;
                for (int i = 0; i < pos - 1 && currentNode != nullptr; i++) {
                    currentNode = currentNode->next;
                }
                if (currentNode == nullptr) return nullptr;
                newNode->next = currentNode->next;
                currentNode->next = newNode;
            }
            return start;
        }
        Node* insertAtStart(int val) {
            Node * newNode = new Node();
            newNode->value = val;
            newNode->next = start;
            start = newNode;
            return start;
        }
        Node* insertAtEnd(int val) {
            Node * newNode = new Node();
            newNode->value = val;
            newNode->next = nullptr;
            if (start == nullptr) {
                start = newNode;
            } else {
                Node * last = start;
                while (last->next != nullptr) {
                    last = last->next;
                }
                last->next = newNode;
            }
            return start;
        }
        bool searchNode(int val) {
            Node * current = start;
            while (current != nullptr) {
                if (current->value == val) return true;
                current = current->next;
            }
            return false;
        }
        bool removeNode(int val) {
            if (searchNode(val)) {
                while (start != nullptr && start->value == val) {
                    Node* temp = start->next;
                    delete start;
                    start = temp;
                }
                if (start == nullptr) return true;
                Node * currentNode = start;
                while (currentNode->next != nullptr) {
                    if (currentNode->next->value == val) {
                        Node * toDelete = currentNode->next;
                        currentNode->next = toDelete->next;
                        delete toDelete;
                    } else {
                        currentNode = currentNode->next;
                    }
                }
                return true;
            }
            return false;
        }
        bool removeFromStart() {
            if (start == nullptr) return false;
            Node * temp = start->next;
            delete start;
            start = temp;
            return true;
        }
        bool removeFromEnd() {
            if (start == nullptr) return false;
            if (start->next == nullptr) {
                delete start;
                start = nullptr;
            } else {
                Node * currentNode = start;
                while (currentNode->next->next != nullptr) {
                    currentNode = currentNode->next;
                }
                delete currentNode->next;
                currentNode->next = nullptr;
            }
            return true;
        }
        void displayList() {
            Node * currentNode = start;
            cout << "Linked List: ";
            while (currentNode != nullptr) {
                cout << currentNode->value << "--->";
                currentNode = currentNode->next;
            }
            cout << "Null" << endl;
        }
        Node* reverseList() {
            Node * previous = nullptr;
            Node * temp = nullptr;
            Node * current = start;
            while (current != nullptr) {
                temp = current->next;
                current->next = previous;
                previous = current;
                current = temp;
            }
            start = previous;
            return start;
        }
        Node* sortList(Node *list) {
            for (Node * i = list; i != nullptr; i = i->next) {
                Node * minNode = i;
                for (Node * j = i->next; j != nullptr; j = j->next) {
                    if (j->value < minNode->value) {
                        minNode = j;
                    }
                }
                swap(i->value, minNode->value);
            }
            return list;
        }
        Node* removeDuplicates(Node *list) {
            Node * current = list;
            while (current != nullptr && current->next != nullptr) {
                Node * remaining = current;
                while (remaining->next != nullptr) {
                    if (current->value == remaining->next->value) {
                        Node * toRemove = remaining->next;
                        remaining->next = toRemove->next;
                        delete toRemove;
                    } else {
                        remaining = remaining->next;
                    }
                }
                current = current->next;
            }
            return list;
        }
        Node* mergeLists(Node* list1, Node* list2) {
            if (!list1) return list2;
            if (!list2) return list1;

            if (list1->value < list2->value) {
                list1->next = mergeLists(list1->next, list2);
                return list1;
            } else {
                list2->next = mergeLists(list1, list2->next);
                return list2;
            }
        }
        Node* intersectLists(Node *list1, Node *list2) {
            LinkedList result;
            while (list1 != nullptr) {
                Node * current = list2;
                while (current != nullptr) {
                    if (list1->value == current->value && !result.searchNode(list1->value)) {
                        result.insertAtEnd(list1->value);
                    }
                    current = current->next;
                }
                list1 = list1->next;
            }
            result.displayList();
            return result.getStart();
        }
};

int main() {
    LinkedList list;
    LinkedList list2;
    list.insertAtEnd(10);
    list.insertAtEnd(30);
    list.insertAtEnd(20);
    list.insertAtStart(30);
    list.insertAtStart(5);
    list.insertAtEnd(30);
    list.insertAtEnd(30);
    list.insertAtPosition(3,3);
    list.displayList();
    list.removeFromStart();
    list.displayList();
    list.removeFromEnd();
    list.displayList();
    list.removeNode(30);
    list.displayList();
    cout << list.searchNode(20) << endl;
    cout << list.searchNode(2) << endl;
    list2.insertAtEnd(3);
    list2.insertAtEnd(5);
    list2.insertAtEnd(7);
    list2.insertAtEnd(3);
    list2.insertAtEnd(7);
    list2.insertAtEnd(7);
    list2.displayList();
    list2.reverseList();
    list2.displayList();
    Node * first = list2.getStart();
    list2.sortList(first);
    list2.displayList();
    list2.removeDuplicates(first);
    list2.displayList();
    
    Node * mergedList = list.mergeLists(list.getStart(), list2.getStart());
    while (mergedList != nullptr) {
        cout << mergedList->value << " ";
        mergedList = mergedList->next;
    }
}

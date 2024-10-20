#include<iostream>
using namespace std;

struct Node {
    int value;
    Node* prev;
    Node* next;
};

class DoubleLinkedList {
    private:
        Node* head;
    public:
        DoubleLinkedList() {
            head = nullptr;
        }

        ~DoubleLinkedList() {
            Node* currentNode = head;
            while(currentNode != nullptr) {
                Node* nextNode = currentNode->next;
                delete currentNode;
                currentNode = nextNode;
            }
            head = nullptr;
        }

        Node* getHead() {
            return head;
        }

        bool isEmpty() {
            return head == nullptr;
        }

        Node* insertNode(int index, int value) {
            if(index < 0) {
                return nullptr;
            }
            Node* newNode = new Node();
            newNode->value = value;

            if(index == 0) {
                newNode->prev = nullptr;
                newNode->next = head;
                head = newNode;
            } else {
                Node* currentNode = head;
                for(int i = 0; i < index - 1 && currentNode != nullptr; i++) {
                    currentNode = currentNode->next;
                }
                if(currentNode == nullptr)
                    return nullptr;

                newNode->prev = currentNode;
                newNode->next = currentNode->next;
                currentNode->next = newNode;
            }
            return head;
        }

        Node* insertAtHead(int value) {
            Node* newNode = new Node();
            newNode->value = value;
            newNode->prev = nullptr;
            newNode->next = head;
            head = newNode;
            return head;
        }

        Node* insertAtEnd(int value) {
            Node* newNode = new Node();
            newNode->value = value;

            if(head == nullptr) {
                newNode->prev = nullptr;
                newNode->next = head;
                head = newNode;
            } else {
                Node* lastNode = head;
                while(lastNode->next != nullptr) {
                    lastNode = lastNode->next;
                }
                newNode->prev = lastNode;
                lastNode->next = newNode;
                newNode->next = nullptr;
            }
            return head;
        }

        bool findNode(int value) {
            Node* currentNode = head;
            while(currentNode != nullptr) {
                if(currentNode->value == value) {
                    return true;
                }
                currentNode = currentNode->next;
            }
            return false;
        }

        bool deleteNode(int value) {
            while (head != nullptr && head->value == value) {
                Node* nextNode = head->next;
                delete head;
                if (nextNode != nullptr) {
                    nextNode->prev = nullptr;
                }
                head = nextNode;
            }

            if (head == nullptr) {
                return true;
            }

            Node* currentNode = head;
            while (currentNode != nullptr && currentNode->next != nullptr) {
                if (currentNode->next->value == value) {
                    Node* nodeToRemove = currentNode->next;
                    currentNode->next = nodeToRemove->next;
                    if (nodeToRemove->next != nullptr) {
                        nodeToRemove->next->prev = currentNode;
                    }
                    delete nodeToRemove;
                } else {
                    currentNode = currentNode->next;
                }
            }
            return true;
        }

        bool deleteFromStart() {
            if(head == nullptr) {
                return false;
            }
            Node* nextNode = head->next;
            if (nextNode != nullptr) {
                nextNode->prev = nullptr;
            }
            delete head;
            head = nextNode;
            return true;
        }

        bool deleteFromEnd() {
            if(head == nullptr) {
                return false;
            } else if(head->next == nullptr) {
                delete head;
                head = nullptr;
                return true;
            }

            Node* lastNode = head;
            while(lastNode->next != nullptr) {
                lastNode = lastNode->next;
            }
            lastNode->prev->next = nullptr;
            delete lastNode;
            return true;
        }

        void displayList() {
            Node* currentNode = head;
            cout << "Linked List: ";
            while(currentNode != nullptr) {
                cout << currentNode->value << "--->";
                currentNode = currentNode->next;
            }
            cout << "Null" << endl;
        }

        Node* reverseList() {
            Node* currentNode = head;
            while(currentNode->next != nullptr) {
                currentNode = currentNode->next;
            }
            head = currentNode;

            while(currentNode != nullptr) {
                Node* nextNode = currentNode->prev;
                currentNode->prev = currentNode->next;
                currentNode->next = nextNode;
                currentNode = currentNode->next;
            }
            return head;
        }

        Node* sortList(Node* listHead) {
            for(Node* i = listHead; i->next != nullptr; i = i->next) {
                Node* minNode = i;
                for(Node* j = i->next; j != nullptr; j = j->next) {
                    if(j->value < minNode->value) {
                        minNode = j;
                    }
                }
                swap(i->value, minNode->value);
            }
            return listHead;
        }

        Node* removeDuplicates(Node* listHead) {
            Node* currentNode = listHead;
            while(currentNode != nullptr && currentNode->next != nullptr) {
                Node* nextNode = currentNode;
                while(nextNode->next != nullptr) {
                    if(currentNode->value == nextNode->next->value) {
                        Node* nodeToRemove = nextNode->next;
                        nextNode->next = nodeToRemove->next;
                        if(nodeToRemove->next != nullptr) {
                            nodeToRemove->next->prev = nextNode;
                        }
                        delete nodeToRemove;
                    } else {
                        nextNode = nextNode->next;
                    }
                }
                currentNode = currentNode->next;
            }
            return listHead;
        }

        Node* mergeLists(Node* list1Head, Node* list2Head) {
            if (!list1Head) return list2Head;
            if (!list2Head) return list1Head;

            if (list1Head->value < list2Head->value) {
                list1Head->next = mergeLists(list1Head->next, list2Head);
                if (list1Head->next != nullptr) {
                    list1Head->next->prev = list1Head;
                }
                return list1Head;
            } else {
                list2Head->next = mergeLists(list1Head, list2Head->next);
                if (list2Head->next != nullptr) {
                    list2Head->next->prev = list2Head;
                }
                return list2Head;
            }
        }

        Node* intersectLists(Node* list1Head, Node* list2Head) {
            DoubleLinkedList intersectionList;
            Node* list1Current = list1Head;
            Node* list2Current;

            while(list1Current != nullptr) {
                list2Current = list2Head;
                while(list2Current != nullptr) {
                    if(list1Current->value == list2Current->value) {
                        if(!intersectionList.findNode(list1Current->value)) {
                            intersectionList.insertAtEnd(list1Current->value);
                        }
                    }
                    list2Current = list2Current->next;
                }
                list1Current = list1Current->next;
            }
            intersectionList.displayList();
            return intersectionList.getHead();
        }
};

int main() {
    DoubleLinkedList list1;
    DoubleLinkedList list2;

    list1.insertAtEnd(10);
    list1.insertAtEnd(30);
    list1.insertAtEnd(20);
    list1.insertAtHead(30);
    list1.insertAtHead(5);
    list1.insertAtEnd(30);
    list1.insertAtEnd(30);
    list1.insertNode(3, 3);
    list1.displayList();

    list1.deleteFromStart();
    list1.displayList();
    
    list1.deleteFromEnd();
    list1.displayList();

    list1.deleteNode(30);
    list1.displayList();

    cout << list1.findNode(20) << endl;
    cout << list1.findNode(2) << endl;

    list2.insertAtEnd(3);
    list2.insertAtEnd(5);
    list2.insertAtEnd(7);
    list2.insertAtEnd(3);
    list2.insertAtEnd(7);
    list2.insertAtEnd(7);
    list2.displayList();

    Node* list2Head = list2.getHead();
    list2.sortList(list2Head);
    list2.displayList();

    list2.removeDuplicates(list2Head);
    list2.displayList();

    list2.reverseList();
    list2.displayList();

    Node* mergedListHead = list1.mergeLists(list1.getHead(), list2.getHead());
    while(mergedListHead != nullptr) {
        cout << mergedListHead->value << " ";
        mergedListHead = mergedListHead->next;
    }
}

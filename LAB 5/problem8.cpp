#include <iostream>

using namespace std;

class ArrayList {
private:
    int* data;
    int size;
    int capacity;

public:
    ArrayList();
    ~ArrayList();
    void PushBack(int value);
    int operator[](int index) const;
    int& operator[](int index);
    friend ostream& operator<<(ostream& out, const ArrayList& list);
};

int main() {
    ArrayList arr;

    arr.PushBack(10);
    arr.PushBack(20);
    arr.PushBack(30);

    cout << "ArrayList elements: " << arr << endl;
    cout << "Element at index 1: " << arr[1] << endl;

    return 0;
}

ArrayList::ArrayList() {
    size = 0;
    capacity = 2;
    data = new int[capacity];
}

ArrayList::~ArrayList() {
    delete[] data;
}

void ArrayList::PushBack(int value) {
    if (size == capacity) {
        capacity = static_cast<int>(capacity * 1.5);
        int* newData = new int[capacity];
        for (int i = 0; i < size; ++i) {
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
    }
    data[size++] = value;
}

int ArrayList::operator[](int index) const {
    return data[index];
}

int& ArrayList::operator[](int index) {
    return data[index];
}

ostream& operator<<(ostream& out, const ArrayList& list) {
    for (int i = 0; i < list.size; ++i) {
        out << list.data[i] << " ";
    }
    return out;
}

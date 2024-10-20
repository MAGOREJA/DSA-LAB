#include <iostream>

using namespace std;

class Vector {
private:
    int* data;
    int size;
    int capacity;

public:
    Vector();
    ~Vector();
    void PushBack(int value);
    int& operator[](int index);
    friend ostream& operator<<(ostream& out, const Vector& vec);
};

int main() {
    Vector vec;

    vec.PushBack(10);
    vec.PushBack(20);
    vec.PushBack(30);

    cout << "Vector elements: " << vec << endl;
    cout << "Element at index 1: " << vec[1] << endl;

    return 0;
}

Vector::Vector() {
    size = 0;
    capacity = 1;
    data = new int[capacity];
}

Vector::~Vector() {
    delete[] data;
}

void Vector::PushBack(int value) {
    if (size == capacity) {
        capacity *= 2;
        int* newData = new int[capacity];
        for (int i = 0; i < size; ++i) {
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
    }
    data[size++] = value;
}

int& Vector::operator[](int index) {
    return data[index];
}

ostream& operator<<(ostream& out, const Vector& vec) {
    for (int i = 0; i < vec.size; ++i) {
        out << vec.data[i] << " ";
    }
    return out;
}

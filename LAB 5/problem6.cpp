#include <iostream>
#include <stdexcept> 
using namespace std;

template <typename T>
class AutoGrowingArray
{
private:
    T* arr;        
    int size;       
    int capacity;  

    void grow() 
    {
        capacity += 1; 
        T* newArr = new T[capacity]; 

        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        delete[] arr; 
        arr = newArr; 
    }

public:
    AutoGrowingArray() : size(0), capacity(1) 
    {
        arr = new T[capacity];  // Initialize with capacity of 1
    }

    ~AutoGrowingArray() 
    {
        delete[] arr;
    }

    void PushBack(T value) {
        if (size == capacity) 
        {
            grow(); 
        }
        arr[size] = value;
        size++;
    }

    T operator[](int index) const 
    {
        if (index < 0 || index >= size) 
        {
            throw out_of_range("Index out of range");
        }
        return arr[index];
    }

    T& operator[](int index) {
        if (index < 0 || index >= size) {
            throw out_of_range("Index out of range");
        }
        return arr[index];
    }

    friend ostream& operator<<(ostream& out, const AutoGrowingArray& other) {
        for (int i = 0; i < other.size; i++) {
            out << other.arr[i] << " ";
        }
        return out;
    }

    int getSize() const {
        return size;
    }

    int getCapacity() const {
        return capacity;
    }
};

int main() {
    AutoGrowingArray<int> autoArr;

    // Inserting values into the AutoGrowingArray
    autoArr.PushBack(10);
    autoArr.PushBack(20);
    autoArr.PushBack(30);

    // Display the elements using overloaded << operator
    cout << "AutoGrowingArray elements: " << autoArr << endl;

    // Accessing elements using [] operator
    cout << "Element at index 1: " << autoArr[1] << endl;

    // Modifying an element
    autoArr[1] = 50;
    cout << "Modified AutoGrowingArray: " << autoArr << endl;

    // Check size and capacity
    cout << "Size: " << autoArr.getSize() << ", Capacity: " << autoArr.getCapacity() << endl;

    return 0;
}

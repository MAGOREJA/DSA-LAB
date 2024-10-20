#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> transposeMatrix(const vector<vector<int>>& matrix);
void displayMatrix(const vector<vector<int>>& matrix);
void addColumn(vector<vector<int>>& matrix, const vector<int>& newColumn);
void addRow(vector<vector<int>>& matrix, const vector<int>& newRow);

int main() 
{
    // 2D vector (matrix)
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    cout << "Initial matrix:" << endl;
    displayMatrix(matrix);

    // Adding a new row
    vector<int> newRow = {10, 11, 12};
    addRow(matrix, newRow);
    cout << "\nMatrix after adding a new row:" << endl;
    displayMatrix(matrix);

    // Adding a new column
    vector<int> newColumn = {13, 14, 15, 16}; // Size must match the number of rows
    addColumn(matrix, newColumn);
    cout << "\nMatrix after adding a new column:" << endl;
    displayMatrix(matrix);

    // Transpose of the matrix
    vector<vector<int>> transposedMatrix = transposeMatrix(matrix);
    cout << "\nTransposed matrix:" << endl;
    displayMatrix(transposedMatrix);

    return 0;
}

void displayMatrix(const vector<vector<int>>& matrix) 
{
    for (const auto& row : matrix) {
        for (int element : row) {
            cout << element << " ";
        }
        cout << endl;
    }
}

void addRow(vector<vector<int>>& matrix, const vector<int>& newRow) 
{
    if (!matrix.empty() && newRow.size() != matrix[0].size()) {
        cout << "New row must have " << matrix[0].size() << " elements." << endl;
        return;
    }
    matrix.push_back(newRow);
}

void addColumn(vector<vector<int>>& matrix, const vector<int>& newColumn) 
{
    if (newColumn.size() != matrix.size()) {
        cout << "New column must have " << matrix.size() << " elements." << endl;
        return;
    }
    for (size_t i = 0; i < matrix.size(); ++i) {
        matrix[i].push_back(newColumn[i]);
    }
}

vector<vector<int>> transposeMatrix(const vector<vector<int>>& matrix) 
{
    if (matrix.empty()) return {};
    
    size_t rows = matrix.size();
    size_t cols = matrix[0].size();
    vector<vector<int>> transposed(cols, vector<int>(rows));

    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            transposed[j][i] = matrix[i][j];
        }
    }
    return transposed;
}

//Question link:- https://practice.geeksforgeeks.org/problems/reversal-algorithm5340/1

// Given an array of size N. The task is to rotate array by D elements where D ≤ N.

// Your Task:
// You don't need to read input or print anything.
// Your task is to complete the function leftRotate()
// which takes the array of integers arr[],
// its size n and d as input parameters and rotates arr[]
// in-place without using any extra memory.

// Example 1:

// Input:
// N = 7
// Arr[] = {1, 2, 3, 4, 5, 6, 7}
// D = 2
// Output: 3 4 5 6 7 1 2
// Explanation:
// Rotate by 1: [2, 3, 4, 5, 6, 7, 1]
// Rotate by 2: [3, 4, 5, 6, 7, 1, 2]

// Example 2:

// Input:
// N = 4
// Arr[] = {1, 3, 4, 2}
// D = 3
// Output: 2 4 3 1

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void leftRotate(int arr[], int n, int d)
    {

        if (d == 0)
            return;

        reverceArray(arr, 0, d - 1);
        reverceArray(arr, d, n - 1);
        reverceArray(arr, 0, n - 1);
    }
    void reverceArray(int a[], int start, int end)
    {
        int temp;
        while (start < end)
        {
            temp = a[start];
            a[start] = a[end];
            a[end] = temp;
            start++;
            end--;
        }
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, d;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        cin >> d;
        Solution ob;
        ob.leftRotate(arr, n, d);
        for (int i = 0; i < n; i++)
        {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}

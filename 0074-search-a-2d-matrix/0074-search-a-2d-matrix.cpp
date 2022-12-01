#include<bits/stdc++.h>
using namespace std;



class Solution {
public:

    bool search(vector<int> arr, int f){
        int l = 0;
        int r = arr.size();
        while(l<=r){
            int m = l + (r-l)/2;
            if(f == arr[m]) return true;
            else if(f < arr[m]) r = m - 1;
            else l = m + 1;
        }
            
        return false;
    }



    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(int i=0;i<matrix.size();i++){
            if(target > matrix[i][matrix[i].size()-1]) continue;
            else if(target == matrix[i][matrix[i].size()-1]) return true;
            if(search(matrix[i],target)) return true;
        }
        return false;
    }
};
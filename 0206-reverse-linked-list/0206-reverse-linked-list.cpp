#include<bits/stdc++.h>
using namespace std;




//   struct ListNode {
//       int val;
//       ListNode *next;
//       ListNode() : val(0), next(nullptr) {}
//       ListNode(int x) : val(x), next(nullptr) {}
//       ListNode(int x, ListNode *next) : val(x), next(next) {}
//   };

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode * temp = NULL;
        ListNode * temp2 = head;
        ListNode * temp3 = NULL;
        while(temp2!=NULL){
            temp3 = temp2->next;
            temp2->next = temp;
            temp = temp2;
            temp2 = temp3;
        }
        return temp;
    }
};
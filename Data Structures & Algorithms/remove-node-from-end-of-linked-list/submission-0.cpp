/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* curr = head;
        int count = 0;
        while(curr != nullptr){
            count += 1;
            curr = curr->next;
        }
        curr = head;
        int newCount = 0;
        while(curr != nullptr){
            if(count - n == 0){
                return curr->next;
            }
            if((count - n - 1) == newCount){
                curr->next = curr->next->next;
            }
            curr = curr->next;
            newCount += 1;
        }
        return head;
    }
};

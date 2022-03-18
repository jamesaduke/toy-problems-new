//

const mergeTwoSortedLists = (l1, l2) => {

    // we create a dummy node to hold our new list
    const dummy = new ListNode(-1);
    // we create a pointer to the new list
    let current = dummy;

    while(l1 != null && l2 != null){
        // if the first node in l1 is less than the first node in l2
        if(l1.val < l2.val){
            // we add the first node in l1 to the new list
            currnet.next = l1;
            // current = l1;
            // we move l1 to the next node
            l1 = l1.next;
        }else{
            // if the first node in l2 is greater than the first node in l1
            // we add the first node in l2 to the new list
            current.next = l2;
            // current = l2;
            // we move l2 to the next node
            l2 = l2.next;
        }
    }
    // we add the remaining nodes in l2 to the new list
    if(!l1) current.next = l2;
    // we add the remaining nodes in l1 to the new list
    if(!l2) current.next = l1;

    return dummy.next;
}

console.log(mergeTwoSortedLists([1,2,4],[1,3,4]));

/**
 * Tags: Linked List, Merge Sort
 */

// NOTE: This will not run on node
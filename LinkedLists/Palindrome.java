def palindrome(Node head){}
    if head == null{}
        return true
      }
    Node reversed = reverse(head);
    while(head.next != null){
      if head.data != reversed.data{
        return false;
      }
      head = head.next;
      reversed = reversed.next;
    }


reverse(Node head){
    if head.next == null{
          return head;
      }
      Node prev = null;
      Node current = head;
      Node next = null;
      while(current != null){
          next = current.next;
          current.next = prev;
          prev = current;
          current = next;
    }
    return prev;

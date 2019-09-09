#reverse order

def sum(head_1, head_2, carry):
    if head_1 != None and head_2 != None:
        if head_1.data + head_2.data > 9
            sum(head1.next, head_2.next, 1)
        else:
            sum(head1.next, head_2.next, 0)
        head_1.data = head_1.data + head_2.data
    if head_1 != None:
        if head_1 == 9 and carry == 1:
            sum(head_1.next, head_2, 1)
        else:
            sum(head_1.next, head_2,0)
    if head_2 != None:
        if head_2 == 9 and carry == 1:
            sum(head_1.next, head_2, 1)
        else:
            sum(head_1.next, head_2,0)
        head_1 = head_2
    else:
        return None;

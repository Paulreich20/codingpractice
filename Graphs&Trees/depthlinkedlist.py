DepthLinkedLists(head, depth, list)
    if depth >= list.length():
        list.append(new Node(head.data))
    else:
        n = list[depth]
        while(n.next != null):
            n = n.next
        n.next = new Node(head.data)
    if(n.right and n.left == None):
        return list;
list = []
DepthLinkedLists(root, 0):

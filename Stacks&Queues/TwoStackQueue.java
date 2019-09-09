public class myQueue<T> {
    private myStack<T> stack1;
    private myStack<T> stack2;

    public enqueue(T item){
        if(!stack2.isEmpty()){
          stack2.popAll(stack1)
        }
        stack1.push(item);
        stack1.popAll(stack2);
    }

    public T dequeue(){
        return stack2.pop();
    }

    public T peek(){
        return stack2.peek();
    }

    public boolean T isEmpty(){
        return stack2.isEmpty();
    }



}

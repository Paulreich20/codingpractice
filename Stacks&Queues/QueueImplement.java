public class MyQueue<T>{
    private static class QueueNode<T>{
        private T data;
        private QueueNode<T> next;

        public static QueueNode(T data){
            this.data = data
        }
        private QueueNode<T> first;
        private QueueNode<T> last;


    }
    public enqueue(T item{
      QueueNode t= new QueueNode<T>(item)
      if(last != null){
        last.next = t ;
      }
      last = t;
      if (first == null){
        first = t;
      }
    }
    public T remove(){
      if (last == null) {throw new QueuePointerException}
      T item = first.data;
      first = first.next;
      return item;

    }

    p
}

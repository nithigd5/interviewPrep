import java.util.*;

class MinStack {
    
    Stack<Integer> stack;
    int min;
    public MinStack() {
        stack  = new Stack<>();
        min = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        if(val<=min){
            min = val;
            stack.push(val);
        }else{
            
        }
    }
    
    public void pop() {
        
    }
    
    public int top() {
        
    }
    
    public int getMin() {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
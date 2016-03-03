import java.util.*;
import java.io.*;
import java.awt.*;

public class Problem87 {

   public static void main(String[] args) {
      System.out.print(System.getProperty("java.version"));
   }   
   
}   

class BinaryIntTree implements Iterable<Integer>{
   public TreeNode overallRoot;
   
   public BinaryIntTree(TreeNode node) {
      overallRoot = node == null ? null : node.deepCopy();
   }      
   
   public BinaryIntTree(int... elements) {
      if (elements.length == 0)
         overallRoot = null;
      for (int i : elements)
         insert(i);   
   }              
   
   public BinaryIntTree getCopy() {
      return new BinaryIntTree(overallRoot);
   }         
   
   public TreeNode getRoot() {
      return overallRoot.deepCopy();
   }   
   
   public void insert(int val) {
      if (overallRoot == null) {
         overallRoot = new TreeNode(val);
         return;
      }   
      insert(val, overallRoot);
   }
   
   private void insert(int value, TreeNode node) {
      if (value < node.data) {
         if (node.left != null)
            insert(value, node.left);
         else
            node.left = new TreeNode(value, node);
      }
      else if (value > node.data) {
         if (node.right != null) 
            insert(value, node.right);
         else 
            node.right = new TreeNode(value, node);
      }
   }
   
   public void remove(int val) {
      if (overallRoot == null)
         return;
      remove(val, overallRoot);
   }
   
   private void remove(int val, TreeNode node) {
      if (node == null)
         return;
      if (val > node.data)
         remove(val, node.right);
      else if (val < node.data)
         remove(val, node.left);
      else {
      }}
   
   public void printInorder() {
      printInorder(overallRoot);
      System.out.println();
   }
   
   private void printInorder(TreeNode node) {
      if (node != null) {
         printInorder(node.left);
         System.out.print(node.data+" ");
         printInorder(node.right);
      }   

   }
   
   public void printPreorder() {
      printPreorder(overallRoot);
      System.out.println();
   }
   
   private void printPreorder(TreeNode node) {
      if (node != null) {
         System.out.print(node.data+" ");
         printInorder(node.left);
         printInorder(node.right);
      }
   }
   
   public void printPostorder() {
      printPostorder(overallRoot);
      System.out.println();
   }
   
   private void printPostorder(TreeNode node) {
      if (node != null) {
         printInorder(node.left);
         printInorder(node.right);
         System.out.print(node.data+" ");
      }      
   }
   
   public int highestNumber() {
      if (overallRoot == null)
         throw new NullPointerException();
      return highestNumber(overallRoot);
   }
   
   private int highestNumber(TreeNode node) {
      if (node.right == null) {
         return node.data;
      }
      return highestNumber(node.right);
   }
   
   public int lowestNumber() {
      if (overallRoot == null)
         throw new NullPointerException();
      return lowestNumber(overallRoot);
   }
   
   private int lowestNumber(TreeNode node) {
      return node.left == null ? node.data : lowestNumber(node.left);
   }
   
   private TreeNode lowestNode(TreeNode node) {
      return (node == null) ? null : ((node.left == null) ? node : lowestNode(node.left));
   }   
   
   private TreeNode highestNode(TreeNode node) {
      return (node == null) ? null : ((node.right == null) ? node : highestNode(node.right));
   }  
   
   public void printFullTree() {
      printFullTree(overallRoot, 0);
      System.out.println();
   }
   
   private void printFullTree(TreeNode node, int level) {
      if (node == null) {
         return;
      }
      if (node.right != null) {
         printFullTree(node.right, level+1);
      }
      else {
         System.out.println();
      }
      for (int i = 0; i < level; i++) {
         System.out.print("    ");
      }
      System.out.println(node.data);
      if (node.left != null) {
         printFullTree(node.left, level+1);
      }
      else {
         System.out.println();
      }
   } 
   
   public int getSize() {
      return getSize(overallRoot);
   }
   
   private int getSize(TreeNode node) {
      if (node == null)
         return 0;
      return 1 + getSize(node.left) + getSize(node.right);
   }
   
   public boolean equals(Object other) {
      if (!(other instanceof BinaryIntTree))
         return false;
      BinaryIntTree otherTree = (BinaryIntTree) other;
      return this.overallRoot.equals(otherTree.getRoot());
   }   
   
   public int count(int value) {
      return count(value, overallRoot);
   }
   
   private int count(int value, TreeNode node) {
      if (node == null)
         return 0;
      if (node.data == value)
         return 1 + count(value, node.left) + count(value, node.right);
      return count(value, node.left) + count(value, node.right);
   }
   
   public int sum() {
      return sum(overallRoot);
   }
   
   private int sum(TreeNode node) {
      return (node != null) ? node.data + sum(node.left) + sum(node.right) : 0;
   }   
   
   public boolean contains(int value) {
      return contains(value, overallRoot);
   }
   
   private boolean contains(int value, TreeNode node) {
      return (node == null) ? false : (node.data == value || contains(value, node.left) || contains(value, node.right));
   }   
   
   public static int children(TreeNode node) {
      if (node == null || node.left == null && node.right == null)
         return 0;
      if (node.left == null ^ node.right == null)
         return 1;
      if (node.left != null && node.right != null)
         return 2;
      return 0;   
   }            
   
   public int[] toArray() {
      int[] arr = new int[this.getSize()];
      toArray(arr, overallRoot, 0);
      return arr;
   }
      
   private int toArray(int[] arr, TreeNode node, int index) {
      if (index >= arr.length)
         return 0;
      int newIndex = index;
      if (node == null)
         return index;
      if (node.left != null)
         newIndex = toArray(arr, node.left, index);
      arr[newIndex] = node.data;
      if (node.right != null) {
         newIndex = toArray(arr, node.right, newIndex+1);
         return newIndex;
      }   
      return newIndex+1;
   }
   
   public static class TreeNode implements Comparable{
      public int data;
      public boolean accessed = false;
      public TreeNode left;
      public TreeNode right;
      public TreeNode parent;
      
      public TreeNode() {
         this.left = null;
         this.right = null;
         this.parent = null;
      }
      
      public TreeNode(int value) {
         this(value, null, null, null);
      }
      
      public TreeNode(int value, TreeNode parentNode) {
         this(value, null, null, parentNode);
      }   
      
      public TreeNode(int value, TreeNode leftNode, TreeNode rightNode, TreeNode parentNode) {
         this.data = value;
         this.left = leftNode;
         this.right = rightNode;
         this.parent = parentNode;
      }  
      
      public TreeNode deepCopy() {
         return deepCopy(this);
      }   
      
      public TreeNode deepCopy(TreeNode node) {
         if (node == null)
            return null;
         TreeNode newNode = new TreeNode(node.data);
         newNode.left = deepCopy(node.left);
         newNode.right = deepCopy(node.right);
         return newNode;
      }
      @Override
      public String toString() {
         return "" + this.data;
      }
      @Override
      public boolean equals(Object object) {
         if (!(object instanceof TreeNode))
            return false;
         if (object == null)
            return false;   
         TreeNode node = (TreeNode) object;
         return (this.data == node.data) && ((this.left != null) ? this.left.equals(node.left) : (node.left == null)) && ((this.right != null) ? this.right.equals(node.right) : (node.right == null));
      }
      
      public int compareTo(Object obj) {
         if (!(obj instanceof TreeNode))
            throw new ClassCastException();        
         TreeNode otherNode = (TreeNode) obj;
         return this.data - otherNode.data;
      }      
            
   }         
   
   @Override
   public String toString() {
      StringBuilder strBuild = new StringBuilder();
      toString(overallRoot, strBuild);
      return strBuild.toString();
   }
   
   private void toString(TreeNode node, StringBuilder strBuild) {
      if (node != null) {
         toString(node.left, strBuild);
         strBuild.append(node.data);
         strBuild.append(" ");
         toString(node.right, strBuild);
      }     
   }      
   
   public void resetAccesses() {
      resetAccesses(overallRoot);
   }
   
   private void resetAccesses(TreeNode node) {
      if (node != null) {
         node.accessed = false;
         resetAccesses(node.left);   
         resetAccesses(node.right); 
      }
   }      
   
   /*public Iterator<Integer> iterator() {
      //return new BinaryIntTreeArrayIterator();
      return new BinaryIntTreeIterator();
   }*/
   
   public Iterator<Integer> iterator() {
      return 
         new Iterator<Integer>() {
            {
               BinaryIntTree.this.resetAccesses();
            }
         
            private TreeNode currentNode = BinaryIntTree.this.lowestNode(BinaryIntTree.this.overallRoot);
         
            public boolean hasNext() {
               return currentNode != null; 
            }
         
            private TreeNode nextNode(TreeNode node) {
               if (node == null)
                  return null;
               if (node.left != null && !node.left.accessed)
                  return nextNode(node.left);
               if (!node.accessed)
                  return node;
               if (node.right != null && !node.right.accessed)
                  return nextNode(node.right);
               return nextNode(node.parent);           
            }
         
            public Integer next() {
               TreeNode retNode = currentNode;
               retNode.accessed = true;
               currentNode = nextNode(retNode);
               return retNode.data;
            }
         
            public void remove() { throw new UnsupportedOperationException("Removal is not yet supported"); }  
         
         };
   }      
      
   
   private class BinaryIntTreeArrayIterator implements Iterator<Integer> {
      
      private int current = 0;
      
      private int[] elements = BinaryIntTree.this.toArray();
      
      public boolean hasNext() {
         return current < elements.length;
      }
      
      public Integer next() {
         return elements[current++];
      }
      
      public void remove() { throw new UnsupportedOperationException("Removal is not yet supported"); }
      
   }   
   
   private class BinaryIntTreeIterator implements Iterator<Integer> {
   
      {
         BinaryIntTree.this.resetAccesses();
      }
      
      private TreeNode currentNode = BinaryIntTree.this.lowestNode(BinaryIntTree.this.overallRoot);
      
      public boolean hasNext() {
         return currentNode != null; 
      }
      
      private TreeNode nextNode(TreeNode node) {
         if (node == null)
            return null;
         if (node.left != null && !node.left.accessed)
            return nextNode(node.left);
         if (!node.accessed)
            return node;
         if (node.right != null && !node.right.accessed)
            return nextNode(node.right);
         return nextNode(node.parent);           
      }
      
      public Integer next() {
         TreeNode retNode = currentNode;
         retNode.accessed = true;
         currentNode = nextNode(retNode);
         return retNode.data;
      }
      
      public void remove() { throw new UnsupportedOperationException("Removal is not yet supported"); }   
      
   }   
     
}

@SuppressWarnings("unchecked")

class SearchTree<E extends Comparable<E>> implements Iterable<E>{

   public SearchTreeNode overallRoot;
   
   public SearchTree() {
      overallRoot = null;
   }   
   
   public SearchTree(E e) {
      overallRoot = new SearchTreeNode(e);
   }
   
   public SearchTree(SearchTreeNode node) {
      overallRoot = node.deepCopy();
   }
   
   public SearchTree<E> getCopy() {
      return new SearchTree<E>(overallRoot);
   }         
   
   public SearchTreeNode getRoot() {
      return overallRoot.deepCopy();
   }   
   
   public void insert(E e) {
      if (overallRoot == null) {
         overallRoot = new SearchTreeNode(e);
         return;
      }   
      insert(e, overallRoot);
   }
   
   private void insert(E e, SearchTreeNode node) {
      if (e.compareTo(node.data) < 0) {
         if (node.left != null) {
            insert(e, node.left);
         }
         else {
            node.left = new SearchTreeNode(e);
         }
      }
      else if (e.compareTo(node.data) >= 0) {
         if (node.right != null) {
            insert(e, node.right);
         }
         else {
            node.right = new SearchTreeNode(e);
         }
      }
   }
   
   public void printInorder() {
      printInorder(overallRoot);
      System.out.println();
   }
   
   private void printInorder(SearchTreeNode node) {
      if (node == null) {
         return;
      }
      if (node.left != null) {
         printInorder(node.left);
      }
      
      System.out.print(node.data.toString()+" ");
      
      if (node.right != null) {
         printInorder(node.right);
      }
   }
   
   public void printPreorder() {
      printPreorder(overallRoot);
      System.out.println();
   }
   
   private void printPreorder(SearchTreeNode node) {
      if (node == null) {
         return;
      }
      
      System.out.print(node.data.toString()+" ");
      
      if (node.left != null) {
         printPreorder(node.left);
      }
            
      if (node.right != null) {
         printPreorder(node.right);
      }
   }
   
   public void printPostorder() {
      printPostorder(overallRoot);
      System.out.println();
   }
   
   private void printPostorder(SearchTreeNode node) {
      if (node == null) {
         return;
      }
      if (node.left != null) {
         printPostorder(node.left);
      }
      
      if (node.right != null) {
         printPostorder(node.right);
      }
      
      System.out.print(node.data.toString()+" ");
   }
   
   public E highestValue() {
      return highestValue(overallRoot);
   }
   
   private E highestValue(SearchTreeNode node) {
      if (node.right == null) {
         return node.data;
      }
      return highestValue(node.right);
   }
   
   public E lowestValue() {
      return lowestValue(overallRoot);
   }
   
   private E lowestValue(SearchTreeNode node) {
      if (node.left == null) {
         return node.data;
      }
      return lowestValue(node.left);
   }
   
   public void printFullTree() {
      printFullTree(overallRoot, 0);
      System.out.println();
   }
   
   private void printFullTree(SearchTreeNode node, int level) {
      if (node == null) {
         return;
      }
      if (node.right != null) {
         printFullTree(node.right, level+1);
      }
      else {
         System.out.println();
      }
      for (int i = 0; i < level; i++) {
         System.out.print("    ");
      }
      System.out.println(node.data);
      if (node.left != null) {
         printFullTree(node.left, level+1);
      }
      else {
         System.out.println();
      }
   } 
   
   public int getSize() {
      return getSize(overallRoot);
   }
   
   private int getSize(SearchTreeNode node) {
      if (node == null)
         return 0;
      return 1 + getSize(node.left) + getSize(node.right);
   }
   
   public boolean equals(Object other) {
      if (!(other instanceof SearchTree))
         return false;
      SearchTree<E> otherTree = (SearchTree<E>) other;
      return this.overallRoot.equals(otherTree.getRoot());
   }   
   
   public int count(E e) {
      return count(e, overallRoot);
   }
   
   private int count(E e, SearchTreeNode node) {
      if (node == null)
         return 0;
      if (e.compareTo(node.data) == 0)
         return 1 + count(e, node.left) + count(e, node.right);
      return count(e, node.left) + count(e, node.right);
   }
   
   public boolean contains(E e) {
      return contains(e, overallRoot);
   }
   
   private boolean contains(E e, SearchTreeNode node) {
      return (node == null) ? false : (node.data.compareTo(e) == 0 || contains(e, node.left) || contains(e, node.right));
   } 
   
   public E[] toArray() {
      Comparable[] arr = new Comparable[this.getSize()];
      toArray(arr, overallRoot, 0);
      return (E[]) arr;
   }

   private int toArray(Comparable[] arr, SearchTreeNode node, int index) {
      if (index >= arr.length)
         return 0;
      int newIndex = index;
      if (node == null)
         return index;
      if (node.left != null)
         newIndex = toArray(arr, node.left, index);
      arr[newIndex] = node.data;
      if (node.right != null) {
         newIndex = toArray(arr, node.right, newIndex+1);
         return newIndex;
      }   
      return newIndex+1;
   } 
   
   public class SearchTreeNode {
      public E data;
      public boolean accessed = false;
      public SearchTreeNode left;
      public SearchTreeNode right;
      public SearchTreeNode parent;
      
      public SearchTreeNode() {
         this.left = null;
         this.right = null;
      }
      
      public SearchTreeNode(E e) {
         this(e, null, null);
      }
      
      public SearchTreeNode(E e, SearchTreeNode leftNode, SearchTreeNode rightNode) {
         this.data = e;
         this.left = leftNode;
         this.right = rightNode;
      }  
      
      public SearchTreeNode deepCopy() {
         return deepCopy(this);
      }   
      
      public SearchTreeNode deepCopy(SearchTreeNode node) {
         if (node == null)
            return null;
         SearchTreeNode newNode = new SearchTreeNode(node.data);
         newNode.left = deepCopy(node.left);
         newNode.right = deepCopy(node.right);
         return newNode;
      }
      
      public String toString() {
         return "" + this.data;
      }
      
      public boolean equals(SearchTreeNode node) {
         if (node == null)
            return false;
         return (this.data.compareTo(node.data) == 0) && ((this.left != null) ? this.left.equals(node.left) : (node.left == null)) && ((this.right != null) ? this.right.equals(node.right) : (node.right == null));
      }     
         
   }   
   
   private SearchTreeNode lowestNode(SearchTreeNode node) {
      return (node == null) ? null : ((node.left == null) ? node : lowestNode(node.left));
   }
   
   public void resetAccesses() {
      resetAccesses(overallRoot);
   }
   
   private void resetAccesses(SearchTreeNode node) {
      if (node != null) {
         node.accessed = false;
         resetAccesses(node.left);   
         resetAccesses(node.right); 
      }
   } 
   
   public Iterator<E> iterator() {
      //return new SearchTreeArrayIterator<E>();
      return new SearchTreeArrayIterator<E>();
   }        
   
   private class SearchTreeArrayIterator<E> implements Iterator<E> {
   
      private int current = 0;
      
      private Comparable[] elements = SearchTree.this.toArray();
      
      public boolean hasNext() {
         return current < elements.length;
      }
      
      public E next() {
         return (E) elements[current++];
      }
      
      public void remove() { throw new UnsupportedOperationException("Removal is not yet supported"); }
      
   } 
   
   private class SearchTreeIterator implements Iterator<E> {
   
      {
         SearchTree.this.resetAccesses();
      }
      
      private SearchTreeNode currentNode = lowestNode(SearchTree.this.overallRoot);
      
      public boolean hasNext() { 
         return currentNode != null; }
      
      private SearchTreeNode nextNode(SearchTreeNode node) {
         if (node == null)
            return null;
         if (node.left != null && !node.left.accessed)
            return nextNode(node.left);
         if (!node.accessed)
            return node;
         if (node.right != null && !node.right.accessed)
            return nextNode(node.right);
         return nextNode(node.parent);           
      }
      
      public E next() {
         SearchTreeNode retNode = currentNode;
         retNode.accessed = true;
         currentNode = nextNode(retNode);
         return retNode.data;
      }
      
      public void remove() {
         throw new UnsupportedOperationException("Removal is not yet supported");
      }   
      
   }   
     
}

package main

import (
	"errors"
	"fmt"
)

// Node is the type used by each node in the linked list
type Node struct {
	Value int
	Next  *Node
}

// LinkedList struct is the actual linked list.
// It stores the head noed and methods to perform operations
// on the linked list denoted by that head node
type LinkedList struct {
	head *Node
}

// Head returns the head node
func (list *LinkedList) Head() *Node {
	return list.head
}

// Insert appends a new node with a given value
// at the end of the linked list
func (list *LinkedList) Insert(val int) {
	if list.head == nil {
		list.head = &Node{Value: val}
		return
	}
	cur := list.head
	for cur.Next != nil {
		cur = cur.Next
	}
	cur.Next = &Node{Value: val}
}

// Search returns the node with a certain value if found, else nil.
func (list *LinkedList) Search(target int) (*Node, error) {

	cur := list.head
	for cur.Next != nil {
		if cur.Value == target {
			return cur, nil
		}
		cur = cur.Next
	}
	return nil, errors.New("value not found")
}

// PrintList traverses the list one by one
// and prints the value of each node
func (list *LinkedList) PrintList() {
	cur := list.head
	for cur != nil {
		fmt.Printf("%v -> ", cur.Value)
		cur = cur.Next
	}
	fmt.Println("nil")
}

func main() {
	ll := LinkedList{}
	ll.Insert(5)
	ll.Insert(510)
	ll.Insert(50)
	ll.Insert(10)
	ll.Insert(0)
	ll.PrintList()

	findTarget := 10
	if node, err := ll.Search(findTarget); err != nil {
		fmt.Printf("Error searching %v: %v\n", node.Value, err)
	} else {
		fmt.Printf("Found %v\n", node.Value)
	}

	findTarget = 20
	if node, err := ll.Search(findTarget); err != nil {
		fmt.Printf("Error searching %v: %v\n", findTarget, err)
	} else {
		fmt.Printf("Found %v\n", node.Value)
	}
}

package main

import (
	"fmt"
	"time"
)


func selectionSorted(a []string) []string {
	length := len(a)
	
	for i := 0; i<length-1; i++ {
		smallest := i

		for x:=i+1; x<length; x++ {
			if len(a[x]) < len(a[smallest]) {
				smallest = x
			}
		}

		if smallest != i {
			a[smallest], a[i] = a[i], a[smallest]
			fmt.Printf("\r%v", a)
			time.Sleep(800 * time.Millisecond)
		}

	}
	return a
}


func main() {
	a := []string {
		"#####",
		"######",
		"#",
		"#########",
		"########",
		"####",
		"###",
		"#######",
		"##",
	}

	// Lets print unsorted array
	fmt.Println("Unsorted array")
	for _,e := range a {
		fmt.Println(e)
	}
	
	// Sorting array here
	a = selectionSorted(a)
	// fmt.Printf("\nIterated %v times.\n", iterations)

	// Lets print sorted array
	fmt.Println("\nSorted array")
	for _,e := range a {
		fmt.Println(e)
	}
}


/* OUTPUT

Unsorted array
#####
######
#
#########
########
####
###
#######
##
[# ## ### #### ##### ###### ####### ######## #########]
Sorted array
#
##
###
####
#####
######
#######
########
#########
*/
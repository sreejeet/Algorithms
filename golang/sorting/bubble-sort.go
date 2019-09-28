package main

import "fmt"


func swap(a *string, b *string){
	tmp := *a
	*a = *b
	*b = tmp
}


func bubbleSorted(a []string) (int, []string) {
	length := len(a)
	iteration := 0

	for ; iteration<length-1; iteration++ {
		swapped := false
		for x:=0; x<length-1-iteration; x++ {
			if len(a[x]) > len(a[x+1]) {
				// fmt.Println("Swapping", x, "and", x+1)
				swapped = true
				swap(&a[x], &a[x+1])
			}
		}
		// If the last iteration did not swap anything,
		// it means all the values are now sorted comlpetely.
		if !swapped{
			break
		}
	}
	return iteration, a
}


func main() {
	a := []string{
		"#####",
		"############",
		"######",
		"#",
		"##########",
		"#########",
		"####",
		"########",
		"##",
	}

	// Lets print unsorted array
	fmt.Println("Unsorted array")
	for _,e := range a{
		fmt.Println(e)
	}
	
	// Sorting array here
	iterations, a := bubbleSorted(a)
	fmt.Printf("\nIterated %v times.\n", iterations)

	// Lets print sorted array
	fmt.Println("\nSorted array")
	for _,e := range a{
		fmt.Println(e)
	}
}

// OUTPUT
/*
Unsorted array
#####
############
######
#
##########
#########
####
########
##

Iterated 7 times.

Sorted array
#
##
####
#####
######
########
#########
##########
############
*/
package main

import "fmt"

func main() {
    var a float64
    var b float64
    
    _, err := fmt.Scanln(&a, &b)
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println(a / b)
    }
}
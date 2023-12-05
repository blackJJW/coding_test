package main

import "fmt"

func main() {
    var a, b, c int
    
    _, err := fmt.Scanln(&a, &b, &c)
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println(a + b + c)
    }
}
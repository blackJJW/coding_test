package main

import "fmt"

func main() {
    var a int
    var b int
    
    _, err := fmt.Scan(&a, &b)
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println(a * (b % 10))
        fmt.Println(a * ((b / 10) - ((b / 100)*10)))
        fmt.Println(a * (b / 100))
        fmt.Println(a * b)
    }
}
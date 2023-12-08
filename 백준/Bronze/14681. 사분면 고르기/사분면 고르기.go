package main

import "fmt"

func main() {
    var a, b int
    
    _, err := fmt.Scan(&a, &b)
    if err != nil {
        fmt.Println(err)
    } else {
        if a > 0 && b > 0 {
            fmt.Println(1)
        } else if a > 0 && b < 0 {
            fmt.Println(4)
        } else if a < 0 && b > 0 {
            fmt.Println(2)
        } else {
            fmt.Println(3)
        }
    }
}
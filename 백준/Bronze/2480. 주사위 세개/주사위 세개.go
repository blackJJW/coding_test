package main

import (
    "fmt"
)

func main() {
    var a, b, c int
    
    _, err := fmt.Scanln(&a, &b, &c)
    if err != nil {
        fmt.Println(err)
        return
    }
    
    if a == b && b == c {
        fmt.Println(10000 + (a * 1000))
    } else if (a == b) && a != c {
        fmt.Println(1000 + (a * 100))
    } else if (a == c) && a != b {
        fmt.Println(1000 + (a * 100))
    } else if (b == c) && b != a {
        fmt.Println(1000 + (b * 100))
    } else {
        fmt.Println(max(a, b, c) * 100)
    }
}
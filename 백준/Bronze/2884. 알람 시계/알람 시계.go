package main

import "fmt"

func main() {
    var a, b int
    
    _, err := fmt.Scanln(&a, &b)
    if err != nil {
        fmt.Println(err)
    } else {
        if (b - 45) < 0 && a == 0 {
            a = 23
            b = b + 15
            fmt.Println(a, b)
        } else if (b - 45) < 0 && a != 0 {
            a = a - 1
            b = b + 15
            fmt.Println(a, b)
        } else {
            a = a
            b = b - 45
            fmt.Println(a, b)
        }
    }
}
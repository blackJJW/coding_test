package main

import "fmt"

func main() {
    var year int
    
    _, err := fmt.Scanln(&year)
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println(year - 543)
    }
}
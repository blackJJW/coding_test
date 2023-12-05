package main 

import "fmt"

func main() {
    var a, b int
    
    _, err := fmt.Scanln(&a, &b)
    if err != nil {
        fmt.Println(err)
    } else {
        if a > b {
            fmt.Println(">")
        } else if a < b {
            fmt.Println("<")
        } else {
            fmt.Println("==")
        }
    }
}
package main

import "fmt"

func main() {
    var msg string
    
    _, err := fmt.Scanln(&msg)
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println(msg + "??!")
    }
}
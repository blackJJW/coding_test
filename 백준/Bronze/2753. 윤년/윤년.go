package main

import "fmt"

func main() {
    var a int
    _, err := fmt.Scanln(&a)
    if err != nil {
        fmt.Println(err)
    }
    
    if ((a % 4 == 0) && (a % 100 != 0)) || (a % 400 == 0){
        fmt.Println("1")
    } else {
        fmt.Println("0")
    }
}
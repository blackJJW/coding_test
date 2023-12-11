package main

import "fmt"

func main() {
    var h, m, t int
    
    _, err := fmt.Scanln(&h, &m)
    if err != nil {
        fmt.Println(err)
        return
    }
    
    _, err = fmt.Scan(&t)
    if err != nil {
        fmt.Println(err)
        return
    }

    total_m := m + t

    if total_m > 59 {
        plus_h := total_m / 60

        if h+plus_h > 23 {
            fmt.Printf("%d %d", (h+plus_h-24), total_m%60)
        } else {
            fmt.Printf("%d %d", (h + plus_h), total_m%60)
        }
    } else {
        fmt.Printf("%d %d", h, total_m)
    }
}
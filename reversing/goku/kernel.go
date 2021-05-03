package main

import (
    "fmt"
)

func f() string {
    return "799159"
}
func a() string {
    return "_"
}
func c() string {
    return "summon"
}
func b() string {
    return "the"
}
func e() string {
    return "spirit"
}
func d() string {
    return "bomb"
}

func function() string {
    var cat string
    var dog bool = true
    var owl bool = true
    var pig bool = true
    var cow bool = true
    var rat bool = true
    for i := 1; i < 32; i++ {
        if !rat && !dog && !owl && !pig && !cow {
            break
        }
        if i % 17 == 0 && rat {
            cat += f()
            rat = false
        }
        if i % 11 == 0 && pig {
            cat += e()
            pig = false
        }
        if i % 4 == 0 {
            cat += a()
        }
        if i % 5 == 0 && owl {
            cat += b()
            owl = false
        }
        if i % 2 == 0 && dog {
            cat += c()
            dog = false
        }
        if i % 13 == 0 && cow {
            cat += d()
            cow = false
        }
    }
    cat = "gigem{" + cat
    cat += "}"
    return cat
}

func main() {
    function()
    fmt.Printf("TODO :: PUT FLAG HERE\n")
}

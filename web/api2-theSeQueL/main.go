package main

import (
    "fmt"
    "image"
    "bytes"
    "database/sql"
    "encoding/base64" 
    "os"
    "image/png"
    "net/http"
    "html/template"
    "io/ioutil"
    "net/url"

    _ "github.com/lib/pq"
)

// Struct for the card
type SCPCard struct {
    Codename string
    Id string
    Containment string
    Description string
    Image string
}

type CardHolder struct {
    Cards []SCPCard
}

type Debug struct {
    Error string
}

const (
    host = "localhost"
    port = 5432
    user = "yeetus"
    password = "stardate2387jellyfish"
    dbname = "scpfoundation"
)

func encodeImage(path string) string {
    var buffer bytes.Buffer

    // Open image
    imgFile, err := os.Open(path)
	if err != nil {
        imgFile, err = os.Open("imgs/avatar.png")
	}
	defer imgFile.Close()

	imageData, _, imgErr := image.Decode(imgFile)
	if err != nil {
        panic(imgErr)
	}

    encErr := png.Encode(&buffer, imageData)
    if err != nil {
        panic(encErr)
    }

    return base64.StdEncoding.EncodeToString(buffer.Bytes())
}

func pageHandler(w http.ResponseWriter, req *http.Request) {

    // Parse the URL query into a map of key, value (strings I think)
    newMap, err := url.ParseQuery(req.URL.RawQuery)
    if err != nil {
        panic(err)
    }

    if len(newMap) == 0 {
        newMap["name"] = []string{"Default"}
    }

    w.Header().Add("Content-Type", "text/html")

    // Read in index.html
    file, fErr := ioutil.ReadFile("./index.html")
    if fErr != nil {
        panic(fErr)
    }
    doc := string(file)

    // Fill out the template
    tmpl, err := template.New("anyNameForTemplate").Parse(doc)
    if err == nil {

        // Connect to and query database
        var id string
        var codename string
        var containment string
        var description string
        var img string

        // Connection String
        psqlInfo := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", host, port, user, password, dbname)
        db, dbErr := sql.Open("postgres", psqlInfo)
        if dbErr != nil {
            panic(dbErr)
        }
        defer db.Close()

        // Ping Test
        //pingErr := db.Ping()
        //if pingErr != nil {
        //    panic(pingErr)
        //}

        cardHolder := CardHolder{}

        if len(newMap) != 0 {
            query := "SELECT * FROM experiments WHERE codename LIKE '%" + newMap["name"][0] + "%'"
            rows, rowErr := db.Query(query)
            if rowErr != nil {
                file, fErr := ioutil.ReadFile("./debug.html")
                if fErr != nil {
                    panic(fErr)
                }
                doc := string(file)

                e := Debug{ Error: fmt.Sprintf("%s", rowErr) }

                // Fill out the template
                tmpl, _ := template.New("debugger").Parse(doc)
                tmpl.Execute(w, e)
                return
            }

            for rows.Next() {
                rowErr = rows.Scan(&id, &codename, &containment, &description, &img)
                if rowErr != nil {
                    panic(rowErr) 
                }
                data := SCPCard {
                    Codename : codename,
                    Id : id,
                    Containment : containment,
                    Description : description,
                    Image : "imgs/" + img + ".png",
                }

                // Creating the image
                data.Image = encodeImage(data.Image)
                cardHolder.Cards = append(cardHolder.Cards, data)
            }
            //fmt.Printf("%v %v %v %v %v\n", id, codename, containment, description, img)

            // Fill in the template
            tmpl.Execute(w, cardHolder)
        }
    }
}

func main() {
    // Handler
    http.HandleFunc("/", pageHandler)
    http.ListenAndServe(":1337", nil)
}

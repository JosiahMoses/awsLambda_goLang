package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main() {

	var userInput string
	fmt.Println("Enter IP: ")
	fmt.Scanln(&userInput)
	fmt.Println("IP enterd: " + userInput)
	response, err := http.Get("http://ipwhois.app/json/" + userInput)

	if err != nil {
		fmt.Print(err.Error())
		os.Exit(1)
	}

	responseData, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(responseData))

}

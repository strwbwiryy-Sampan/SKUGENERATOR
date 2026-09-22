from pyscript import display, document

def display_char(e):
    document.getElementById("output1").innerHTML = ""

    get_word =   document.getElementById("word").value

    display(get_word[:3], target="output1") #get the first three letters of the word
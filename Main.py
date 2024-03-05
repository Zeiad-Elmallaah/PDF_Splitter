from PyPDF2 import PdfWriter, PdfReader

names_of_people_going = [
    "Sophia",
    "Liam",
    "Olivia",
    "Noah",
    "Emma",
    "Jackson",
    "Ava",
    "Lucas",
    "Isabella",
    "Oliver",
    "Mia",
    "Ethan"
]

inputpdf = PdfReader(open("Train_Tickets.pdf", "rb"))


counter = 0
for person in names_of_people_going:
    output = PdfWriter()
    for i in range(0, 2):
        print(person, (i+counter))
        output.add_page(inputpdf.pages[i+counter])
        with open((person + "_ticket" + ".pdf"), "wb") as outputStream:
            output.write(outputStream)
    counter = counter + 2

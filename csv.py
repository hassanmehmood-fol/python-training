from openpyxl import load_workbook

file_path = "Book1.xlsx"

wb = load_workbook(file_path)
sheet = wb.active  

user_name = input("Enter your name: ")


sheet.append([user_name])

wb.save(file_path)

print("Name added successfully!")

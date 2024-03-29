import tkinter as tk

def fahrenheit_to_celsius():
    # อ่านค่าอุณหภูมิจากช่องข้อมูล
    fahrenheit = float(entry.get())
    # แปลงจากองศาฟาเรนไฮน์เป็นองศาเซลเซียส
    celsius = (fahrenheit - 32) * 5/9
    # แสดงผลลัพธ์
    label_result["text"] = f"{fahrenheit} องศาฟาเรนไฮน์ = {celsius:.2f} องศาเซลเซียส"

# สร้างหน้าต่าง Tkinter
window = tk.Tk()
window.title("แปลงอุณหภูมิ")

# สร้างข้อความและช่องข้อมูลสำหรับอุณหภูมิ
label = tk.Label(window, text="กรุณากรอกอุณหภูมิในหน่วยองศาฟาเรนไฮน์:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# สร้างปุ่มสำหรับแปลง
button_convert = tk.Button(window, text="แปลง", command=fahrenheit_to_celsius)
button_convert.pack()

# สร้างข้อความสำหรับผลลัพธ์
label_result = tk.Label(window, text="")
label_result.pack()

# เริ่มต้นโปรแกรม
window.mainloop()

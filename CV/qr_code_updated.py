import qrcode
import cv2
import matplotlib.pyplot as plt


products = {
    1: ["Apple", "Food", "123456789", 4, 50, 15], 
    2: ["Milk", "Dairy", "987654321", 1, 40, 0],
    3: ["Bread", "Food", "112233445", 2, 30, 20],
    4: ["Shampoo", "Personal Care", "998877665", 1, 120, 10]
}


total_price = 0
for serial_no, product in products.items():
    name, category, barcode, quantity, price, discount = product
    final_price = price * (1 - (discount/100)) * quantity
    total_price += final_price


overall_discount = 10 
total_price_after_discount = total_price * (1 - (overall_discount)/100)


img = qrcode.make(f'upi://pay?pa=7569664234@ybl&pn=JAGADEESH&am={total_price_after_discount:.2f}&cu=INR')


img.save('qrcode_test.png')


image = cv2.imread("qrcode_test.png")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Hide axis
plt.show()

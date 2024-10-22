import qrcode
import cv2
import matplotlib.pyplot as plt

price = 33
img = qrcode.make(f'upi://pay?pa=7569664234@ybl&pn=JAGADEESH&am={price}&cu=INR')
# upi://pay?pa=<UPI_ID>&pn=<Name>&mc=<Merchant_Code>&tid=<Transaction_ID>&tr=<Transaction_Ref_ID>&tn=<Transaction_Note>&am=<Amount>&cu=<Currency>&url=<URL>

img.save('qrcode_test.png')
image = cv2.imread("qrcode_test.png")

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()


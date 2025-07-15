import csv
import qrcode
import matplotlib.pyplot as plt

# Function to get the link based on the name
# %%
def get_links(name, filename='66159_6418847_4377234.csv'):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == name:
                return row[1:]
        return None

# Function to display a QR code
# %%
def display_qrcode(link):
    qr = qrcode.QRCode()
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    plt.imshow(img, cmap="gray")
    plt.axis('off')
    plt.show()

# Prompt the user to choose a name
# %%
while True:
    user_choice = input("Choose a name (1 for name1, 2 for name2): ")
    if user_choice == '1':
        name = 'name1'
        break
    elif user_choice == '2':
        name = 'name2'
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

link = get_links(name)

if link and len(link) > 0:
    display_qrcode(link[0])
else:
    print(f"No link found for {name}")

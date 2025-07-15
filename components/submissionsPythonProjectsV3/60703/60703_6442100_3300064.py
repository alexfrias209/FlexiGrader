from random import randint


print('Hello there, welcome to the one stop shop to the perfect product.')
print('Developed')
print('In short, this is a test to compile what is favored from your experiences with products in the past and what we have in stock. These products are all kept in mind to be afforable!')
print('We will use the information you grant us to give you the best products we think will suit you.')
print('To begin with some questions')
print('What type of product are you interested in? From options: 1/2/3/4')
print('1) Hair')
print('2) Skin Care')
print('3) Facial Cosmetics')
print('4) Nails')
Product_list = {1:'Hair', 2:'Skin Care', 3:'Facial Cosmetics', 4:'Nails'}
product = int(input())
print('Now that we got the general item of interest, its time for specifics')
if (product== 1):
    print('So, you chose Hair. We have 5 options available for what we got in stock.')
    print('Choose from: 1/2/3/4/5')
    print('1) Hair Oil; Something to give that hair some growth and reduce dryness.')
    print('2) Hair Mask; Reduces frizz, adds moisture, and strengthens hair.')
    print('3) Scalp Mask; Deeply nourish or can exfoliate.')
    print('4) Leave In Conditioner; Hydrates hair shaft')
    print('5) Hair Moose; Reduces frizz and helps lifen curls with some extra bounce.')
    hair = {1:'hair oil', 2:'hair mask', 3:'scalp mask', 4:'leave in conditioner', 5:'hair moose'}
    hair_option = int(input())
    if hair_option==1:
        brand = str('Mielle')
        price = str('$9.99')
        print('You chose', Product_list.get(1))
        print('The options displayed', hair.get(1), 'with recommended brand:', brand, price)
    if hair_option==2:
        brand = str('Olaplex No.8 Bond Intense Moisture Mask')
        price = str('$30')
        print('You chose', Product_list.get(1))
        print('The options displayed', hair.get(2), 'with recommended brand:', brand, price)
    if hair_option==3:
        brand = str('Sephora Collection, Purifying Green Clay Scalp Mask + AHA')
        price = str('$16')
        print('You chose', Product_list.get(1))
        print('The options displayed', hair.get(3), 'withrecommended brand:', brand, price)
    if hair_option==4:
        brand = str('SheaMoisture Manuka Honey and Mafura Oil Inteseive Hydration Leave-In Conditioner')
        price = str('$13')
        print('You chose', Product_list.get(1))
        print('The options displayed', hair.get(4), 'with recommended brand:', brand, price)
    if hair_option==5:
        brand = str("Not Your Mother's Curl Talk Refreshing Curl Foam")
        price = str('$7.75')
        print('You chose', Product_list.get(1))
        print('The options displayed', hair.get(5), 'with recommended brand:', brand, price)
elif (product == 2):
    print('So, you chose Skin Care. We have 5 options available for what we got in stock.')
    print('Choose from: 1/2/3/4/5')
    print('1) Serums; Helps skin look firm and toned. Can soothe sensitive skin.')
    print('2) Moisturizers; Reduce fine lines and make skin appear smooth and soft.')
    print('3) Exfoliators; Helps to clean skin from dead cells and remove oil.')
    print('4) Body Lotions; Lather up for some dry irriated skin.')
    print('5) Body oils; Gives moisture and gloss layer to brighten up skin with chosen nutrients.')
    Skin_Care = {1:'Serums', 2:'Moisturizers', 3:'Exfoliators', 4:'Body Lotions', 5:'Body Oils'}
    Skin_Care_option = int(input())
    if Skin_Care_option ==1:
        brand = str('Vichy Ideal Body-Serum Milk')
        price = str('$29')
        print('You chose', Product_list.get(2))
        print('The options displayed', Skin_Care.get(1), 'with recommended brand:', brand, price)
    if Skin_Care_option == 2:
        brand = str('CeraVe Daily Moisturizing Lotion')
        price = str('$12')
        print('You chose', Product_list.get(2))
        print('The options displayed', Skin_Care.get(2), 'with recommended brand:', brand, price)
    if Skin_Care_option == 3:
        brand = str('Tree Hut, Shea Sugar Scrub')
        price = str('8$')
        print('You chose', Product_list.get(2))
        print('The options displayed', Skin_Care.get(3), 'with recommended brand:', brand, price)
    if Skin_Care_option == 4:
        brand = str('Nivea Essentially Enriched Body Lotion')
        price = str('$8')
        print('You chose', Product_list.get(2))
        print('The options displayed', Skin_Care.get(4), 'with recommended brand:', brand, price)
    if Skin_Care_option == 5:
        brand = str("Palmer's Cocoa Butter Moisturizing Body Oil")
        price = str('$8')
        print('You chose', Product_list.get(2))
        print('The options displayed', Skin_Care.get(5), 'with recommended brand:', brand, price)
elif (product == 3):
    print('So, you chose Facial Cosmetics. We have 5 options available for what we got in stock.')
    print('Choose from: 1/2/3/4/5')
    print('1) Foundation; A base to perform makeup on a solid color.')
    print('2) Contour; For shadows and shaping curves and edge.')
    print('3) Makeup Remover; Removing the work.')
    print('4) Brow Pencil; Draw on eyebrows/Give eyebrows more shape.')
    print('5) Eyeshadow; Color add onto eyebrow ridge.')
    facial_cosmetics={1:'Foundation', 2:'Contour', 3:'Makeup Remover', 4:'Brow Pencil', 5:'Eyeshadow'}
    facial_cos_options= int(input())
    if facial_cos_options ==1:
        brand = str("Fenty Beauty Pro Filt'r Soft Matte Foundation at Sephora")
        price = str('$18')
        print('You chose', Product_list.get(3))
        print('The options displayed', facial_cosmetics.get(1), 'with recommended brand:', brand, price)
    if facial_cos_options ==2:
        brand = str("Charlottle Tilbury Bronze & Glow Contour Duo")
        price = str('$56')
        print('You chose', Product_list.get(3))
        print('The options displayed', facial_cosmetics.get(2), 'with recommended brand:', brand, price)
    if facial_cos_options ==3:
        brand = str("CeraVe Hydrating Makeup Removing Plant-Based Wipes")
        price = str('$10')
        print('You chose', Product_list.get(3))
        print('The options displayed', facial_cosmetics.get(3), 'with recommended brand:', brand, price)
    if facial_cos_options ==4:
        brand = str("L'Oréal Paris Brow Stylist Definer")
        price = str('$9')
        print('You chose', Product_list.get(3))
        print('The options displayed', facial_cosmetics.get(4), 'with recommended brand:', brand, price)
    if facial_cos_options ==5:
        brand = str("ILIA The NEcessary Eyeshadow Palette")
        price = str('$38')
        print('You chose', Product_list.get(3))
        print('The options displayed', facial_cosmetics.get(5), 'with recommended brand:', brand, price)
elif(product==4):
    print('So, you chose Nails. We have 3 options available for what we got in stock.')
    print('Choose from: 1/2/3')
    print('1) Nail Polish; Colorful display for some beautiful creativity.')
    print('2) Nail Coat; Clear shine to lift up any polish')
    print('3) Nail File; To reduce nail growth and keep your ends smooth.')
    nails = {1:'Polish', 2:'Coat', 3:'File'}
    nails_options = int(input())
    if nails_options ==1:
        brand = str("Sally Hansen Insta-Dri")
        price = str('$7')
        print('You chose', Product_list.get(4))
        print('The options displayed', nails.get(1), 'with recommended brand:', brand, price)
    if nails_options ==2:
        brand = str("L.A. COLORS Craze Base Coat")
        price = str('$2')
        print('You chose', Product_list.get(4))
        print('The options displayed', nails.get(2), 'with recommended brand:', brand, price)
    if nails_options ==3:
        brand = str("Makartt Professional Nail File")
        price = str('$10')
        print('You chose', Product_list.get(4))
        print('The options displayed', nails.get(3), 'with recommended brand:', brand, price)

random = Product_list.get(randint(1,4))

print('We got that you should look at',brand,'. Our suggested item would be', random)
print('Please rate this experience!, from 1-10')

rating= int(input())
while rating <= 10:
    print('Thank you for your time. Hope this helped!')
    break


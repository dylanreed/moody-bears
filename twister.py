from PIL import Image 
from IPython.display import display 
import random
import json

#Inject all the shapes and set their weights

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%


backgrounds = ["BLACK", "GREY", "GREEN", "MARION", "YELLOW", "MAGENTA", "CONFETTI MIST", "NEWSPRINT", "PINK", "BLUE", "PURPLE CRACK", "3D BLUE"] 
backgrounds_weights = [0.12, 0.12, 0.12, 0.12, 0.12, 0.07, 0.07, 0.07, 0.07, 0.055, 0.055, 0.01]

bodies = ["BLUEBERRY", "KELLY", "PURPLE", "RED", "BROWN", "GREY", "SKETCH"] 
bodies_weights = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.1]

wears = ["NAKED", "POWER TIE", "PARTY TIE", "NEWAVE SKINNY TIE", "CLOWN BOW TIE", "CHIPPY", "BLACK TIE", "PICNIC TIE", "CIRCUS SCARF", "BUDDY BOW TIE", "DANCING"] 
wears_weights = [0.35, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.05, 0.05, 0.05, 0.02]

moods = ["AHHH", "BLBL", "BLSS", "DOHH", "GRRR", "MMMM", "OHHH", "UHHH", "WHOA", "ZZZZ", "BLAH", "GLAH", "HMPH", "NRVS"] 
moods_weights = [0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143, 0.07142857143]

atmos = ["CLEAR", "BUBBLES", "CONFETTI", "HONEY", "RAIN"] 
atmos_weights = [0.6, 0.1, 0.1, 0.1, 0.1]


# Dictionary variable for each trait. 
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish


backgrounds_files = {
    "BLACK": "09MB_NFT-BKG-BLK",
    "GREY": "09MB_NFT-BKG-GREY",
    "GREEN": "09MB_NFT-BKG-MNTG",
    "MARION": "09MB_NFT-BKG-MRNG",
    "YELLOW": "09MB_NFT-BKG-YLWG",
    "MAGENTA": "09MB_NFT-BKG-MGNT",
    "CONFETTI MIST": "09MB_NFT-BKG-CNFTG",
    "NEWSPRINT": "09MB_NFT-BKG-NWSP",
    "PINK": "09MB_NFT-BKG-PINK",
    "BLUE": "09MB_NFT-BKG-PRCH",
    "PURPLE CRACK": "09MB_NFT-BKG-BKBL",
    "3D BLUE": "01MB_NFT-BKG-3DBLU"
}

bodies_files = {
    "BLUEBERRY": "15MB_NFT-BLUE_BEAR",
    "KELLY": "15MB_NFT-GREEN_BEAR",
    "PURPLE": "15MB_NFT-PRPL_BEAR",
    "RED": "15MB_NFT-RED_BEAR",
    "BROWN": "15MB_NFT-BRWN_BEAR",
    "GREY": "15MB_NFT-GREY_BEAR",
    "SKETCH": "10MB_NFT-SKTCH_BEAR"
}

wears_files = {
    "NAKED": "35MB_NFT-PFP_NAKED",
    "POWER TIE": "08MB_NFT-PFP_POWER",
    "PARTY TIE": "08MB_NFT-PFP_PARTY",
    "NEWAVE SKINNY TIE": "08MB_NFT-PFP_NEWAV",
    "CLOWN BOW TIE": "08MB_NFT-PFP_CLOWN",
    "CHIPPY": "08MB_NFT-PFP_CHPNDL",
    "BLACK TIE": "08MB_NFT-PFP_BLKTIE",
    "PICNIC TIE": "05MB_NFT-PFP_PICNIC",
    "CIRCUS SCARF": "05MB_NFT-PFP_LADY",
    "BUDDY BOW TIE": "05MB_NFT-PFP_BUDDY",
    "DANCING": "02MB_NFT-PFP_DANCE"
}

moods_files = {
    "AHHH": "MB_NFT-PFP_AHHH",
    "BLBL": "MB_NFT-PFP_BLBL",
    "BLSS": "MB_NFT-PFP_BLSS",
    "DOHH": "MB_NFT-PFP_DOHH",
    "GRRR": "MB_NFT-PFP_GRRR",
    "MMMM": "MB_NFT-PFP_MMMM",
    "OHHH": "MB_NFT-PFP_OHHH",
    "UHHH": "MB_NFT-PFP_UHHH",
    "WHOA": "MB_NFT-PFP_WHOA",
    "ZZZZ": "MB_NFT-PFP_ZZZZ",
    "BLAH": "MB_NFT-PFP_BLAH",
    "GLAH": "MB_NFT-PFP_GLAH",
    "HMPH": "MB_NFT-PFP_HMPH",
    "NRVS": "MB_NFT-PFP_NRVS"
}

atmos_files = {
    "CLEAR": "60MB_NFT-PFP_CLEAR",
    "BUBBLES": "10MB_NFT-PFP_BUBBLES",
    "CONFETTI": "10MB_NFT-PFP_CNFT",
    "HONEY": "10MB_NFT-PFP_HONEY",
    "RAIN": "10MB_NFT-PFP_RAIN"
}

#Create a function to generate unique image combinations
TOTAL_IMAGES = 1000 # Number of random unique images we want to generate ( 2 x 2 x 2 = 8)

all_images = [] 

def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    #new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["backgrounds"] = random.choices(backgrounds, backgrounds_weights)[0]
    new_image ["bodies"] = random.choices(bodies, bodies_weights)[0]
    new_image ["wears"] = random.choices(wears, wears_weights)[0]
    new_image ["moods"] = random.choices(moods, moods_weights)[0]
    new_image ["atmos"] = random.choices(atmos, atmos_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)

#Return true if all images are unique

def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

#add token id

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

#print all images

print(all_images)

#get trait count

backgrounds_count = {}
for item in backgrounds:
    backgrounds_count[item] = 0

bodies_count = {}
for item in bodies:
    bodies_count[item] = 0

wears_count = {}
for item in wears:
    wears_count[item] = 0

moods_count = {}
for item in moods:
    moods_count[item] = 0

atmos_count = {}
for item in atmos:
    atmos_count[item] = 0


for image in all_images:
    #background_count[image["Background"]] += 1
    backgrounds_count[image["backgrounds"]] += 1
    bodies_count[image["bodies"]] += 1
    wears_count[image["wears"]] += 1
    moods_count[image["moods"]] += 1
    atmos_count[image["atmos"]] += 1


#print(background_count)
print(backgrounds_count)
print(bodies_count)
print(wears_count)
print(moods_count)
print(atmos_count)


#Generate Metadata for all Traits

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#Generate Images

for item in all_images:

    im1 = Image.open(f'./layers/backgrounds/{backgrounds_files[item["backgrounds"]]}.png').convert('RGBA')
    im2 = Image.open(f'./layers/bodies/{bodies_files[item["bodies"]]}.png').convert('RGBA')
    im3 = Image.open(f'./layers/wears/{wears_files[item["wears"]]}.png').convert('RGBA')
    im4 = Image.open(f'./layers/moods/{moods_files[item["moods"]]}.png').convert('RGBA')
    im5 = Image.open(f'./layers/atmos/{atmos_files[item["atmos"]]}.png').convert('RGBA')
    
    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)

    #Convert to RGB
    rgb_im = com4.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)

#Generate Metadata

#f = open('./metadata/all-traits.json',) 
#data = json.load(f)

#IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE/"
#PROJECT_NAME = "Balloon Animals"

#def getAttribute(key, value):
#    return {
#        "trait_type": key,
#        "value": value
#    }
#for i in data:
#    token_id = i['tokenId']
#    token = {
#        "image": IMAGES_BASE_URI + str(token_id) + '.png',
#        "tokenId": token_id,
#        "name": PROJECT_NAME + ' ' + str(token_id),
#        "attributes": []
#    }
#    token["attributes"].append(getAttribute("Background", i["Background"]))
#    token["attributes"].append(getAttribute("Back Legs", i["Back Legs"]))
#    token["attributes"].append(getAttribute("backgrounds", i["backgrounds"]))
#    token["attributes"].append(getAttribute("Ears", i["Ears"]))
#    token["attributes"].append(getAttribute("Front Legs", i["Front Legs"]))
#    token["attributes"].append(getAttribute("Head", i["Head"]))
#    token["attributes"].append(getAttribute("atmos", i["atmos"]))
#    token["attributes"].append(getAttribute("Tail", i["Tail"]))
#    token["attributes"].append(getAttribute("Outline", i["Outline"]))

#    with open('./metadata/' + str(token_id), 'w') as outfile:
#        json.dump(token, outfile, indent=4)
#f.close()
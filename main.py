import requests
import os
import htmlparser
dexList = {'pokedex'}
           #'pokedex-gs',
           #'pokedex-rs',
           #'pokedex-dp',
           #'pokedex-bw',
           #'pokedex-xy',
           #'pokedex-sm',
           #'pokedex-swsh'}
           #'pokedex-sv'}

imageList = {'green'}

#Change Directory format depending on Operating System
parent_dir = '/Users/jamie/Documents/PokemonPy/'
results = []

#Creates directory if it does not already exists for caching HTML files.
def create_dir(name):
    dir = name
    path = os.path.join(parent_dir, dir)
    isExist = os.path.exists(path)
    if(isExist):
        print(f'Path: {path} already exists')
    else:
        return os.mkdir(path)
        print(f'Path: {path} was created!')

def gatherImageFiles(image):
    create_dir(image)
    path = os.path.join(parent_dir, image)
    isExists = os.path.exists(path)
    size = os.path.getsize(path)
    var = True
    if(isExists & size > 0):
        print(f'{image} folder is already created')
        var = False
    else:
        x = 0
        while var:
            try:
                if (x <= 9):
                    url = f'https://www.serebii.net/pokearth/sprites/{image}/00{x}.png'
                elif (x <= 99):
                    url = f'https://www.serebii.net/pokearth/sprites/{image}/0{x}.png'
                else:
                    url = f'https://www.serebii.net/pokearth/sprites/{image}/{x}.png'
                response = requests.get(url)
                if (response.status_code == 200):
                    results.append(open(f'{path}/{x}.png', 'wb').write(response.content))
                    print(f'Log: Pokemon Number {x} images, {image}')
                    x += 1
                    var = True
                elif (x == 0):
                    var = True
                    x += 1
                else:
                    var = False
            except StopIteration:
                break


def gatherHtmlFiles(dex):
    create_dir(dex)
    path = os.path.join(parent_dir, dex)
    isExists = os.path.exists(path)
    size = os.path.getsize(path)
    var = True

    # Checks if files have already been gathered. If so Skip process
    if(isExists & size > 0):
        print(f'{dex} is already gathered')
        var = False
    else:
        x = 0
        while var:
            try:
                if (x <= 9):
                    url = f'https://www.serebii.net/{dex}/00{x}.shtml'
                elif (x <= 99):
                    url = f'https://www.serebii.net/{dex}/0{x}.shtml'
                else:
                    url = f'https://www.serebii.net/{dex}/{x}.shtml'
                response = requests.get(url)
                if (response.status_code == 200):
                    results.append(open(f'{path}/{x}.shtml', 'wb').write(response.content))
                    print(f'Log: Pokemon Number {x}, {dex}')
                    x+=1
                    var = True
                elif(x == 0):
                    var = True
                    x+=1
                #Only here because Scarlett and Violet have a weird web format. Will most likely change this later.
                elif(dex.__contains__('sv')):
                    var = True
                    x+=1
                    if (x >= 1008):
                        var = False
                else:
                    var = False
            except StopIteration:
                break

        print(f'Log: {dex} complete with {x} files created with usable data')

prompt = "Please Choose the Process you would like use from the options below: "
prompt += "\n Enter g for gathering Html files"
prompt += "\n Enter i for gathering image files"
prompt += "\n Enter p for parsing Html files"
prompt += "\n Enter s to save data into MySql Database (Please configure connections in Config file)"
prompt += "\n Enter a for all options above to run"
prompt += "\n Enter q to Quit"
prompt += "\n Text Here: "

active = True
while active:
    message = input(prompt)

    match message:
        case 'q':
            active = False
        case 'g':
            print('Gathering Html:\n')
            for dex in dexList:
                gatherHtmlFiles(dex)
        case 'i':
            print('Gathering Image files:\n')
            for i in imageList:
                gatherImageFiles(i)
        case 'p':
            print('Starting Html Parsing:\n')
            htmlparser.parseHtml(dexList, parent_dir)



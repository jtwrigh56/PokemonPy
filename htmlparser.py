from bs4 import BeautifulSoup
import json


def parseHtml(dex, path):
    for i in dex:
        for v in range(152):
            with open(f'{path}{i}/{v}.shtml', encoding='latin-1') as fp:
                stuff = BeautifulSoup(fp, 'html.parser')
                divs = stuff.findAll('div', {'align': 'center'})
                panelInfo = divs[0].findAll('td', {'class': 'fooinfo'})
                damnageTake = divs[0].findAll('td', {'class': 'footype'})

            # Creates Dictionary Information
                pokemon = dict()
                pokemon['Name'] = panelInfo[1].text
                pokemon['Number'] = panelInfo[3].text
                pokemon['Classification'] = panelInfo[4].text
                pokemon['Height'] = panelInfo[5].text
                pokemon['Weight'] = panelInfo[6].text
                pokemon['Capture Rate'] = panelInfo[7].text
                pokemon['Experience Growth'] = panelInfo[8].text
                pokemon['Base Stats'] = panelInfo[9].text
                pokemon['Normal Type'] = damnageTake[15].text
                pokemon['Fire Type'] = damnageTake[16].text
                pokemon['Water Type'] = damnageTake[17].text
                pokemon['Electric Type'] = damnageTake[18].text
                pokemon['Grass Type'] = damnageTake[19].text
                pokemon['Ice Type'] = damnageTake[20].text
                pokemon['Fighting Type'] = damnageTake[21].text
                pokemon['Poison Type'] = damnageTake[22].text
                pokemon['Ground Type'] = damnageTake[23].text
                pokemon['Flying Type'] = damnageTake[24].text
                pokemon['Psychic Type'] = damnageTake[25].text
                pokemon['Bug Type'] = damnageTake[26].text
                pokemon['Rock Type'] = damnageTake[27].text
                pokemon['Ghost Type'] = damnageTake[28].text
                pokemon['Dragon Type'] = damnageTake[29].text
                pokemon['Location'] = panelInfo[11].text

            # Creates list of Moves TODO
                moves = dict()


            print(pokemon)
            WriteToJson(pokemon)

def WriteToJson(p):
        filename = f'Json/{p["Name"]}.json'
        with open(filename, 'w') as convert_file:
            convert_file.write(json.dumps(p))

from PIL import Image, ImageDraw, ImageFont
import os

finalCertDirectory = "final_images"
template = 'teamname-template.jpg'
coordinates = [(130, 1400), (130, 3200)]
fontSize = 300

def draw_team_name_plate (teamName1, teamName2):
    fontFile = os.path.join(os.getcwd(), "lucida-grande-bold.ttf")
    saveFileName = teamName1 + '-' + teamName2 + '.jpg'
    print saveFileName

    #Set Font
    certFont = ImageFont.truetype(fontFile, fontSize)
    print certFont.getsize(teamName1)
    
    #open image
    newCertificate = Image.open(template)
    
    #Draw text on Image
    draw = ImageDraw.Draw(newCertificate)
    draw.text(coordinates[0], teamName1, font=certFont, fill=0)
    draw.text(coordinates[1], teamName2, font=certFont, fill=0)

    #Save File
    newCertificate.save(os.path.join(os.getcwd(), finalCertDirectory, saveFileName))


def main():
    os.system("rm -rf final_images/")
    os.system("mkdir final_images")
    noTeams = int(raw_input(''))
    try:
        for i in range(noTeams):
            teamName1 = str(raw_input(''))
            teamName2 = str(raw_input(''))
            img = draw_team_name_plate(teamName1, teamName2)
            i = i + 1
    except EOFError:
        print "End of file reached"

if __name__ == "__main__":
    main()

"""
    File to generate the InCTF certificates for
    first three places and for mentors.

    Input format
        <no of teams>
        <position of team>: 1, 2, 3
        <Name of team>
        <Name of college>
        <Name of mentor>
        <no of members>
        <member list>
        -
"""
import os
from PIL import Image, ImageDraw, ImageFont

def draw_mentor_certificate(mentorName,teamName, finalCertDirectory):
    #Create a directory to hold team certificates
 
    os.mkdir(os.path.join(finalCertDirectory, teamName))
    #Constants
    fontFile = os.path.join(os.getcwd(), "lucida-grande-bold.ttf")
    fontSize = 60
    templateFile = 'mentor.tif'
    fillColour = 'blue'
    saveFileName = 'Mentor.tif'
    print saveFileName

    #Set Font
    certFont = ImageFont.truetype(fontFile, fontSize)
    print certFont.getsize(mentorName)

    #open image
    newCertificate = Image.open(templateFile)

    #Draw text on Image
    draw = ImageDraw.Draw(newCertificate)
    draw.text((145, 650), mentorName,font=certFont,fill=fillColour)
    draw.text((145, 950), teamName,font=certFont,fill=fillColour)

    #Save File in CMYK mode
#    newCertificate.save(os.path.join(os.getcwd(), finalCertDirectory, teamName, saveFileName))

def draw_participant_certificate(participantName,teamName,collegeName, templateFile, coordinates, finalCertDirectory):
    #Constants
    fontFile = os.path.join(os.getcwd(), "lucida-grande-bold.ttf")
    fontSize = 80
    fillColour = 'black'
    saveFileName = teamName + '-' + participantName + '.tif'
    print saveFileName

    #Set Font
    certFont = ImageFont.truetype(fontFile, fontSize)
    print certFont.getsize(participantName)

    #open image
    newCertificate = Image.open(templateFile)
    #Draw text on Image
    draw = ImageDraw.Draw(newCertificate)
    draw.text(coordinates[0], participantName,font=certFont,fill=fillColour)
    draw.text(coordinates[1], teamName,font=certFont,fill=fillColour)
    #draw.text(coordinates[2], collegeName,font=certFont,fill=fillColour)

    #Save File
    newCertificate.save(os.path.join(os.getcwd(), finalCertDirectory, teamName, saveFileName))

def main():
    os.system("rm -rf final_certs/*")
    finalCertDirectory = "final_certs"
    template = {}
    template[1] = 'participation.tif'
    template[2] = 'participation.tif'
    template[3] = 'participation.tif'
    template[4] = 'participation.tif'
    template[5] = 'participation.tif'

    coordinates = {}
    coordinates[1] = [(145, 650), (145, 950)]
    coordinates[2] = [(145, 650), (145, 950)]
    coordinates[3] = [(145, 650), (145, 950)]
    coordinates[4] = [(145, 650), (145, 950)]
    coordinates[5] = [(145, 650), (145, 950)]
    noTeams = int(raw_input(''))
    for j in range(noTeams):
        position = int(raw_input(''))
        teamName = raw_input('')
        collegeName = raw_input('')
        mentorName = raw_input('')
        img = draw_mentor_certificate(mentorName, teamName, finalCertDirectory)
        print mentorName
        noMembers = int(raw_input(''))

        for i in range(noMembers):
            participantName = str(raw_input(''))
            img = draw_participant_certificate(participantName,
                    teamName,
                    collegeName,
                    template[position],
                    coordinates[position],
                    finalCertDirectory
                    )
        raw_input('')
if __name__ == "__main__":
    main()

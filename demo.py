__author__ = 'Priscila'
from xml.dom.minidom import *

print("Welcome to Reading Crime Registration")
menuChoice = input("Would you like to:\n[1] Report a crime\n[2] Access a file\n[0] Leave\n")

if menuChoice == "1":

    crime = Document()

    root = crime.createElement("root")
    crime.appendChild(root)                                                     # (1ST LEVEL) ROOT (PLACEHOLDER)
    code = crime.createElement("code")
    root.appendChild(code)                                                      # (2ND LEVEL) ROOT'S CHILD
    codeText = input("Digit the code of the crime: ")
    code.appendChild(crime.createTextNode(codeText))
    date = crime.createElement("date")
    root.appendChild(date)
    dateText = input("Digit the date of the crime: ")
    date.appendChild(crime.createTextNode(dateText))
    print("[About the informer]")
    informer = crime.createElement("informer")
    root.appendChild(informer)                                                  # (2ND LEVEL) ROOT'S CHILD
    informerName = crime.createElement("name")
    informer.appendChild(informerName)                                          # (3RD LEVEL) INFORMER'S CHILD
    informerNameText = input("Name: ")
    informerName.appendChild(crime.createTextNode(informerNameText))
    informerOccupation = crime.createElement("occupation")
    informer.appendChild(informerOccupation)                                    # (3RD LEVEL) INFORMER'S CHILD
    informerOccupationText = input("Occupation: ")
    informerOccupation.appendChild(crime.createTextNode(informerOccupationText))
    informerAddress = crime.createElement("address")
    informer.appendChild(informerAddress)                                       # (3RD LEVEL) INFORMER'S CHILD
    informerAddressText = input("Address: ")
    informerAddress.appendChild(crime.createTextNode(informerAddressText))
    informerPhone = crime.createElement("phone")
    informer.appendChild(informerPhone)                                         # (3RD LEVEL) INFORMER'S CHILD
    informerPhoneText = input("Phone: ")
    informerPhone.appendChild(crime.createTextNode(informerPhoneText))
    informerEmail = crime.createElement("email")
    informer.appendChild(informerEmail)                                         # (3RD LEVEL) INFORMER'S CHILD
    informerEmailText = input("E-mail: ")
    informerEmail.appendChild(crime.createTextNode(informerEmailText))
    informerVictim = crime.createElement("victim")
    informer.appendChild(informerVictim)
    ifVictim = input("Was the informer the victim?"
                     "\n[0] No\n[1] Yes\n")
    if ifVictim == "0":
        ifVictim = "false"
    else:
        ifVictim = "true"
    informerVictimText = ifVictim
    informerVictim.appendChild(crime.createTextNode(informerVictimText))
    root.appendChild(informer)
    description = crime.createElement("description")
    root.appendChild(description)                                           # (2ND LEVEL) ROOT'S CHILD
    descriptionText = input("Describe the crime: ")
    description.appendChild(crime.createTextNode(descriptionText))
    ifEvidence = input("Do you have any evidence(s)?"
                       "\n[0] No\n[1] Yes\n")
    count = 0
    while ifEvidence == "1":
        count = count + 1
        evidence = crime.createElement("evidence")
        root.appendChild(evidence)                                          # (2ND LEVEL) ROOT'S CHILD
        print("[Evidence #" + str(count) + "]")
        evidenceText = input("What's the evidence? ")
        evidence.appendChild(crime.createTextNode(evidenceText))
        # evidence.tagName = "evidence" + str(count)
        ifEvidence = input("Do you have any more evidences?"
                           "\n[0] No\n[1] Yes\n")
    typeCrime = input("Select the type of crime:"
                      "\n[1] Cybercrime\n[2] Theft\n[3] Homicide\n")
    if typeCrime == "1":
        root.tagName = "cybercrime"
        category = crime.createElement("category")
        categoryText = input("What's the category of this cybercrime? ")
        category.appendChild(crime.createTextNode(categoryText))
        root.appendChild(category)                                          # (2ND LEVEL) ROOT'S CHILD
    elif typeCrime == "2":
        root.tagName = "theft"
        place = crime.createElement("address")
        placeText = input("Where did the crime happen? ")
        place.appendChild(crime.createTextNode(placeText))
        root.appendChild(place)                                             # (2ND LEVEL) ROOT'S CHILD
        suspect = crime.createElement("suspect")
        suspectText = input("Description of the suspect: ")
        suspect.appendChild(crime.createTextNode(suspectText))
        root.appendChild(suspect)                                           # (2ND LEVEL) ROOT'S CHILD
        ifCar = input("Is the item stolen a vehicle?\n[0] No\n[1] Yes\n")
        if ifCar == "1":
            print("[About the vehicle]")
            vehicle = crime.createElement("vehicle")
            root.appendChild(vehicle)                                       # (2ND LEVEL) ROOT'S CHILD
            vehicleType = crime.createElement("type")
            vehicleTypeText = input("What kind of vehicle was it? ")
            vehicleType.appendChild(crime.createTextNode(vehicleTypeText))
            vehicle.appendChild(vehicleType)                                # (3RD LEVEL) VEHICLE'S CHILD
            if vehicleTypeText != "Bicycle":
                vehiclePlate = crime.createElement("plate")
                vehiclePlateText = input("Plate: ")
                vehiclePlate.appendChild(crime.createTextNode(vehiclePlateText))
                vehicle.appendChild(vehiclePlate)                           # (3RD LEVEL) VEHICLE'S CHILD
            vehicleColour = crime.createElement("colour")
            vehicleColourText = input("Colour: ")
            vehicleColour.appendChild(crime.createTextNode(vehicleColourText))
            vehicle.appendChild(vehicleColour)                                     # (3RD LEVEL) VEHICLE'S CHILD
            vehicleYear = crime.createElement("year")
            vehicleYearText = input("Year: ")
            vehicleYear.appendChild(crime.createTextNode(vehicleYearText))
            vehicle.appendChild(vehicleYear)                                       # (3RD LEVEL) VEHICLE'S CHILD
            vehicleModel = crime.createElement("model")
            vehicleModelText = input("Model: ")
            vehicleModel.appendChild(crime.createTextNode(vehicleModelText))
            vehicle.appendChild(vehicleModel)                                      # (3RD LEVEL) VEHICLE'S CHILD
        else:
            stolenProperty = crime.createElement("item")
            stolenPropertyText = input("Stolen item: ")
            stolenProperty.appendChild(crime.createTextNode(stolenPropertyText))
            root.appendChild(stolenProperty)                                # (2ND LEVEL) ROOT'S CHILD
        ifWitness = input("Do you have any witness(es)?\n[0] No\n[1] Yes\n")
        count = 0
        while ifWitness == "1":
            count = count + 1
            print("[About the witness #" + str(count) + "]")
            witness = crime.createElement("witness")
            root.appendChild(witness)                                       # (2ND LEVEL) ROOT'S CHILD
            witnessName = crime.createElement("name")
            witnessNameText = input("Name: ")
            witnessName.appendChild(crime.createTextNode(witnessNameText))
            witness.appendChild(witnessName)                                # (3RD LEVEL) WITNESS' CHILD
            witnessAddress = crime.createElement("address")
            witnessAddressText = input("Address: ")
            witnessAddress.appendChild(crime.createTextNode(witnessAddressText))
            witness.appendChild(witnessAddress)                             # (3RD LEVEL) WITNESS' CHILD
            witnessPhone = crime.createElement("phone")
            witnessPhoneText = input("Phone: ")
            witnessPhone.appendChild(crime.createTextNode(witnessPhoneText))
            witness.appendChild(witnessPhone)                               # (3RD LEVEL) WITNESS' CHILD
            witnessEmail = crime.createElement("email")
            witnessEmailText = input("E-mail: ")
            witnessEmail.appendChild(crime.createTextNode(witnessEmailText))
            witness.appendChild(witnessEmail)                               # (3RD LEVEL) WITNESS' CHILD
            ifWitness = input("Any other witness?\n[0] No\n[1] Yes\n")
    else:
        root.tagName = "homicide"                                         # (2ND LEVEL) ROOT'S CHILD
        place = crime.createElement("address")
        placeText = input("Where did the crime happen? ")
        place.appendChild(crime.createTextNode(placeText))
        root.appendChild(place)
        suspect = crime.createElement("suspect")
        suspectText = input("Description of the suspect: ")
        suspect.appendChild(crime.createTextNode(suspectText))
        root.appendChild(suspect)                                          # (2ND LEVEL) ROOT'S CHILD
        ifPrejudice = input("Was the crime a prejudice crime?"
                            "\n[0] No\n[1] Yes\n")
        if ifPrejudice == "1":
            prejudice = crime.createElement("prejudice")
            root.appendChild(prejudice)                                     # (2ND LEVEL) ROOT'S CHILD
            category = crime.createElement("category")
            categoryText = input("What kind of prejudice? ")
            category.appendChild(crime.createTextNode(categoryText))
            prejudice.appendChild(category)                                 # (3RD LEVEL) PREJUDICE'S CHILD
        weapon = crime.createElement("weapon")
        weaponText = input("What's the weapon of the crime? ")
        weapon.appendChild(crime.createTextNode(weaponText))
        root.appendChild(weapon)                                            # (2ND LEVEL) ROOT'S CHILD
        print("[About the victim]")
        victim = crime.createElement("victim")
        root.appendChild(victim)                                            # (2ND LEVEL) ROOT'S CHILD
        victimName = crime.createElement("name")
        victimNameText = input("Name: ")
        victimName.appendChild(crime.createTextNode(victimNameText))
        victim.appendChild(victimName)                                      # (3RD LEVEL) VICTIM'S CHILD
        victimAddress = crime.createElement("address")
        victimAddressText = input("Address: ")
        victimAddress.appendChild(crime.createTextNode(victimAddressText))
        victim.appendChild(victimAddress)                                   # (3RD LEVEL) VICTIM'S CHILD
        victimBirth = crime.createElement("date")
        victimBirthText = input("Birth date: ")
        victimBirth.appendChild(crime.createTextNode(victimBirthText))
        victim.appendChild(victimBirth)                                     # (3RD LEVEL) VICTIM'S CHILD
        victimOccupation = crime.createElement("occupation")
        victimOccupationText = input("Occupation: ")
        victimOccupation.appendChild(crime.createTextNode(victimOccupationText))
        victim.appendChild(victimOccupation)                                # (3RD LEVEL) VICTIM'S CHILD
        victimRelation = crime.createElement("relationship")
        victimRelationText = input("Relationship of the suspect and"
                                    " the victim: ")
        victimRelation.appendChild(crime.createTextNode(victimRelationText))
        victim.appendChild(victimRelation)                                  # (3RD LEVEL) VICTIM'S CHILD
        category = crime.createElement("category")
        categoryText = input("Category of the homicide: ")
        category.appendChild(crime.createTextNode(categoryText))
        root.appendChild(category)

    out = open("C:\\Users\\Priscila\\" + codeText + ".xml", "w")
    crime.writexml(out)
    out.flush()
    out.close()
    print("\nThank you. The crime was computed.\n")

    xml = xml.dom.minidom.parse("C:\\Users\\Priscila\\" + codeText + ".xml")    # PRETTY PRINT XML
    print(xml.toprettyxml())                                                    # PRETTY PRINT XML

elif menuChoice == "2":
    code = input("Digit the code of the crime: ")
    xml = xml.dom.minidom.parse("C:\\Users\\Priscila\\" + code + ".xml")
    crime = xml.childNodes[0]
    print()
    if crime.tagName == "cybercrime":
        print("[CYBERCRIME CASE #" + str(crime.childNodes[0].firstChild.nodeValue) + "]")
        print()
        print("Date: " + str(crime.childNodes[1].firstChild.nodeValue))
        print()
        print("About the informer:")
        print("\tName: " + str(crime.childNodes[2].childNodes[0].firstChild.nodeValue))
        print("\tOccupation: " + str(crime.childNodes[2].childNodes[1].firstChild.nodeValue))
        print("\tAddress: " + str(crime.childNodes[2].childNodes[2].firstChild.nodeValue))
        print("\tPhone: " + str(crime.childNodes[2].childNodes[3].firstChild.nodeValue))
        print("\tE-mail: " + str(crime.childNodes[2].childNodes[4].firstChild.nodeValue))
        if (str(crime.childNodes[2].childNodes[5].firstChild.nodeValue) == "true"):
            print("\tIs this person the victim? Yes.")
        else:
            print("\tIs this person the victim? No.")
        print()
        print("About the crime: ")
        print("\tDescription: " + str(crime.childNodes[3].firstChild.nodeValue))
        print("\tCategory: " + str(crime.childNodes[4].firstChild.nodeValue))
    elif crime.tagName == "theft":
        print("[THEFT CASE #" + str(crime.childNodes[0].firstChild.nodeValue) + "]")
        print()
        print("Date: " + str(crime.childNodes[1].firstChild.nodeValue))
        print()
        print("About the informer:")
        print("\tName: " + str(crime.childNodes[2].childNodes[0].firstChild.nodeValue))
        print("\tOccupation: " + str(crime.childNodes[2].childNodes[1].firstChild.nodeValue))
        print("\tAddress: " + str(crime.childNodes[2].childNodes[2].firstChild.nodeValue))
        print("\tPhone: " + str(crime.childNodes[2].childNodes[3].firstChild.nodeValue))
        print("\tE-mail: " + str(crime.childNodes[2].childNodes[4].firstChild.nodeValue))
        if (str(crime.childNodes[2].childNodes[5].firstChild.nodeValue) == "true"):
            print("\tIs this person the victim? Yes.")
        else:
            print("\tIs this person the victim? No.")
        print()
        print("Description of the crime: " + str(crime.childNodes[3].firstChild.nodeValue))
        print()
        evidenceCount = 0
        for n in crime.childNodes:
            if (n.tagName == "evidence"):
                evidenceCount = evidenceCount + 1
                print("Evidence #" + str(evidenceCount) + ": " + str(n.firstChild.nodeValue))
                print()
        print("About the crime:")
        print("\tPlace: " + str(crime.childNodes[4 + evidenceCount].firstChild.nodeValue))
        print("\tDescription of the suspect: " + str(crime.childNodes[5 + evidenceCount].firstChild.nodeValue))
        if (str(crime.childNodes[6 + evidenceCount].tagName) == "vehicle"):
            # print(str(crime.childNodes[6 + evidenceCount].childNodes))
            print("\tItem stolen: " + str(crime.childNodes[6 + evidenceCount].childNodes[0].firstChild.nodeValue))
            vehicleCount = 0
            if (str(crime.childNodes[6 + evidenceCount].childNodes[0].firstChild.nodeValue) != "Bicycle"):
                vehicleCount = vehicleCount + 1
                print("\t\tPlate: " + str(crime.childNodes[6 + evidenceCount].childNodes[vehicleCount].firstChild.nodeValue))
            print("\t\tColour: " + str(crime.childNodes[6 + evidenceCount].childNodes[1 + vehicleCount].firstChild.nodeValue))
            print("\t\tYear: " + str(crime.childNodes[6 + evidenceCount].childNodes[2 + vehicleCount].firstChild.nodeValue))
            print("\t\tModel: " + str(crime.childNodes[6 + evidenceCount].childNodes[3 + vehicleCount].firstChild.nodeValue))
        else:
            print("\tItem stolen: " + str(crime.childNodes[6 + evidenceCount].firstChild.nodeValue))
        print()
        witnessCount = 0
        for n in crime.childNodes:
            if (n.tagName == "witness"):
                witnessCount = witnessCount + 1
                print("Witness #" + str(witnessCount) + ": ")
                print("\tName: " + str(crime.childNodes[6 + evidenceCount + witnessCount].childNodes[0].firstChild.nodeValue))
                print("\tAddress: " + str(crime.childNodes[6 + evidenceCount + witnessCount].childNodes[1].firstChild.nodeValue))
                print("\tPhone: " + str(crime.childNodes[6 + evidenceCount + witnessCount].childNodes[2].firstChild.nodeValue))
                print("\tE-mail: " + str(crime.childNodes[6 + evidenceCount + witnessCount].childNodes[3].firstChild.nodeValue))
                print()
    elif crime.tagName == "homicide":
        print("[HOMICIDE CASE #" + str(crime.childNodes[0].firstChild.nodeValue) + "]")
        print()
        print("Date: " + str(crime.childNodes[1].firstChild.nodeValue))
        print()
        print("About the informer:")
        print("\tName: " + str(crime.childNodes[2].childNodes[0].firstChild.nodeValue))
        print("\tOccupation: " + str(crime.childNodes[2].childNodes[1].firstChild.nodeValue))
        print("\tAddress: " + str(crime.childNodes[2].childNodes[2].firstChild.nodeValue))
        print("\tPhone: " + str(crime.childNodes[2].childNodes[3].firstChild.nodeValue))
        print("\tE-mail: " + str(crime.childNodes[2].childNodes[4].firstChild.nodeValue))
        if (str(crime.childNodes[2].childNodes[5].firstChild.nodeValue) == "true"):
            print("\tIs this person the victim? Yes.")
        else:
            print("\tIs this person the victim? No.")
        print()
        print("About the crime:")
        print("\tDescription: " + str(crime.childNodes[3].firstChild.nodeValue))
        print("\tPlace: " + str(crime.childNodes[4].firstChild.nodeValue))
        print("\tDescription of the suspect: " + str(crime.childNodes[5].firstChild.nodeValue))
        ifPrejudice = 0
        if (str(crime.childNodes[6].tagName) == "prejudice"):
            print()
            print("\t[Prejudice crime]")
            print("\tPrejudice: " + str(crime.childNodes[6].childNodes[0].firstChild.nodeValue))
            print()
            ifPrejudice = ifPrejudice + 1
        print("\tWeapon of the crime: " + str(crime.childNodes[6 + ifPrejudice].firstChild.nodeValue))
        print()
        print("\tAbout the victim:")
        print("\t\tName: " + str(crime.childNodes[7 + ifPrejudice].childNodes[0].firstChild.nodeValue))
        print("\t\tAddress: " + str(crime.childNodes[7 + ifPrejudice].childNodes[1].firstChild.nodeValue))
        print("\t\tBirth date: " + str(crime.childNodes[7 + ifPrejudice].childNodes[2].firstChild.nodeValue))
        print("\t\tOccupation: " + str(crime.childNodes[7 + ifPrejudice].childNodes[3].firstChild.nodeValue))
        print("\t\tRelationship with the suspect: "
              + str(crime.childNodes[7 + ifPrejudice].childNodes[4].firstChild.nodeValue))
        print()
        print("\tCategory: " + str(crime.childNodes[8 + ifPrejudice].firstChild.nodeValue))

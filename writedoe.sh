#Have user input the doe# of the device
read -p "Please input the DOE# of the device: " DOE1
read -p "Please input the DOE# of the device: " DOE2

#Repeats the what the user typed into the command line
echo "You typed this" $DOE1
echo "You typed this" $DOE2

	if [[ $DOE1 -eq $DOE2 ]]; 
		then 
		echo "Your DOE#'s match. The system will now write this value to a plist."; 
	fi

#Command to using Jamf binary to set the ARD Field & Creates a Plist file inside Library folder
#this enables bigfix to read the location, instead of relying on the ARD Fields. Users can still 
#modify these fields. Reading a plist would be a safer condition. 

jamf setARDFields -target / -1 "$DOE1"
defaults write /Library/Preferences/com.lbl.information.plist DOE# "$DOE1"

#Repeats the what the user typed into the command line
read -p "Please input the Orgcode of the user: " ORG1
read -p "Please input the Orgcode of the user: " ORG2

#Repeats the what the user typed into the command line
echo "You typed this" $ORG1
echo "You typed this" $ORG2

#Command to using Jamf binary to set the ARD Field & Creates a Plist file inside Library folder
#this enables bigfix to read the location, instead of relying on the ARD Fields. Users can still 
#modify these fields. Reading a plist would be a safer condition. 

jamf setARDFields -target / -2 "$ORG1"
defaults write /Library/Preferences/com.lbl.information.plist Orgcode "$ORG1" 

#Repeats the what the user typed into the command line
read -p "Please input the Phone Number of the user: " PN1
read -p "Please input the Phone Number of the user: " PN2

#Repeats the what the user typed into the command line
echo "You typed this" $PN1
echo "You typed this" $PN2

#Command to using Jamf binary to set the ARD Field & Creates a Plist file inside Library folder
#this enables bigfix to read the location, instead of relying on the ARD Fields. Users can still 
#modify these fields. Reading a plist would be a safer condition. 

jamf setARDFields -target / -3 "$PN1"
defaults write /Library/Preferences/com.lbl.information.plist Phone\ Number "$PN1"

#Repeats the what the user typed into the command line
read -p "Please input the Email Address of the user: " EM1
read -p "Please input the Email Address of the user: " EM2

#Repeats the what the user typed into the command line
echo "You typed this" $EM1
echo "You typed this" $EM2

#Command to using Jamf binary to set the ARD Field & Creates a Plist file inside Library folder
#this enables bigfix to read the location, instead of relying on the ARD Fields. Users can still 
#modify these fields. Reading a plist would be a safer condition. 

jamf setARDFields -target / -4 "$EM1"
defaults write /Library/Preferences/com.lbl.information.plist Email "$EM1" 
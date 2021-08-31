#Python code to illustrate parsing of XML files
# importing the required modules
import plistlib as plist

def parseXML(xmlfile):
	with open(xmlfile, 'rb') as fp:
		return plist.load(fp, fmt=plist.FMT_XML)

def main():
	with open("convertedContacts.vcf", "w") as cfp:
		contactsData = parseXML('Contacts.list')
		for item in contactsData["Contacts"] :
			if item["AccountType"] != "com.skype.m2":
				contact = "BEGIN:VCARD\r\n"
				contact = contact + "VERSION:2.1\r\n"
				contact = contact + "FN:"+item["FullName"]+"\r\n"
				if "FamilyName" in item :
					contact = contact + "N:"+item["FamilyName"]+";"
					if "GivenName" in item:
						contact = contact + item["GivenName"]+";;\r\n"
					else:
						contact = contact + ";;;\r\n"
				else:
					if "GivenName" in item:
						contact = contact + "N:"+";"+item["GivenName"]+";;\r\n"
					else:
						contact = contact +"N:;;;;\r\n"
				if "Emails" in item:
					for email in item["Emails"]:
						contact = contact + "EMAIL:" + email["Value"] + "\r\n"
				if "PhoneNumbers" in item:
					for number in item["PhoneNumbers"]:
						contact = contact + "TEL;CELL:" + number["Value"] + "\r\n"
				if "PictureData" in item:
					contact = contact + "PHOTO;ENCODING=BASE64;JPEG:"+item["PictureData"]+"\r\n"
				contact = contact + "END:VCARD\r\n"
				cfp.write(contact)

if __name__ == "__main__":

	# calling main function
	main()

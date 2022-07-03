import os, sys, argparse
from email import generator
from email.message import EmailMessage
from os.path import isfile, join
from os import listdir

parser = argparse.ArgumentParser(description="Create phishing email",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--fromaddress", help="Sender email address")
parser.add_argument("-t", "--toaddress",  help="Recipient email address")
parser.add_argument("-s", "--subject", help="Subject of the phishing email")
parser.add_argument("-o", "--output", help="File location to write email to ending with .eml")
args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

files = [f for f in listdir("attachments") if isfile(join("attachments", f))]

def create_message():
    msg = EmailMessage()
    msg["To"] = args.toaddress
    msg["From"] = args.fromaddress
    msg["Subject"] = args.subject

    with open("body.txt") as fp:
        msg.set_content(fp.read())

    for file in files:
        with open("attachments" + "/" + file, 'rb') as fp:
            data = fp.read()
        msg.add_attachment(data, maintype='application',
                                 subtype="msword")

    return msg

def write_eml_file(msg):
    filename = args.output

    with open(filename, 'w') as file:
        emlGenerator = generator.Generator(file)
        emlGenerator.flatten(msg)

def main():
    msg = create_message()
    write_eml_file(msg)

if __name__ == "__main__":
    main()

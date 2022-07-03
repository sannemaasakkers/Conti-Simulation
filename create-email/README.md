# create-email

This small tools generates an .eml file which can be used during an adversary simulation. In this case you don't need to setup a mailserver between the victim and attacker VM: just open the file in the victim's Outlook application.

## Usage

```bash
python3 create.py -f [email address of the attacker] -t [email address of the recipient] -s [subject of the email] -o [output file to write]
```

The body.txt file contains the content of the email to generate. In the attachments folder you could place the attachments you would like to add to the email.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

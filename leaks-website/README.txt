# leaks-website

This small tools sets up a Conti leaks website given the stolen files in an earlier phase of the adversary simulation demo.
## Usage

```bash
python3 serve.py -n [name of the hacked organisation] -d [directory of the stolen files to include on the website] -s [amount of the stolen files to display on the website]
```

The leaked page will be served on localhost:8000. If you want to make it more realistic, change your hosts file for example to match the readme-file generate in the create-email step.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

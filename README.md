# SOEN6611MeasurementProject

#Project Structure  
The main folder is called Project, which contains five folders:    
* CommonCollections.    
* Common Configuration.  
* CommonDigester. 
* CommonLang.  
* Metrics5&6.py
* ClassLevelCorrelation.py 

   
Each Folders of project contains 'Metric 1,2,4', Metric3, Metric5, Metric6 results obtained from various tools.Where in Metric3  contains metrics for only one version where as rest all the folder contains metrics for 5 versions of each project 
Each folder also contains Correlation.csv which are the results of correlation between different metrics respectively
    
    
Requirements for running the Scripts and tools 

1. Jacoco Maven Plugin:-  
   * This Plugin is used to collect data for Metric 1,2 and 4.
   * Steps for generating metrics:-  
      1. Insert the plugin in pom.xml
      2. Run Maven Clean Goal and test goal.
   * We get the reports in jacoco-ut folder which is currently present in the above folder structure in each project/version sub-folders

2. PiTest Plugin
    * Steps for generating metrics:-  
      1. Insert the plugin in pom.xml
      2. Run Maven Clean Goal and test goal.
  
    We get the reports in a Pit-test reports folder after successfully running pit-test plugin.  
    The output is in the form of index.html format for desired result 

3. Code Churn  
  Download and install cloc  
  
  #### Command used :  
    cloc --diff “version1Code” “Version2Code” --out=version.csv  
    
  This creates a file .csv files that contains the count of files ,blank lines, commented lines and lines of code that are same, added , modified and removed between two versions of projects
  Code churn =linesadded+modified+removed


4. SonarQube/SonarLint
 * Steps for generating metrics:-  
      1. Insert the plugin in pom.xml
      2. Run Maven Clean Goal and test goal with goal  “mvn sonar: sonar Dsonar.projectKey=”KeyValue”Dsonar.host.url=http://localhost:9000 Dsonar.login=admin Dsonar.password=admin”.
  
  The results can then be seen at localhost:9000
  The code smell value can then be used for further correlation.


After running each above given tools we will have metrics for each project.After this first extract the mutation score details from index.html file from metrics3 using Scrapper.java to need to run this file in java environment,here all we need to do is just supply the filepath of index.html it will generate the .csv file in the same directory of the file path supplied

Thus after generating the pit file we need run the python script i.e ClassLevelCorrelation.py this will prompt the user to enter the two file paths where first file path would be the jacoco.csv file path in metrics 1,2&4 folder and second file path would have file path of pit.csv in metrics3 folder and after runnning the script there would be correlation.csv generated in the project folder.

For finding the version level correlation we use python script i.e metrics5&6.py, After running the script,it prompts the user to enter the two file paths where first file path would be the 1,2&6.csv file path in project folder and second file path would have file path of 5&6.csv  this will compute the correlation results and would append them in correlation.csv file

Thus we would have all the correlation results in correlation.csv file


## Team Details  

  - PULKIT WADHWA       || 40082832 || pulkitwadhwa95@gmail.com
  - ZINNIA RANA         || 40074965 || zinnia.rana1@gmail.com
  - BIRJOT SINGH        || 40096078 || birjot1996@gmail.com
  - JATIN RUPEJA        || 40084383 || atul12nov@gmail.com
  - Sahil Savaliya      || 40080380 || sahiladg@gmail.com


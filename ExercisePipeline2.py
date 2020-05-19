#!/usr/bin/env python
# coding: utf-8

# In[2]:


properties([
    parameters([
        string (name:'name',
                defaultValue:'Raj',
                description:'Employee Name'),
        string (name:'age',
                defaultValue:'24',
                description: 'Employee Age'),
        string (name:'salary',
                defaultValue:'100000',
                description:'Employee Salary')
              ])
          ])   

def remote = [:]
remote.name = '10.110.3.222'
remote.host = '10.110.3.222'
remote.user = 'root'
remote.password = 'Accenture.1'
remote.allowAnyHosts = true

pipeline{
    agent any
    stages{
        stage('Checking the version of Python'){
             steps{
                 sh 'python -- version'                
            }
        }    
        stage('Converting the file to executable'){
            steps{
                sh 'chmod u+x Exercise_Pipeline.py'
                sh 'python Exercise_Pipeline.py'
            }
        }           
    }
}


# In[ ]:





```groovy
        stage('Terraform Apply') {
            steps {
                input message: 'Plan successful. Approve creation of AWS infrastructure?'
                bat 'terraform apply -input=false -auto-approve tfplan'
            }
        }
```
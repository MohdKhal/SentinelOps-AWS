terraform {
  backend "s3" {
    bucket         = "sentinelops-tfstate-395616638064"
    key            = "networking/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "sentinelops-tf-locks"
    encrypt        = true
  }
}

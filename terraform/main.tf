terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }

    aws = {
      source  = "hashicorp/aws"
    }
  }
}

provider "local" {}

provider "aws" {
  region = "ap-south-1"
}

resource "local_file" "hello" {
  filename = "${path.module}/hello.txt"
  content  = "Terraform is working!"
}

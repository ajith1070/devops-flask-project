# Terraform Fundamentals

## Overview

This project demonstrates basic Terraform Infrastructure as Code (IaC) concepts using the local file provider.

## What I Practised

- Terraform configuration and resource blocks
- Provider configuration
- Using `path.module` in resource paths
- Creating a local file using Terraform
- Understanding Terraform initialization and execution

## Resource

The `local_file` resource creates `hello.txt` containing:

`Terraform is working!`

## Commands

```bash
terraform init
terraform validate
terraform plan
terraform apply
terraform destroy

variable "vpc_name" {
  type    = string
  default = "sentinelops-vpc"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "public_subnet_1" {
  type    = string
  default = "10.0.1.0/24"
}

variable "public_subnet_2" {
  type    = string
  default = "10.0.2.0/24"
}

variable "private_subnet_1" {
  type    = string
  default = "10.0.11.0/24"
}

variable "private_subnet_2" {
  type    = string
  default = "10.0.12.0/24"
}

variable "cluster_name" {
  default = "sentinelops-eks"
}

variable "cluster_version" {
  default = "1.31"
}

variable "subnet_ids" {
  type = list(string)
}

variable "vpc_id" {
  type = string
}



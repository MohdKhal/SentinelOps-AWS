resource "aws_ecr_repository" "user_service" {
  name = "user-service"
}

resource "aws_ecr_repository" "policy_service" {
  name = "policy-service"
}

resource "aws_ecr_repository" "quote_service" {
  name = "quote-service"
}

resource "aws_ecr_repository" "payment_service" {
  name = "payment-service"
}

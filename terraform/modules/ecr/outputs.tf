output "user_repo_url" {
  value = aws_ecr_repository.user_service.repository_url
}

output "policy_repo_url" {
  value = aws_ecr_repository.policy_service.repository_url
}

output "quote_repo_url" {
  value = aws_ecr_repository.quote_service.repository_url
}

output "payment_repo_url" {
  value = aws_ecr_repository.payment_service.repository_url
}

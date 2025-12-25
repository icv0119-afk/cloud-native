output "public_ip" {
  description = "EC2 實例的公有 IP"
  value       = aws_instance.app_server.public_ip
}

output "ssh_command" {
  description = "連線指令"
  value       = "ssh -i devops-key.pem ec2-user@${aws_instance.app_server.public_ip}"
}
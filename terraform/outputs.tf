output "public_ip" {
  description = "EC2 實例的公有 IP (請將此填入 GitHub Secrets 的 EC2_HOST)"
  value       = aws_instance.app_server.public_ip
}

output "ssh_command" {
  description = "連線指令"
  value       = "ssh -i vic-key.pem ec2-user@${aws_instance.app_server.public_ip}"
}
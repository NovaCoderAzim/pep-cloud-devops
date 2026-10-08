output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "subnet_1_id" {
  description = "Subnet 1 ID"
  value       = aws_subnet.subnet_1.id
}

output "subnet_2_id" {
  description = "Subnet 2 ID"
  value       = aws_subnet.subnet_2.id
}

output "ec2_1_public_ip" {
  description = "Public IP of EC2 instance 1"
  value       = aws_instance.ec2_1.public_ip
}

output "ec2_2_public_ip" {
  description = "Public IP of EC2 instance 2"
  value       = aws_instance.ec2_2.public_ip
}

output "ec2_1_public_dns" {
  description = "Public DNS of EC2 instance 1"
  value       = aws_instance.ec2_1.public_dns
}

output "ec2_2_public_dns" {
  description = "Public DNS of EC2 instance 2"
  value       = aws_instance.ec2_2.public_dns
}
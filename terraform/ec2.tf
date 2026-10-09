data "aws_ami" "ubuntu" {
  most_recent = true

  owners = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
}

resource "aws_security_group" "ec2" {
  name        = "pep-devops-ec2-sg"
  description = "Security group for PEP DevOps EC2 instances"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["14.195.132.38/32"]
  }

  ingress {
    description = "Application"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["14.195.132.38/32"]
  }

  egress {
    description = "Allow outbound internet"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["14.195.132.38/32"]
  }

  tags = {
    Name    = "pep-devops-ec2-sg"
    Project = "pep-cloud-devops"
  }


}
resource "aws_key_pair" "pep_devops" {
  key_name   = "pep-devops-key"
  public_key = file("${path.module}/pep-devops-key.pub")
}

resource "aws_instance" "ec2_1" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.subnet_1.id
  vpc_security_group_ids      = [aws_security_group.ec2.id]
  associate_public_ip_address = true
  key_name                    = aws_key_pair.pep_devops.key_name

  user_data = file("${path.module}/user_data.sh")

  credit_specification {
    cpu_credits = "standard"
  }

  root_block_device {
    volume_size = 8
    volume_type = "gp3"
  }

  tags = {
    Name    = "pep-devops-ec2-1"
    Project = "pep-cloud-devops"
  }
}

resource "aws_instance" "ec2_2" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.subnet_2.id
  vpc_security_group_ids      = [aws_security_group.ec2.id]
  associate_public_ip_address = true
  key_name                    = aws_key_pair.pep_devops.key_name

  user_data = file("${path.module}/user_data.sh")

  credit_specification {
    cpu_credits = "standard"
  }

  root_block_device {
    volume_size = 8
    volume_type = "gp3"
  }

  tags = {
    Name    = "pep-devops-ec2-2"
    Project = "pep-cloud-devops"
  }
}
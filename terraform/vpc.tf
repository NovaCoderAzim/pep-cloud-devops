resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name    = "pep-devops-vpc"
    Project = "pep-cloud-devops"
  }
}

resource "aws_subnet" "subnet_1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.subnet_1_cidr
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name    = "pep-devops-subnet-1"
    Project = "pep-cloud-devops"
  }
}

resource "aws_subnet" "subnet_2" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.subnet_2_cidr
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true

  tags = {
    Name    = "pep-devops-subnet-2"
    Project = "pep-cloud-devops"
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name    = "pep-devops-igw"
    Project = "pep-cloud-devops"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name    = "pep-devops-public-route"
    Project = "pep-cloud-devops"
  }
}

resource "aws_route_table_association" "subnet_1" {
  subnet_id      = aws_subnet.subnet_1.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "subnet_2" {
  subnet_id      = aws_subnet.subnet_2.id
  route_table_id = aws_route_table.public.id
}
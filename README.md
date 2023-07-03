# Saber Interactive Build System

## Table of Contents

- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)

## Getting Started

APE was developed in python 3.9.

Take this repository and install it in the directory you need using the command.

```git clone https://github.com/Caxaro4ekPixel/SaberInteractiveBuildSystem.git```

### Installation

To install all the necessary libraries, write the command 

```pip install -r requirements.txt```

## Usage

To run, you need to run "hosting". I used unicorn for development.

```pip install unicorn```

```uvicorn main:app --host 127.0.0.1 --port 8000 --reload``` to run in test mode

You can use any other method to launch.

For testing and clarity, you can use Postman (import of the collection is attached)
# CAN Bus Communication Simulation using Python, SocketCAN, and DBC

## Overview

This project simulates a two-node vehicle communication network using Linux SocketCAN virtual interfaces and Python. The system demonstrates how CAN messages are transmitted between a Sensor Node and an ECU Node using standardized CAN message definitions stored in a DBC file.

The project was developed to understand CAN Bus fundamentals, message transmission, signal encoding/decoding, and automotive communication architecture without requiring physical CAN hardware.

## Features

* Simulated CAN Bus communication using SocketCAN (`vcan0`)
* Developed Sender and Receiver nodes using Python
* Defined CAN message structure using a DBC file
* Encoded and decoded CAN signals using `cantools`
* Simulated vehicle parameters such as Speed and Temperature
* Generated ECU warnings based on received sensor values
* Demonstrated automotive-style sensor-to-ECU communication

## Technologies Used

* Python
* SocketCAN
* python-can
* cantools
* Linux (Ubuntu)
* DBC (CAN Database)

## Project Architecture

Sensor Node → CAN Bus (vcan0) → ECU Node

### Sensor Node

* Generates Speed and Temperature values
* Encodes data according to DBC definitions
* Sends CAN messages with a predefined CAN ID

### ECU Node

* Receives CAN messages
* Decodes signals using the DBC file
* Displays vehicle parameters
* Generates warning messages when limits are exceeded

## CAN Message Definition

| Signal | Description              |
| ------ | ------------------------ |
| Speed  | Vehicle speed (km/h)     |
| Temp   | Vehicle temperature (°C) |

CAN ID: `100`

## Learning Outcomes

* Understanding of CAN Bus communication
* Experience with SocketCAN virtual interfaces
* CAN message transmission and reception using Python
* DBC-based signal encoding and decoding
* Automotive communication architecture fundamentals
* Linux-based embedded development workflow

## Future Improvements

* Add Fuel Level and RPM signals
* Implement a Dashboard Node
* Add CAN traffic logging
* Support multiple CAN message IDs
* Develop a real-time GUI for monitoring vehicle parameters

## Author

Harish

Automotive Communication and Embedded Systems Learning Project

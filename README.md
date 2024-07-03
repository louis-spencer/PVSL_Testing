# Welcome to the Pressure Vessel Slow Leak (PVSL) Testing Repo
This is the respository that will be used for storing all of the software and scripts for the automated PV testing.
The project integrates multiple different aspects, including computer and electrical engineering, software development,
PCB design, and some mechanics.

## Goal
The goal for this project is to create a system that can automatically detect leaks in naval pressure vessels. This is
accomplished by using an absolute pressure transducer and a resistance temperature detector (RTD) to determine whether
pressure will fluctuate during a given time period.

The code and software on this repository will be run on a Raspberry Pi 5 and will log the varying temperature and
pressure readings.

## TODO
- [ ] Acquire sensors
- [ ] Calibrate sensors
- [ ] Design receivers to turn current mode to voltage
- [ ] Create (low pass) filters to filter higher frequency noise
- [ ] Create board for sensors, ADC, filters, amplifiers, etc.
- [ ] Finish frontend app with QtDesigner
- [x] Add save file/path functionality for data to CSV
  - [ ] Make it decent :)
- [ ] Create dialog when test time set to custom  
- [ ] Add backend files to pull data from sensors from ADC on Raspberry Pi



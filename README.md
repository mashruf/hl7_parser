# HL7 SIU^S12 Parser

This Python module will parses an HL7 SIU S12 message from disk and converts it into a normalized JSON representation of an appointment. 

User will get error message for any missing segment among MSH, SCH, PID and PV1. It will also provide error message if the message type is not SIU S12. The final JSON file will be created with appropiate data only if the message have all the required segment and its a valid message type.
 

## Project structure

```
project-root
|_ main.py
|_ hl7_parser
   |_ check_message.py
   |_ produce_data.py
|_ sample_data
   |_ sample.hl7
   |_ sample_missing_seg.hl7
   |_ sample_invalid_msg.hl7
|_ test
   |_ test_check_message.py
   |_ test_produce_data.py
```

## Requirements

- Python 3.8+
- PyTest

## Installation

- Clone or download the folder
- To run the test, install `pytest`
- To install Pytest run following command

```
pip install pytest

```

## Sample file

- Sample file will be found in `sample_data` folder.
- `sample.hl7` was used to read valid data from the disk.
- `sample_missing_seg.hl7` was used to read data with missing segment.
- `sample_invalid_msg.hl7` was used to read data with invalid message type.

## Helper function

- The helper functions will be found in `hl7_parser` folder.
- `checkSegments()` function from `check_message.py` will check whether the sample message has all the required segment or not.  
- `checkMessageType` function from `check_message.py` will check whether the message has the correct message type or not.
- `indexOfSegment()` from `produce_data.py` was used to extract the indexes of SCH, PID and PV1 so that we can use their indexes dynamically to extract required data from the message.
- `extractSchedule()` from `produce_data.py` was used to extract `appointment_id`, `appointment_reason`, `iso_time` from SCH.
- `extractPatientInfo()` from `produce_data.py` was used to extract `patient_id`, `patient_first_name`, `patient_last_name`, `date_of_birth`, `patient_gender` from PID.
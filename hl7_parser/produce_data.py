from .check_message import checkMessageType
from datetime import datetime

'''
will find the index of SCH, PID and PV1 from the list of splitted message
'''
def indexOfSegment(message): 
    
    segments = checkMessageType(message)

    index_SCH = None
    index_PID = None
    index_PV1 = None

    if isinstance(segments, list):
    
        for ind, val in enumerate(segments):    

            if (val[0] == "SCH"):
                index_SCH = ind

            if(val[0] == "PID"):
                index_PID = ind

            if(val[0] == "PV1"):
                index_PV1 = ind
    
    else:
        return "Required HL7 segment is missing!"
    
    return index_SCH, index_PID, index_PV1



'''
will extrct the appointment id, appoinment reason and appointment time from SCH
'''
def extractSchedule(message):

    index = indexOfSegment(message)
    msg_body = checkMessageType(message)

    if isinstance(msg_body, list):
        
        appointment_id = msg_body[index[0]][1].split("^")[0]
        appointment_reason = msg_body[index[0]][4]
        appointment_time = datetime.strptime(msg_body[index[0]][6], "%Y%m%d%H%M%S")
        iso_time = datetime.isoformat(appointment_time)

    else:
        appointment_id = appointment_reason =  iso_time = None
    
    return appointment_id, appointment_reason, iso_time


'''
will extract patiend id, patient name,
patient date of birth, patient gender from PID
'''
def extractPatientInfo(message):

    index = indexOfSegment(message)
    msg_body = checkMessageType(message)

    if isinstance(msg_body, list):
    
        patient_id = msg_body[index[1]][3].split("^")[0]
        patient_first_name = msg_body[index[1]][5].split("^")[1]
        patient_last_name = msg_body[index[1]][5].split("^")[0]
        patient_DOB = datetime.strptime(msg_body[index[1]][7], "%Y%m%d")
        date_of_birth = patient_DOB.date().isoformat()
        patient_gender = msg_body[index[1]][8]

    else:
        patient_id = patient_first_name = patient_last_name = date_of_birth = patient_gender = None

    return patient_id, patient_first_name, patient_last_name, date_of_birth, patient_gender



'''
will extract provider id, provider name, provider location
from PV1
'''
def extractProviderInfo(message):
    index = indexOfSegment(message)
    msg_body = checkMessageType(message)

    if isinstance(msg_body, list):
    
        provider_id = msg_body[index[2]][6].split("^")[0]
        provider_name = f'Dr. {msg_body[index[2]][6].split("^")[1]}'
        clininc_name = msg_body[index[2]][3].split("^")[0]
        room_no = msg_body[index[2]][3].split("^")[1]
        provider_location = f'{clininc_name} Room {room_no}'

    else:
        provider_id = provider_name = provider_location = None

    return provider_id, provider_name, provider_location


# print(extractProviderInfo('./sample_data/sample.hl7'))



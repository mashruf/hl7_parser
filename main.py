import json
import hl7_parser.produce_data as produce_data

sch = produce_data.extractSchedule('./sample_data/sample.hl7')
pid = produce_data.extractPatientInfo('./sample_data/sample.hl7')
pv1 = produce_data.extractProviderInfo('./sample_data/sample.hl7')


details = {
   "appointment_id": sch[0],
    "appointment_datetime": sch[2],
    "patient":{
    "id": pid[0],
    "first_name": pid[1],
    "last_name": pid[2],
    "dob": pid[3],
    "gender": pid[4]
    },
    "provider":{
    "id": pv1[0],
    "name": pv1[2]
    },
    "location": pv1[2],
    "reason": sch[1]    
}


print(json.dumps(details))
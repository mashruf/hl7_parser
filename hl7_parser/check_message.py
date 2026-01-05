
'''
will check the message has required segments and
split the message based on new line and retun a list
'''
def checkSegments(message):  
    
    # open the hl7 file
    file = open(message, 'r')

    # read message from the hl7 file
    msg = file.read()

    # checking all the required segments present
    if "MSH|" in msg and "SCH|" in msg and "PID|" in msg and "PV1|" in msg: 
        return msg.splitlines()
    
    else:
        return "Required HL7 segment is missing!"
        


'''
1. will split every list element and create a list of list and return it
2. will check whether the message header has the correct message type
'''
def checkMessageType(message):

    separate_segment = [] # will store the splitted message body
    
    segments = checkSegments(message)

    if isinstance(segments, list):
         
        for seg in segments: # splitting the message
            separate_segment.append(seg.split("|"))

        if separate_segment[0][8] == "SIU^S12": # checking message type is SIU^S12
            return separate_segment
        
        else:
            return "Message type is not SIU^S12"
        
    else:
        return "Required HL7 segment is missing!"

    
    

# segments = checkSegments('./sample_data/sample.hl7')
# print(segments)
# print(checkMessageType('./sample_data/sample.hl7'))

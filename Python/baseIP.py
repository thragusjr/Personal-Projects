# author: Ethan Page
# This routine takes two strings as arguments:
#   ip_addr - any IP address (e.g. "1.2.3.4")
#   subnet_mask - a valid IPv4 subnet mask (e.g. "255.255.255.0")
#
#   It returns a string that represents the base IP address of that
#   network.  (e.g. in the example above it would return "1.2.3.0")
#

def network_base_addr(ip_addr, subnet_mask):
    ip = ip_addr.split(".")
    sub = subnet_mask.split(".")

    temp2 = 0
    temp3 = 0

    tempA = ''
    tempB = ''

    bitList = []
    subList = []
    cadList = []

    for i in range(0, len(ip)):
        temp2 = ip[i]
        tempA = bin(int(temp2))
        bitList.insert(i, tempA[2:].zfill(8))

    bitString = ''.join(bitList)
    binBitList = list(bitString)

    for j in range(0, len(sub)):
        temp3 = sub[j]
        tempB = bin(int(temp3))
        subList.insert(j, tempB[2:].zfill(8))

    subString = ''.join(subList)
    binSubList = list(subString)

    for a in range(0, len(binSubList)):
        if binSubList[a] == '1' and binBitList[a] == '1':
            cadList.insert(a, '1')
        else:
            cadList.insert(a, '0')

    cadList = ''.join(cadList)

    tempResult = []
    result = []

    for f in range(0, len(cadList), 8):
        tempResult.append(int(cadList[f:f + 8], 2))

    for r in range(0, len(tempResult)):
        result.append(str(tempResult[r]))

    delimiter = '.'
    finalResult = delimiter.join(result)

    return finalResult

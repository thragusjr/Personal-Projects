#
# Author: Ethan Page
# Version : 4/23/2023
#
# CSV_Server is a program that creates a TCP socket that listens for HTTP requests
# from a .csv file using =WEBSERVICE functions. The program looks for town information
# associated with zip codes provided in the request, and returns that information to
# the client (file).
#
# The user of this program can choose to take in user input as variables for file paths
# and host if they prefer. CSV_Server can also be configured to attempt to gather host
# information automatically from the machine from the program is running.
#

import socket
import csv
import re


def csv_zip_server():

    path = 'C:\\Users\\Documents\\zipcodes.txt'

    # Uncomment the following line to use user input for data source if preferred
    # inputPath = input("Please enter the full file path for zip code data: ")

    # hardHost = 192.168.1.4

    # Set information for host and listening port using socket functions
    # hostName = socket.gethostname()
    # servIP = socket.gethostbyname(hostName)

    servIP = '127.0.0.1'

    # Uncomment next two lines for user specified hostname and IP
    # hostName = input('Please enter your computer's hostname')
    # servIP = input('Please enter your computer's IP address')

    servPort = 8080

    # Set address family and socket type
    servSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to host and port
    servSocket.bind((servIP, servPort))

    # Tell socket to listen for connections, with queue limit of 5 connections
    servSocket.listen(5)

    # Print message indicating that the server is waiting for a servConn
    print(f"Waiting for connection on " + servIP + ":" + str(servPort))

    # "Loop" to handle data when connection has been received
    while True:
        # Accept Connection
        servConn, address = servSocket.accept()

        # Print indicator when connection is made. Reflect address information of client to show origin.
        print("Connection received from " + str(address[0]) + " : " + str(address[1]))

        # Initialize dictionary to store zip code and town information from text file
        zipDict = {}

        # Open and handle text file from user specified (or hardcoded) path
        with open(path, 'r') as file:
            for line in file:
                # Separate town and zip code from request using a delimiter of =, then insert lists into dictionary
                zipCode, zipTown = line.strip().split('=')
                zipDict[zipCode] = zipTown

        # Assign received data to variable 'data', with byte read limit = 1024
        data = servConn.recv(1024).decode()

        # Create list from GET request using '/' delim
        zipList = data.split('/')

        # Pull zip code information from resulting list index
        tempZip = zipList[2]

        # Regular expression to extract zip from request. Match on 5 digits, or 4 with leading digit
        match = re.search(r'/zip/(\d{5}|\d{1,4})', data)

        # Add conditions for variable assignments if match is found
        if match:
            # Create temporary value for length check condition
            temp = match.group(1)
            # Check match length, send invalid request if less than 4 digits
            if len(temp) < 4:
                respTown = 'Invalid request – check format'
            # If link check passes, proceed
            else:
                # Extract zip code from match. Pad with leading zero if zipCode match is less than five digits
                zipCode = match.group(1).zfill(5)
                # Extract town data from dictionary and assign that information to respTown
                respTown = (zipDict.get(zipCode))
        # If no match, send invalid request message
        else:
            respTown = 'Invalid request – check format'

        # Gather town information from respTown and convert it to string
        zipResp = str(respTown)

        # Set respLines to header information required for transit of data back to client
        respLines = "HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n"

        # Send data using encoded values for 'zipResp' and 'respLines'
        servConn.sendall(respLines.encode() + zipResp.encode())

        # Close connection when finished
        servConn.close()


csv_zip_server()

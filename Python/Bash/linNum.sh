#!/bin/bash

#######################################################
#  _       _____ ______      ______  _     _ ______  
# | |     (_____)  ___ \ ___|  ___ \| |   | |  ___ \ 
# | |        _  | |   | (___) |   | | |   | | | _ | |
# | |       | | | |   | |___| |   | | |   | | || || |
# | |_____ _| |_| |   | (___) |   | | |___| | || || |
# |_______|_____)_|   |_|   |_|   |_|\______|_||_||_|
# 
#######################################################

USER=$(whoami)
HOSTNAME=$(hostname)
DIRECTORY=$(pwd)
USERID=$(id)

SYSTEMINFO=$(uname -a)
if [ -r "/etc/shadow" ]
then 
    ETCSHADOW=$(cat /etc/shadow)
fi

if [ -r "/etc/group" ]
then 
    ETCGROUPS=$(cat /etc/group)
fi

# Function to check if file is readable by current user and catting it if it is
#TEMPO=
#for FILE in @; do
    #if [-r $CURRENT_FILE]
    #then FILES=$(echo -e "$(pwd)/"CURRENT_FILE\n")

TEMP=$(echo -e "USER: $USER\n" \
           "# HOSTNAME\n$HOSTNAME\n" \
           "# Directory\n$DIRECTORY\n" \
           "# System Info\n$SYSTEMINFO\n" \
           "# Groups\n$ETCSHADOW\n$ETCGROUPS\n")

# BASE_INFO_LIST=()
# for current in $TEMP; do
# BASE_INFO_LIST+=$TEMP
# done
# #"echo -e $(pwd)/$TEMP"

# Recursively account for all files in standard partitions
MNT_FILES=$("ls -alhtr /mnt")
MEDIA_FILES=$("ls -alhtr /media")
TEMP_FILES=-$("ls -alhtr /tmp")
HOME_FILES=$("ls -ahlR /home")

VAR_FILES=$("find /var/log -type f -exec ls -la {}")

# Account for all files within the Home dir that are readable by the user and !empty
echo -e "Within the Home directory, the following files are readable by the current user:\n "
for FILE in $HOME_FILES; do
# do echo -e $FILE > ReadableFiles.txt
if [ -e "$FILE" ] && [ -r "$FILE" ]
then echo -e "$FILE > HomeFiles.txt\n"; echo -e "$FILE"
fi
done

# Recursively list and cat all regular files within /etc/sysconfig:
if [ -d "/etc/sysconfig/" ]
then
    SYSCONFIG=$("find /etc/sysconfig/ -type f -exec cat {}")
fi

# List all files, dirs and subdirs with write perms in /etc/:
ETC_DUMP=$("ls -aRl /etc/ | awk '$1 ~ /w.$/' | grep -v lrwx 2>/dev/null")

# Show network interfaces:
if [ -d "/sbin/ifconfig" ]
then 
    NETINFO=$("/sbin/ifconfig -a")
fi
# "cat network-secret.txt"

MAIL=$("ls -alh /var/mail")

# Gather available process information
PROCESS_INFO_1=$(ps aux)
PROCESS_INFO_2=$(ps -ef)

# Find hidden files
HIDDEN=$("find /home -type f -iname '.*history' | grep -r lrwx 2>/dev/null")

# Find files that will execute with elevated priveleges:
SPECIAL_FILES=$("find / -perm -4000")

CONFIG_FILES=$(echo -e "# Resolv Configuration\n$(ls -la /etc/resolv.conf 2>/dev/null)\n" \
               "# Syslog Configuration\n$(ls -la /etc/syslog.conf 2>/dev/null)\n" \
               "# CHTTP Configuration\n$(ls -la /etc/chttp.conf 2>/dev/null)\n" \
               "# Lighttpd Configuration\n$(ls -la /etc/lighttpd.conf 2>/dev/null)\n" \
               "# Cupsd Configuration\n$(ls -la /etc/cups/cupsd.conf 2>/dev/null)\n" \
               "# Inetd Configuration\n$(ls -la /etc/inetd.conf 2>/dev/null)\n" \
               "# XAMPP HTTPD Configuration\n$(ls -la /opt/lampp/etc/httpd.conf 2>/dev/null)\n" \
               "# Samba Configuration\n$(ls -la /etc/samba/smb.conf 2>/dev/null)\n" \
               "# OpenLDAP Configuration\n$(ls -la /etc/openldap/ldap.conf 2>/dev/null)\n" \
               "# LDAP Configuration\n$(ls -la /etc/ldap/ldap.conf 2>/dev/null)\n" \
               "# Exports Configuration\n$(ls -la /etc/exports 2>/dev/null)\n" \
               "# Auto Master Configuration\n$(ls -la /etc/auto.master 2>/dev/null)\n" \
               "# Alternate Auto Master Configuration\n$(ls -la /etc/auto_master 2>/dev/null)\n" \
               "# Filesystem Table\n$(ls -la /etc/fstab 2>/dev/null)\n" \
               "# Issue Configuration\n$(ls -la /etc/issue{,.net} 2>/dev/null)\n" \
               "# Master Password File\n$(ls -la /etc/master.passwd 2>/dev/null)\n" \
               "# Group Configuration\n$(ls -la /etc/group 2>/dev/null)\n" \
               "# Hosts Configuration\n$(ls -la /etc/hosts 2>/dev/null)\n" \
               "# Crontab Configuration\n$(ls -la /etc/crontab 2>/dev/null)\n" \
               "# Sysctl Configuration\n$(ls -la /etc/sysctl.conf 2>/dev/null)\n")


CONFIG_FILE_DUMP=$(echo -e "# Resolv Configuration\n$(cat /etc/resolv.conf 2>/dev/null)\n" \
               "# Syslog Configuration\n$(cat /etc/syslog.conf 2>/dev/null)\n" \
               "# CHTTP Configuration\n$(cat /etc/chttp.conf 2>/dev/null)\n" \
               "# Lighttpd Configuration\n$(cat /etc/lighttpd.conf 2>/dev/null)\n" \
               "# Cupsd Configuration\n$(cat /etc/cups/cupsd.conf 2>/dev/null)\n" \
               "# Inetd Configuration\n$(cat /etc/inetd.conf 2>/dev/null)\n" \
               "# XAMPP HTTPD Configuration\n$(cat /opt/lampp/etc/httpd.conf 2>/dev/null)\n" \
               "# Samba Configuration\n$(cat /etc/samba/smb.conf 2>/dev/null)\n" \
               "# OpenLDAP Configuration\n$(cat /etc/openldap/ldap.conf 2>/dev/null)\n" \
               "# LDAP Configuration\n$(cat /etc/ldap/ldap.conf 2>/dev/null)\n" \
               "# Exports Configuration\n$(cat /etc/exports 2>/dev/null)\n" \
               "# Auto Master Configuration\n$(cat /etc/auto.master 2>/dev/null)\n" \
               "# Alternate Auto Master Configuration\n$(cat /etc/auto_master 2>/dev/null)\n" \
               "# Filesystem Table\n$(cat /etc/fstab 2>/dev/null)\n" \
               "# Issue Configuration\n$(cat /etc/issue{,.net} 2>/dev/null)\n" \
               "# Master Password File\n$(cat /etc/master.passwd 2>/dev/null)\n" \
               "# Group Configuration\n$(cat /etc/group 2>/dev/null)\n" \
               "# Hosts Configuration\n$(cat /etc/hosts 2>/dev/null)\n" \
               "# Crontab Configuration\n$(cat /etc/crontab 2>/dev/null)\n" \
               "# Sysctl Configuration\n$(cat /etc/sysctl.conf 2>/dev/null)\n")


SERVICE_FILES=$(echo -e "# Home Directories\n$(ls -dla /home/*/ 2>/dev/null)\n" \
                  "# SSH Configurations\n$(ls -dla /home/*/.ssh/ 2>/dev/null)\n" \
                  "# SSH Authorized Keys\n$(ls -la /home/*/.ssh/authorized_keys 2>/dev/null)\n" \
                  "# SSH Known Hosts\n$(ls -la /home/*/.ssh/known_hosts 2>/dev/null)\n" \
                  "# SSH History - Filtered for 'ssh'\n$(grep ^ssh /home/*/._hist_ 2>/dev/null)\n" \
                  "# User History\n$(ls -la /home/*/._hist_ 2>/dev/null)\n" \
                  "# VNC and Subversion Configuration Files\n$(find /home/*/.vnc /home/*/.subversion -type f 2>/dev/null)\n" \
                  "# Telnet History - Filtered for 'telnet'\n$(grep ^telnet /home/*/._hist_ 2>/dev/null)\n" \
                  "# MySQL Command History\n$(ls -la /home/*/.mysql_history 2>/dev/null)\n" \
                  "# MySQL History - Filtered for 'mysql'\n$(grep ^mysql /home/*/._hist_ 2>/dev/null)\n" \
                  "# Vim Info\n$(ls -la /home/*/.viminfo 2>/dev/null)\n" \
                  "# Sudo Permissions\n$(sudo -l 2>/dev/null)\n" \
                  "# Crontab\n$(crontab -l 2>/dev/null)\n" \
                  "# Sudo Password Entry\n$(sudo -p)\n")


SERVICE_DUMP=$(echo -e "# Home Directories\n$(ls -alh /home/*/)\n" \
                  "# SSH Configurations\n$(ls -alh /home/*/.ssh/)\n" \
                  "# SSH Authorized Keys\n$(cat /home/*/.ssh/authorized_keys)\n" \
                  "# SSH Known Hosts\n$(cat /home/*/.ssh/known_hosts)\n" \
                  "# SSH History - Filtered for 'ssh'\n$(grep ^ssh /home/*/._hist_)\n" \
                  "# User History\n$(cat /home/*/._hist_)\n" \
                  "# VNC and Subversion Configuration Files\n$(find /home/*/.vnc /home/*/.subversion -type f)\n" \
                  "# Telnet History - Filtered for 'telnet'\n$(grep ^telnet /home/*/._hist_)\n" \
                  "# MySQL History - Filtered for 'mysql'\n$(grep ^mysql /home/*/._hist_)\n" \
                  "# MySQL Command History\n$(cat /home/*/.mysql_history)\n" \
                  "# Vim Info\n$(cat /home/*/.viminfo)\n" \
                  "# Sudo Permissions\n$(sudo -l 2>/dev/null)\n" \
                  "# Crontab\n$(crontab -l)\n" \\
                  "# Sudo Password Entry\n$(sudo -p)\n")


# "date"  "ls -ahlR /root/" "ls -ahlR /home/" "who" "w" "last" "arp -e" "/sbin/route -nee" "ps aux" "/var/mail/" "/root/" "/home/"

# "cat proof.txt" "cat network-secret.txt" "cat /etc/issue" "cat /etc/passwd" "cat /etc/group" "cat /etc/shadow" "cat /etc/sudoers" "cat /etc/network/interfaces" "cat /etc/services" "proof.txt" "network-secret.txt" 
# "/etc/issue" "/etc/passwd" "/etc/group" "/etc/shadow" "/etc/sudoers" 

failedLogin = 0;
with open("keystone.common.wsgi", "r") as allLine:
    counter = 0;
    for line in allLine:
        counter+=1;
        line  = line.rstrip('\n');
        if"- - - - -] Authorization failed" in line:
            failedLogin+=1;
            print(f"Line #{counter} {line} \n\n")
            
print(f"The number of failedLogin:{failedLogin}")

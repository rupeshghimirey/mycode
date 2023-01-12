failedLogin = 0;
successfulLogin = 0;
with open("keystone.common.wsgi", "r") as all_line:
    counter = 0;
    for line in all_line:
        counter+=1;
        line  = line.rstrip('\n');
        if"- - - - -] Authorization failed" in line:
            failedLogin+=1;
            print(f"Failed Line #{counter} {line} \n\n")
        else:
            successfulLogin+=1;
            print(f"Successful Line #{counter} {line} \n\n")
    print(f"Last line:  {line.split(' ')[-1]}")
            
print(f"The number of failedLogin is:{failedLogin}")


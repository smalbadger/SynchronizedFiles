
import time

def main():

    # clearing data file for fun
    with open("data.txt", "w") as f:
        f.write("")

    dataVal = 0

    while True: # Sensor continuously writes data in this loop

        dataVal += 1 # This is where you could get the sensor data

        # Write the sensor data to the file (append it)
        # ---------------------------------------------
        # The writing is done persistently. There is a chance that the reader is currently reading data.
        # If we try to write while the reader is reading, we'll get a permission error. If we get a permission
        # error, we just keep trying to write until we don't get a permission error anymore.
        while True:
            try:
                with open("data.txt", "a+") as dataFile:
                    dataFile.write(str(dataVal) + "\n")

                print("WRITE SUCCESS:", dataVal)
                break
            except PermissionError:
                print("WRITE FAILURE")

        time.sleep(15)  # wait for however long you want (I think you said you take measurements every 15 seconds)



if __name__ == "__main__":
    main()
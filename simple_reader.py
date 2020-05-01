import time

def main():
    while True: # GUI continuously reads in some loop

        # read all the sensor data
        #-------------------------
        # The reading is done persistently. There is a chance that the writer is currently writing data.
        # If we try to read while the writer is writing, we'll get a permission error. If we get a permission
        # error, we just keep trying to read until we don't get a permission error anymore.
        while True:
            try:
                with open("data.txt", "r") as dataFile:
                    print("READ SUCCESS:", ", ".join([x.strip() for x in dataFile.readlines()]))
                break
            except PermissionError:
                print("READ FAILURE")


        # do the tedious plotting down here to that you aren't holding onto the file longer than you need to.

        time.sleep(1)  # wait for however long you want.

if __name__ == "__main__":
    main()
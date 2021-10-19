inBytes = int(input("Please enter the amount of bytes\n"))
inKilobytes = inBytes / 1000
inKibibytes = inBytes / 1024
inMegabytes = inKilobytes / 1000
inMebibytes = inKibibytes / 1024


print(f"KiloBytes: {inKilobytes}, Kibibytes: {inKibibytes}, Megabytes: {inMegabytes}, Mebibytes: {inMebibytes}")

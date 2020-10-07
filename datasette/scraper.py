import os

import httpx

BASE_URL = httpx.URL("https://environment.data.gov.uk/public-register/")

REGISTERS = (
    # "waste-carriers-brokers",
    # "waste-exemptions",
    # "scrap-metal-dealers",
    # "enforcement-action",
    "water-discharge-exemptions",
    "flood-risk-exemptions",
    # "radioactive-substance",
    # "industrial-installations",
    # "waste-operations",
    # "end-of-life-vehicles",
    "water-discharges",
)


for register in REGISTERS:
    print(register)
    file_path = f"data/{register}.csv"
    try:
        if os.path.exists(file_path):
            continue
        outfile = open(file_path, "w")
        offset = 0
        limit = 200
        path = f"{register}/registration.csv"
        url = BASE_URL.join(path)
        while offset < 100000:
            req = httpx.get(url, params={"_limit": limit, "_offset": offset})
            lines = req.text.splitlines()
            if offset == 0:
                outfile.write(lines[0])
                outfile.write('\n')
            for line in lines[1:]:
                outfile.write(line)
                outfile.write('\n')
            offset += limit
    except (httpx.HTTPError, KeyError):
        os.remove(file_path)


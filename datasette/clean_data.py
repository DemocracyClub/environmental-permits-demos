import csv
import glob
import sys

fieldnames = ["register", "url", "label", "local_authority", "postcode"]

outfile = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
outfile.writeheader()


def file_name_to_function_name(filename):
    name = filename.replace(".csv", "").replace("data/", "").replace("-", "_")
    return f"clean_{name}"


def clean_flood_risk_exemptions(row):
    return {
        "register": "flood_risk_exemptions",
        "url": row["@id"],
        "label": row["registrationType.prefLabel"],
        "local_authority": row["localAuthority.label"],
        "postcode": row["site.siteAddress.postcode"]
    }


def clean_water_discharge_exemptions(row):
    return {
        "register": "water_discharge_exemptions",
        "url": row["@id"],
        "label": row["site.exemption.registrationType.comment"],
        "local_authority": row["localAuthority.label"],
        "postcode": row["site.siteAddress.postcode"]
    }


def clean_water_discharges(row):
    return {
        "register": "water_discharges",
        "url": row["@id"],
        "label": row["site.siteType.comment"],
        "local_authority": row["localAuthority.label"],
        "postcode": row["site.siteAddress.postcode"]
    }


for filename in glob.glob("data/*.csv"):
    with open(filename) as f:
        reader = csv.DictReader(f)
        func = file_name_to_function_name(filename)
        # print(filename)
        # print(next(reader))
        for line in reader:
            cleaned_line = locals()[func](line)
            outfile.writerow(cleaned_line)

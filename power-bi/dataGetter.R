### Play w/ environmental permits API

library(tidyverse)

# ## Here's a curl example:curl -i -H "Accept: text/turtle" http://environment.data.gov.uk/public-register/radioactive-substance/registration/GB3435DG
# url_with_parameters <- paste0("http://environment.data.gov.uk/public-register/radioactive-substance/registration/GB3435DG")
# result <- httr::GET(url_with_parameters)
# content <- httr::content(result)
# jsonlite::fromJSON("https://api.github.com/users/hadley/orgs")
# https://environment.data.gov.uk/public-register/enforcement-action/registration.csv?_limit=20
# easting=450&northing=150&dist=30
# read_csv("https://environment.data.gov.uk/public-register/enforcement-action/registration.csv")


base <- "https://environment.data.gov.uk/public-register/"

registers <- c("waste-carriers-brokers","waste-exemptions","scrap-metal-dealers",
               "enforcement-action","water-discharge-exemptions","flood-risk-exemptions",
               "radioactive-substance","industrial-installations","waste-operations",
               "end-of-life-vehicles","water-discharges")

endpoint <- "/registration.csv"

mods <- "?_limit=200&easting=450&northing=150&dist=30"

df <- paste0(base, registers, endpoint, mods) %>% 
  set_names %>% 
  map(~safely(read_csv)(.)) %>% map("result") %>% enframe %>% unnest(value)

write_csv(df, "output.csv")

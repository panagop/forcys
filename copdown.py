import copernicusmarine as cm

DATASET_ID = "med-hcmr-wav-rean-h"
DATASET_VERSION = "202105"
VARIABLES = ["VHM0", "VHM0_SW1", "VHM0_SW2", "VHM0_WW", "VMDR", "VMDR_SW1", "VMDR_SW2", "VMDR_WW",
             "VPED", "VSDX", "VSDY", "VTM01_SW1", "VTM01_SW2", "VTM01_WW", "VTM02", "VTM10", "VTPK"]
START_DATETIME = "1993-01-01T00:00:00"
END_DATETIME = "2020-12-31T23:00:00"


# 1	Ag Apostoloi
cm.subset(
    dataset_id=DATASET_ID,
    dataset_version=DATASET_VERSION,
    variables=VARIABLES,
    minimum_longitude=24.23,
    maximum_longitude=24.39,
    minimum_latitude=38.25,
    maximum_latitude=38.47,
    start_datetime=START_DATETIME,
    end_datetime=END_DATETIME,
)

# 2	Gyaros
cm.subset(
    dataset_id=DATASET_ID,
    dataset_version=DATASET_VERSION,
    variables=VARIABLES,
    minimum_longitude=24.47,
    maximum_longitude=24.77,
    minimum_latitude=37.50,
    maximum_latitude=37.70,
    start_datetime=START_DATETIME,
    end_datetime=END_DATETIME,
)

# 3	Donousa 2
cm.subset(
    dataset_id=DATASET_ID,
    dataset_version=DATASET_VERSION,
    variables=VARIABLES,
    minimum_longitude=25.81,
    maximum_longitude=26.02,
    minimum_latitude=37.05,
    maximum_latitude=37.16,
    start_datetime=START_DATETIME,
    end_datetime=END_DATETIME,
)

# 4 Crete 1
cm.subset(
    dataset_id=DATASET_ID,
    dataset_version=DATASET_VERSION,
    variables=VARIABLES,
    minimum_longitude=26.27,
    maximum_longitude=26.47,
    minimum_latitude=34.96,
    maximum_latitude=35.20,
    start_datetime=START_DATETIME,
    end_datetime=END_DATETIME,
)

# 5 Crete 2b
cm.subset(
    dataset_id=DATASET_ID,
    dataset_version=DATASET_VERSION,
    variables=VARIABLES,
    minimum_longitude=25.60,
    maximum_longitude=25.95,
    minimum_latitude=35.24,
    maximum_latitude=35.50,
    start_datetime=START_DATETIME,
    end_datetime=END_DATETIME,
)

# 6 Rhodes
cm.subset(
    dataset_id=DATASET_ID,
    dataset_version=DATASET_VERSION,
    variables=VARIABLES,
    minimum_longitude=27.55,
    maximum_longitude=27.77,
    minimum_latitude=35.77,
    maximum_latitude=36.20,
    start_datetime=START_DATETIME,
    end_datetime=END_DATETIME,
)

# 7 Chios
cm.subset(
    dataset_id=DATASET_ID,
    dataset_version=DATASET_VERSION,
    variables=VARIABLES,
    minimum_longitude=25.72,
    maximum_longitude=25.86,
    minimum_latitude=38.55,
    maximum_latitude=38.70,
    start_datetime=START_DATETIME,
    end_datetime=END_DATETIME,
)

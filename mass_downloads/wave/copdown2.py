import copernicusmarine as cm

DATASET_ID = "med-hcmr-wav-rean-h"
DATASET_VERSION = "202105"
VARIABLES = ["VHM0", "VHM0_SW1", "VHM0_SW2", "VHM0_WW", "VMDR", "VMDR_SW1", "VMDR_SW2", "VMDR_WW",
             "VPED", "VSDX", "VSDY", "VTM01_SW1", "VTM01_SW2", "VTM01_WW", "VTM02", "VTM10", "VTPK"]
START_DATETIME = "1993-01-01T00:00:00"
END_DATETIME = "2020-12-31T23:00:00"



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
    output_file="waveChios.nc"
)



# # Greece
# cm.subset(
#     dataset_id=DATASET_ID,
#     dataset_version=DATASET_VERSION,
#     variables=VARIABLES,
#     minimum_longitude=19,
#     maximum_longitude=29,
#     minimum_latitude=34,
#     maximum_latitude=41,
#     start_datetime=START_DATETIME,
#     end_datetime=END_DATETIME,
# )
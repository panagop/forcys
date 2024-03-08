import copernicusmarine as cm

cm.subset(
  dataset_id="med-hcmr-wav-rean-h",
  dataset_version="202105",
  variables=["VHM0", "VHM0_SW1", "VHM0_SW2", "VHM0_WW", "VMDR", "VMDR_SW1", "VMDR_SW2", "VMDR_WW", "VPED", "VSDX", "VSDY", "VTM01_SW1", "VTM01_SW2", "VTM01_WW", "VTM02", "VTM10", "VTPK"],
  minimum_longitude=25.83,
  maximum_longitude=26.01,
  minimum_latitude=37.05,
  maximum_latitude=37.15,
  start_datetime="2000-01-01T00:00:00",
  end_datetime="2024-02-29T23:00:00",

)

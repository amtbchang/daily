

import arcpy, math


if __name__ == '__main__':
	arcpy.CheckOutExtension("Spatial")
	
	# Define workspace and set input and output files
	arcpy.env.workspace = r'F:\fenggang\fenggang\fengfang_info'
	inDEM = r'F:\fenggang\fenggang\fengfang_info\dem_prj.tif'
	outTWI = r'F:\fenggang\fenggang\fengfang_info\twi.tif'

	# Intermediates
	arcpy.AddMessage("Filling DEM.\n")
	DEM_filled = arcpy.sa.Fill(inDEM)
	
	arcpy.AddMessage("Creating flow direction.\n")
	outFlowDirection = arcpy.sa.FlowDirection(DEM_filled, "FORCE")
	
	
	arcpy.AddMessage("Creating flow accumulation.\n")
	
	outFlowAccumulation = arcpy.sa.FlowAccumulation(outFlowDirection, "", "INTEGER") 
	
	arcpy.AddMessage("Creating slope.\n")
	slope = arcpy.sa.Slope(inDEM)* 1.570796  / 90#arcpy.sa.Slope(DEM_filled)
	tan_slp = arcpy.sa.Con( slope > 0, arcpy.sa.Tan(slope), 0.001 )
	sca_scaled = ( outFlowAccumulation + 1 ) * 30#cellsize
	TWI = arcpy.sa.Ln(sca_scaled / tan_slp )
	

	arcpy.AddMessage("Converting slope in degrees to slope in radians")
	# 2Pi
	#slope_radians = slope * math.pi/180.0
	
	# Output
	#arcpy.AddMessage("Creating TWI\n")
	#TWI = arcpy.sa.Ln(outFlowAccumulation*900 / arcpy.sa.Tan(slope))
	TWI.save(outTWI)
	arcpy.AddMessage("Saved TWI. Done.")

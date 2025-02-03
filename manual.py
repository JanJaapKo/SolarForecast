import plugin
import json
print("this script runs some tests on your deployment ")
newPlug = plugin.SolarForecastPlug()
newPlug.onStart()
newPlug.runCounter = 1
newPlug.onHeartbeat()
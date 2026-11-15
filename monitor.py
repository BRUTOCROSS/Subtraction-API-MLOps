import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Original input data
old_data = pd.DataFrame({
    "num1": [20, 30, 40, 50, 60, 70, 80, 90],
    "num2": [10, 15, 20, 25, 30, 35, 40, 45]
})

# New input data
new_data = pd.DataFrame({
    "num1": [100, 120, 140, 160, 180, 200, 220, 240],
    "num2": [5, 10, 15, 20, 25, 30, 35, 40]
})

# Create Evidently report
report = Report([
    DataDriftPreset()
])

result = report.run(
    reference_data=old_data,
    current_data=new_data
)

# Save HTML report
result.save_html("evidently_report.html")

print("Evidently report generated successfully!")

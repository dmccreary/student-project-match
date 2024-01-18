def convert_to_dictionary(project_list):
    project_capacities = {}
    for line in project_list:
        # Split the line at the first space to separate the number and the project name
        number, name = line.split('. ', 1)
        key = f"P{number}:{name}"
        project_capacities[key] = 5  # Assuming a default capacity of 5 for each project
    return project_capacities

# Example usage
project_list = [
    "1. Object Tracking",
    "2. Quadrotor",
    "3. RFID Monitoring",
    "4. Text Summarization",
    "5. Tabletop MRI",
    "6. GenAI Agents",
    "7. AI Assistant",
    "8. Robotic Arm",
    "9. Raspberry PI Supercomputer",
    "10. Spectrum Analyzer",
    "11. SunGuard",
    "12. 2D Assembly Platform",
    "13. AI Racing League",
    "14. Pronunciation Tool",
    "15. FMCW Radar",
    "16. Mag Particle Spectroscopy",
    "17. Object Detection FPGA",
    "18. Electrical Drive",
    "19. Vision Measurement",
    "20. 3D Digital Microscope"
]

project_capacities = convert_to_dictionary(project_list)
print(project_capacities)

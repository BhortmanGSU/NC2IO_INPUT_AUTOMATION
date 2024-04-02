import requests
import time

def send_http_command(url, params):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Request to {url} failed with status code {response.status_code}.")
    else:
        print(f"Request to {url} was successful.")

# Normal Up NC2IO A ROUTES
        
urls = [
    ("http://172.16.1.29/v1/shortcut", {"name": "input1_video_source", "source_name": "NC1IO-BRIDGE (NC1IO (CAM1 [Home]))"}),
    ("http://172.16.1.29/v1/shortcut", {"name": "input2_video_source", "source_name": "NC1IO-BRIDGE (NC1IO (CAM2 [1st]))"}),
    ("http://172.16.1.29/v1/shortcut", {"name": "input3_video_source", "source_name": "NC1IO-BRIDGE (NC1IO (CAM3 [3rd]))"}),
    ("http://172.16.1.29/v1/shortcut", {"name": "input4_video_source", "source_name": "NC1IO-BRIDGE (NC1IO (CAM4 [Outfield]))"}),
    ("http://172.16.1.29/v1/shortcut", {"name": "input5_video_source", "source_name": "NC1IO-BRIDGE (NC1IO (CAM5 [Talent]))"}),
    ("http://172.16.1.29/v1/shortcut", {"name": "input6_video_source", "source_name": "BIRDDOG-CROWS-NEST (CAM)"}),
    ("http://172.16.1.29/v1/shortcut", {"name": "input7_video_source", "source_name": "Black"}),
    ("http://172.16.1.29/v1/shortcut", {"name": "input8_video_source", "source_name": "Black"}),
    
    # Normal Up NC2IO B ROUTES
    ("http://172.16.1.63/v1/shortcut", {"name": "input1_video_source", "source_name": "SOFTBALL-BRIDGE (CONVO-AIDA-HD200 (BASKET-RIGHT-172.16.1.88))"}),
    ("http://172.16.1.63/v1/shortcut", {"name": "input2_video_source", "source_name": "SOFTBALL-BRIDGE (NC2IO-G-NDI2SDI (CAM 2 1ST ))"}),
    ("http://172.16.1.63/v1/shortcut", {"name": "input3_video_source", "source_name": "SOFTBALL-BRIDGE (NC2IO-G-NDI2SDI (CAM3 3RD))"}),
    ("http://172.16.1.63/v1/shortcut", {"name": "input4_video_source", "source_name": "SOFTBALL-BRIDGE (NC2IO-G-NDI2SDI (CAM4 OP OF))"}),
    ("http://172.16.1.63/v1/shortcut", {"name": "input5_video_source", "source_name": "SOFTBALL-BRIDGE (NC2IO-G-NDI2SDI (Cam 5 HH))"}),
    ("http://172.16.1.63/v1/shortcut", {"name": "input6_video_source", "source_name": "SOFTBALL-BRIDGE (NC2IO-G-NDI2SDI (Cam 6 - NDI OF))"}),
    ("http://172.16.1.63/v1/shortcut", {"name": "input7_video_source", "source_name": "BIRDDOG-CROWS-NEST (CAM)"}),
    ("http://172.16.1.63/v1/shortcut", {"name": "input8_video_source", "source_name": "Black"})
]

for url, params in urls:
    send_http_command(url, params)
    time.sleep(0.5)  # wait for 0.5 seconds
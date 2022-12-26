# License Plate Recognition System (LPR)

## How it works?
YoloV7 is used for license plate detection.    
Tesseract OCR is used for recognizing ntext on the number plate.    

## Installation
Clone our repository   
`git clone https://github.com/madaooftheblues/yolov7-lpr`    
  
Move to the cloned repository       
`cd yolov7-lpr`       

Create a python virtual environment     
`python3 -m venv venv`        

Activate the virtual environment   
**On Windows:**  
`venv\Scripts\activate.bat`    

**On Linux/MacOS:**    
`source venv/bin/activate`    

Install dependencies    
`pip install -r requirements.txt`     

## Usage
Run detect.py    
`python detect.py --source <path> --weights runs/train/yolo_lpr_pakistan-custom/weights/best.pt --conf 0.25 --name results`      

Where <path> is the path to the input.    

Results will be saved in `runs/detect/`         

Add `--save-crop` flag if you want to save the bounded box      

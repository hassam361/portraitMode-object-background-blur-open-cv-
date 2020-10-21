# portraitMode-object-background-blur-open-cv-
This is a background technique using thresholding and contours detection. 
Working: 
threshold the original image
use contours detection (open cv) 
detect the largest contour 
apply white mask to it 
do a full gaussian blur on a copy of original image 
now use the mask to redraw the original image pixels on the blurred image.


there are some failure points as well, it is unable to detect objects that have color matching with the background image so it creates a mess over there. 
| Class | Instance Variable | Datatype  | Mutable |
| ------------- |:-------------:| :-----:| :-----:|
| mobile | fname | string | No |
| mobile | lname| string | No |
| mobile | phone_number | list | Yes |
| mobile | messages | list | Yes |
| mobile | contacts | list | Yes |
| mobile | max_contacts | list | Yes |
| mobile | battery_life | int | No |
| mobile | singnal_strength | int | No |
| mobile | network_connection | boolen | No |
| mobile | phone_status | string | No |
| contact | fname | string | No |
| contact | lname| string | No |
| contact | phone_number| int | No |
| contact | MAXIMUM_CHAT_HISTORY| int | No |
| contact | chatHistory | list | Yes |



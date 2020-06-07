# FireDetectionOptimalColorspace
In this project, we have impleted a lightweight fire detection by transforming it to an optimal colorspace. The method detects fire at very early stages with less memory utilization. The optimal colorspace is obtained using Fuzzy-C-Means clustering and particle swarm optimization. Otsu's thresholding is applied on the new colorspace to identify the color pixels. 


## Publication
https://link.springer.com/chapter/10.1007/978-3-030-37218-7_131


## Abstract
With the increase in number of fire accidents, the need for the fire detection system is growing every year. Detecting the fire at early stages can prevent both material loss and loss of human lives. Sensor based fire detection systems are commonly used for detecting the fire. But they have drawbacks like time delay and close proximity. Vision based fire detectors are cost efficient and can potentially detect fire in its early stages. Here we propose a lightweight pixel based fire detection model to extract frames from videos and identify frames with fire in it. We use matrix multiplication to transform our input frame to a new color space in which separation of fire pixels from non-fire pixels is easier. The optimal value for the matrix to be multiplied is obtained using fuzzy-c- means clustering and particle swarm optimization. Otsu thresholding is applied on transformed image in new color space to classify the fire pixels in the frame. Our result shows high accuracy on forest fire videos with very less inference time.


## Output 
![output_image](https://github.com/Thangamgm2000/FireDetectionOptimalColorspace/blob/master/output.png)
&nbsp;&nbsp;&nbsp;![output_gif](https://github.com/Thangamgm2000/FireDetectionOptimalColorspace/blob/master/source_video.gif)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![output_gif](https://github.com/Thangamgm2000/FireDetectionOptimalColorspace/blob/master/output_gif.gif)


## Contributors
<ul>
  <li><a href="https://github.com/Thangamgm2000">M. Thanga Manickam</a></li>
  <li><a href="https://github.com/yogesh5466">M. Yogesh</a></li>
  <li><a href="#">P. Sridhar</a></li>
  <li><a href="#">Senthil Kumar Thangavel</a></li>
  <li><a href="#">Latha Parameswaran</a></li>
</ul>


## Acknowledgment

This proposed work is a part of the project supported by DST (DST/TWF Division/AFW for EM/C/2017/121) titled A framework for event modelling and detection for Smart Buildings using Vision Systems to Amrita Vishwa Vidyapeetham, Coimbatore.

## Cite this paper as:
Thanga Manickam M., Yogesh M., Sridhar P., Thangavel S.K., Parameswaran L. (2020) Video-Based Fire Detection by Transforming to Optimal Color Space. In: Smys S., Tavares J., Balas V., Iliyasu A. (eds) Computational Vision and Bio-Inspired Computing. ICCVBIC 2019. Advances in Intelligent Systems and Computing, vol 1108. Springer, Cham


## License
[MIT](https://choosealicense.com/licenses/mit/)

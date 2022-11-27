# Prokudin-Gorskii-Photo-Collection-Enhancement

Sergei Mikhailovich Prokudin-Gorskii (1863-1944), a Russian chemist and photographer, is considered as a pioneer
in color photography. With Tsar’s special permission and funding, he traveled across the Russian Empire, and took
color photographs of people, daily life, buildings, landscapes, etc., documenting the early 20th-century Russia. He
produced these color photographs by using a simple but ingenious idea: recording three exposures of every scene
onto a glass plate using a blue, a green, and a red filter. These negative plates is now in possession by the Library
of Congress of U.S.A., and have been recently digitized.


Below is an example input photo:



![image](https://user-images.githubusercontent.com/80748060/204113907-24b495a0-13e2-4309-90be-9eea8d0ddb52.png)


Below is an example output of the code:


![image](https://user-images.githubusercontent.com/80748060/204113905-90b4b3b6-97a6-452e-9457-04b4f61661dc.png)


There are 29 similar photos exist on a glass plates. They are queued as blue,green and red from top to bottom.
- Photos are taken one by one.
- At the preprocessing stage, unnecessary pixels (15 pixel) will be trimmed from top,bottom,left and right.
- After trimming, assumption is they are equally divided at the y-axis.
- From top to height/3 pixels are blue channel, from height/3 to 2*height/3 pixels are green channel and rest is red channel.
- After this step sum of squared distances are calculated for better alignment.
- Search range is [-15, 15] pixels for both x and y axis.
- Main channel is blue and templates are green and red.
- After finding the best alignment for green and red, images are shifted and after that merged.

For obtaining better results, defects on the images should be neutralized before applying these steps. Also, each channels should have more length on y-axis and search range should be bigger.

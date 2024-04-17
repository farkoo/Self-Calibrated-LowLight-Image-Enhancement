# Self-Calibrated Low-Light Image Enhancement


This repository contains the implementation of our paper [**"Revealing Shadows: Low-Light Image Enhancement Using Self-Calibrated Illumination"**](https://arxiv.org/abs/2312.15199). If you have any questions or need assistance with understanding the code or the concepts discussed in the paper, feel free to reach out.

------------------------------------------------

In digital imaging, enhancing visual content in poorly lit environments is a significant challenge, as images often suffer from inadequate brightness, hidden details, and an overall reduction in quality. This issue is especially critical in applications like nighttime surveillance, astrophotography, and low-light videography, where clear and detailed visual information is crucial. Our research addresses this problem by enhancing the illumination aspect of dark images. We have advanced past techniques by using varied color spaces to extract the illumination component, enhance it, and then recombine it with the other components of the image. By employing the Self-Calibrated Illumination method, a strategy initially developed for RGB images, we effectively intensify and clarify details that are typically lost in low-light conditions. This method of selective illumination enhancement leaves the color information intact, thus preserving the color integrity of the image. Crucially, our method eliminates the need for paired images, making it suitable for situations where they are unavailable. Implementing the modified SCI technique represents a substantial shift from traditional methods, providing a refined and potent solution for low-light image enhancement. Our approach sets the stage for more complex image processing techniques and extends the range of possible real-world applications where accurate color representation and improved visibility are essential.


### HSV Analysis
<figure>
  <p align="center">
    <img src="https://github.com/farkoo/Self-Calibrated-LowLight-Image-Enhancement/blob/master/HSV.jpg" alt="Block Diagram">
  </p>
  <figcaption>Analysis of the brightness and color components within the HSV color space for a selected image from the LOL dataset. The top row displays a reference image with distinct H (Hue), S (Saturation), and V (Value) channels, accompanied by histograms demonstrating an even distribution across all components. In contrast, the bottom row presents the underexposed image revealing a compressed V channel, indicative of diminished brightness, while the H and S channels remain relatively unaffected.</figcaption>
</figure>


### YCbCr Analysis
<figure>
  <p align="center">
    <img src="https://github.com/farkoo/Self-Calibrated-LowLight-Image-Enhancement/blob/master/YCbCr.jpg" alt="Block Diagram">
  </p>
  <figcaption>Investigation of the luminance and color channels in the YCbCr color space within a selected image from the LOL dataset. Top row: Reference image with detailed Y, Cr, Cb channels and balanced histograms. Bottom row: Low-light image with a compressed Y channel, approximately consistent Cr, Cb channels, and histograms illustrating the need for luminance enhancement.</figcaption>
</figure>

### Block Diagram of our method
<figure>
  <p align="center">
    <img src="https://github.com/farkoo/Self-Calibrated-LowLight-Image-Enhancement/blob/master/Block%20Diagram.png" alt="Block Diagram">
  </p>
  <figcaption>Block Diagram of our method, illustrating the low-light image enhancement process using SCI: starting from the import of the original RGB image, conversion to another color space that can extract the illumination component, application of the SCI enhancement techniques to the illumination component, and recombination with the other original components to produce the final enhanced image</figcaption>
</figure>

### Comparison with State-of-the-art
<figure>
  <p align="center">
    <img src="https://github.com/farkoo/Self-Calibrated-LowLight-Image-Enhancement/blob/master/LOL%20Result.png" alt="Block Diagram">
  </p>
</figure>

<figure>
  <p align="center">
    <img src="https://github.com/farkoo/Self-Calibrated-LowLight-Image-Enhancement/blob/master/LOL-v2%20Result.png" alt="Block Diagram">
  </p>
</figure>

### Visual comparison of the efficiency of the proposed method
<figure>
  <p align="center">
    <img src="https://github.com/farkoo/Self-Calibrated-LowLight-Image-Enhancement/blob/master/Visual%20Comparision.png" alt="Block Diagram">
  </p>
  <figcaption>Comparative visualization of the proposed method's performance using an image from the LOL dataset. The sequence from left to right displays the original low-light image, the image enhanced by our method, and the reference normal-light image for comparison.</figcaption>
</figure>

نتیجه گیریییییییییییییییییییییییییییییییی

citation

اطلاعات تماسسسسسسسسسسس

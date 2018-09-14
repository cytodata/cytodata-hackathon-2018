# :microscope: CytoData - 2018 Challenge 

The CytoData 2018 Challenge features batch effect correction and cross dataset profile matching :cd: :twisted_rightwards_arrows: :dvd:. 
The challenge involves the transformation of signatures using machine learning :space_invader: or statistical methods :bar_chart:. 
You will be given two datasets of image-based signatures :cd: :heavy_plus_sign: :dvd: acquired at different times :date: :clock130: and with different experimental conditions :pill: :syringe: with the goal of retrieving correct matches accurately :dart:. 
See http://cytodata.org/ for more details.

# :tv: Background

:alien: **: What is image-based profiling?**

:sunglasses: : In the study of biological systems, microscopy images are used to measure the response of cells to treatments or perturbations. 
Cell state can be observed and quantitatively measured using images by following a computational workflow known as profiling. 
Single cells are first identified in all images, and then their main characteristics are represented in feature vectors.
The information of a population of cells is aggregated into a single vector, also called profile, containing summary statistics of the features of all cells.
These profiles encode the morphological changes of cell populations exposed to treatments.
Image-based profiles can be used to compare the response of cells to different treatments, and to map their similarities.

<p align="center">
  <img src="files/profiling.png?raw=True" alt="Profiling"/>
</p>


:alien: **: Is image-based profiling the same as image-based screening?**

:sunglasses: : Screening and profiling are different. 
Screening uses images to identify a phenotype of interest known beforehand.
Profiling measures as many cell properties as possible to identify relationships among multiple phenotypes.


:alien: **: What are the applications of image-based profiling?**

:sunglasses: : Image-based profiles can be used for drug discovery and functional genomics applications. 
There are many types of biological studies that can be conducted using image-based profiling.
In the CytoData challenge, we use data from chemical and genetic perturbation experiments (see below).

<p align="center">
  <img src="files/application.png?raw=True" alt="Applications"/>
</p>


:alien: **: What imaging assays can be used for profiling?**

:sunglasses: : Virtually any imaging assay can be used for profiling, specially high-content assays.
In the CytoData challenge, we use an imaging assay called Cell Painting, that paints the cells with 6 stains, imaged in 5 channels, highlighting 8 cellular compartments. 
This is an unbiased, general purpose assay that maximizes information content for profiling, but the assay can be adapted to meet the needs of a research project.

<p align="center">
  <img src="files/cell_painting.png?raw=True" alt="Applications"/>
</p>


# :checkered_flag: Challenge 

As in many biological experiments, imaging data may be subject to batch effects and undesired artifacts :scream:.
More specifically, given two batches of microscopy images with the same treatments :pill:, but acquired under different technical conditions :a::vs::b:, a difference in the quantitative measures is likely to be observed :x:.
These differences are not due to meaningful biological variations and can be removed using computational methods :computer:.

The goal of the challenge :checkered_flag: is to analyze the profiles of two different batches of data :a::b: and design computational methods to correct batch effects :white_check_mark:.
A successful method :trophy: will be able to align the information content of both batches :ab:, 
making profiles of the same treatment have similar measurements without distorting the relationships among other treatments :smiley:.
The following metrics will be used to assess the quality of entries :triangular_ruler::

1. :arrow_upper_right::arrow_upper_right: Replicate correlation
2. :top::arrows_counterclockwise: Enrichment of biologically relevant matches in the top connections
3. :id::white_check_mark: Correct association of treatment type

## :bulb: Tip

From the data analysis perspective, the problem can be formulated in various ways, including 
manifold learning, domain adaptation, subspace alignment, and transfer learning.
Add an issue to this repository with links to relevant literature if you want to suggest a methodology and discuss it with other participants.

<p align="center">
  <img src="files/domains.png?raw=True" alt="Domains"/>
</p>


# :dvd: Data



# :performing_arts: Format

# :wrench: Resources

# 

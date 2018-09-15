# :microscope: CytoData - 2018 Challenge 

The CytoData 2018 Challenge features batch effect correction and cross dataset profile matching :cd: :twisted_rightwards_arrows: :dvd:. 
The challenge involves the transformation of signatures using machine learning :space_invader: or statistical methods :bar_chart:. 
You will be given two datasets of image-based signatures :cd: :heavy_plus_sign: :dvd: acquired at different times :date: :clock130: and with different experimental conditions :pill: :syringe: with the goal of retrieving correct matches accurately :dart:. 
See http://cytodata.org/ for details of the event.

## Table of Contents

[Background](#tv-background)

[Challenge](#checkered_flag-challenge)

[Data](#dvd-data)

[Format](#performing_arts-format)

[Resources](#wrench-resources)


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

<p align="center">
  <img src="files/domains.png?raw=True" alt="Domains"/>
</p>


# :dvd: Data

We are glad to announce that four datasets will be provided during the CytoData 2018 Challenge :tada::tada::tada::tada:. 
All of them were acquired using the Cell Painting assay, at high-throughput, in 384 well plates :microscope:, as part of the research 
conducted in the Broad Institute of MIT and Harvard. 
The following table describes the experimential details of each dataset.

| Dataset :dvd: | Type :syringe: :pill: | Number of treatments :hash: | Cell line :cancer: |
|---|---|---|---|
| BBBC037 | Genetic perturbations. ORF over-expression | 200 wild type genes | U2OS |
| BBBC043 | Genetic perturbations. ORF over-expression | 596 alleles of 53 genes | A549 |
| BBBC022 | Chemical perturbations. Bioactive compounds | 1,600 compounds | U2OS |
| BBBC036 | Chemical perturbations. Bioactive compounds | 5,000 compounds | U2OS |

Notice that two datasets represent genetic perturbations and the other two represent chemical perturbations.
The challenge will consider the cross-dataset matching problem across each of the two pairs :cd::twisted_rightwards_arrows::dvd:, 
i.e, profiles in BBBC037 have to be matched with profiles in BBBC043 because both contain genetic perturbations.
Similarly, profiles in BBBC022 have to be matched with profiles in BBBC036 because both contain chemical perturbations.

The imaging data for all three datasets is more than 3TB of data :boom:, which will be available to everyone during and after the challenge.
However, to facilitate the analysis of treatment profiles and to focus on the cross-dataset matching problem, all the datasets have been processed
before-hand using the profiling workflow described above :sunglasses:.
In particular, two versions of well-level population profiles will be available during the challenge: 
1. Classical features computed with the CellProfiler software using pipelines optimized for Cell Painting images.
2. Deep learning features computed with a convolutional neural network pretrained on ImageNet.


# :performing_arts: Format

The CytoData 2018 challenge will be a collaborative hackathon :sparkles::computer:, with participants forming teams to discuss and implement solutions to the problem.
The challenge will run for two days only, so participants are encouraged to investigate and plan some solutions before the venue starts :pencil:.
In order to meet other participants, we will provide a slack channel to make general announcements and allow participants to organize teams and exchange ideas :bulb:.
It's also a great idea to start discussing methods here in this GitHub repository :octocat:: 

```add issues with relevant links if you want to suggest a methodology and discuss it with other participants!```


Teams will have no less than three :three: and no more than five :five: participants, ideally from different institutions. 
Teams will compite with each other :rage1: to improve the three performance metrics mentioned before :bowling:.
Participants of the team will be able to upload solutions to a scoreboard to check that everything is running properly and to get feedback on performance :ok_hand:.
The best performing solutions will win prizes provided by our sponsors! :trophy::clap:


# :wrench: Resources

The following resources will be provided during the challenge:

1. :satellite: Internet connection.
2. :dvd: Access to all files of the four datasets, including pre-computed profiles.
3. :octocat: A toolkit, written in R and Python, to load the pre-computed profiles, run a baseline model and create a submission.
4. :chart_with_upwards_trend: An account in the scoreboard to evaluate the generated submissions.
5. :computer: Teams will be given access to pre-configured virtual machines in the Amazon Cloud to run experiments.

Participants of the challenge can make use of their own computational resources (laptops, servers, etc) to run experiments during the challenge.

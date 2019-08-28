# DAISE - Reimplementing a State-Of-The-Art Algorithm for Non-Intrusive Load Monitoring


The disaggregation of power consumption data of selected appliances,
called Non-Intrusive Load Monitoring (NILM), is an important
part of energy metering that promises energy savings and
higher comfort levels for occupants. By providing publicly available
datasets, that are used to test, verify, and benchmark possible
solutions to tackle the tasks of NILM, it is much more easier to get
a deeper understanding of the power consumption process in order
to reduce the waste of energy.
This code presents a reimplementation of the state-of-the-art
event detection algorithm Sequential Clustering-based Event Detection
For Non-Intrusive Load Monitoring. The algorithm will be applied
to a new Non-Intrusive Load Monitoring (NILM) dataset, called
building-level office environment dataset of typical electrical appliances
(BLOND). The algorithm is a Sequential Clustering-Based
Event Detection. It clusters sequential detection of abrupt changes
in an aggregate electricity consumption profile. The input signal is
decomposed into stationary and non-stationary segments and determines
events happening based on a certain event model. This method
presents the results of the algorithm for the BLOND in comparison
to the BLUED dataset.

# For further information read the paper "Groenning, Illner - DAISE - Reimplementing a State-Of-The-Art Algorithm"
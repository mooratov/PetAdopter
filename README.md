# PetAdopter
data exploration and predictive modeling for pet adoption

see the notebook for current prototype
`PROJECT parse petfinder description data - and make some quick attempt at predicting adoption rates` 


ToDo:
- find a better way to clean data
- use longitudinal aspect of the data (i.e. pet records disappearing with time) as additional cue for adoption
- if we still find positive data to be a defecit, we need to combine all positive records and sample from negative record distribution. 
- try other modeling methods.
- improve tokenization
- take the "ADOPTED!" out of positive records. As soon as this hting starts working, it should obviously be picking up on that as by far the most predictive token

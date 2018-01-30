The vehicles.py manages the dataset and it creates scatterplots and histogrems as it uses the data from the file. After that it saves the results in png and pdf files and because of some values which are missing, they are being converted into n/a. Lastly it is printing the following results: Mean, Median, Var, std and MAD(Median Absolute Deviation). 
The results are the following:

Index(['Current fleet', 'New Fleet'], dtype='object')
Mean: 30.481013
Median: 32.000000
Var: 36.831918
std: 6.068931
MAD: 4.000000


![logo](./veh_scaterplot.png?raw=true)
>>>>>>> 0c9d3809a6d844bd9675422b631cd3faafa2b4ea

![logo](./veh_histogram.png?raw=true)

The bootstr_vehicles.py removes the nan values in array, it gets the data for the current fleet column and after that it gets the data for the new fleet column.
The results are the following:

Current Fleet Standard Deviation : 20.14457831325301
Current Fleet Upper Bound: 6.944272735071886
Current Fleet Lower Bound 5.8116844542516555

New Fleet Standard Deviation : 30.481012658227847
New Fleet Upper Bound: 6.903292535493309
New Fleet Lower Bound 5.133611370461226

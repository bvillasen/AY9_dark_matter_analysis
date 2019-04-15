# Welcome

This is the repository for the AY9 Project: **Analysis of Dark Matter Simulations.**

<a href="https://bvillasen.github.io/blog/ay9project/" >The site for the project </a>

## Numerical Simulations  

For the simulations we use the Plank 2018 cosmological parameters:

H_0 = 67.66

Omega_matter = 0.3111

Omega_lambda = 0.6889

sigma_8 = 0.8102

n_s = 0.9665


## Instructions

<ol>

<li> First you need to open a terminal an make sure you are in a directory where you can read/write. </li>

<li> Clone this repository:</li>

```
git clone https://github.com/bvillasen/AY9_dark_matter_analysis.git
```
<li> Enter the newly created directory: </li>

```
cd AY9_dark_matter_analysis
```

<li> Enter the data directory:</li>



```
cd data
```

<li> Download the simulation outputs: </li>

```
wget https://www.dropbox.com/s/tgurthptvsphah5/128_dm.tar.gz
```

Now you have a file **128_dm.tar.gz** on your data directory, this file is compressed that's why the **.tar.gz** ending.

<li> Extract (decompress) the file: </li>

```
tar xvzf 128_dm.tar.gz
```

Now you have a folder called **128_dm** with the simulations outputs inside it

<li> Delete the .tar.gz file. Since we now have the decompressed file, the compressed file is no longer useful </li>

```
rm 128_dm.tar.gz
```

<li> See the contents of the 128_dm directory: </li>

```
ls 128_dm
```

</ol>

Now you are ready to load the data and do some analysis!

### Download new Snapshots for Halo analysis

<ol>

<li>Go to the project directory </li>

```
cd AY9_dark_matter_analysis
```

<li>Go to the data directory </li>

```
cd data
```

<li>Delete the previous data </li>

```
rm -r 128_dm
```

<li>Download the new data ( this data has a higher Force resolution ) </li>

```
wget https://www.dropbox.com/s/k3l2erbso3eu8jr/128_dm_halos.tar.gz
```

<li>Extract (decompress) the file: </li>

```
tar xvzf 128_dm_halos.tar.gz
```

<li>Delete the .tar.gz file. </li>

```
rm 128_dm_halos.tar.gz
```

<li>Download the Halo catalogs </li>

```
wget https://www.dropbox.com/s/mnobu3oqhk3nm4b/halo_catalogs_128.tar.gz
```

<li>Extract (decompress) the file: </li>

```
tar xvzf halo_catalogs_128.tar.gz
```

<li>Delete the .tar.gz file. </li>

```
rm halo_catalogs_128.tar.gz
```
### Install PYMC

Download the PYMC repository: 

```
git clone git://github.com/pymc-devs/pymc.git
```

Configure and install PYMC:

```
cd pymc
python setup.py config_fc --fcompiler gfortran build
python setup.py install --prefix=$HOME/.local

```


</ol>
